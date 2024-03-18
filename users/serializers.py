# application/users/serializers.py
from .models import User
from django.conf import settings
from rest_framework import serializers
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode

User = get_user_model()

# This class is a serializer for user objects in Python.
class UserSerializer(serializers.ModelSerializer):
    # The class Meta defines metadata for a User model in Python, including fields and extra kwargs.
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'middle_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'password', 'last_login', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """
        The function creates a new instance, sets the password, saves the instance, sends a welcome
        email with an account verification link, and returns the instance.
        
        :param validated_data: The `validated_data` parameter in the `create` method is typically a
        dictionary containing the validated input data that is passed to the serializer. This data has
        already been validated against the serializer's fields and is ready to be used to create a new
        instance of the model associated with the serializer. In your
        :return: The `instance` object is being returned after it has been created, saved to the
        database, and a welcome email has been sent.
        """
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()

        # Send welcome email with account verification link
        self.send_welcome_email(instance)

        return instance

    def update(self, instance, validated_data):
        """
        The `update` function updates a user instance with validated data, including username, email,
        and password if provided, and sends a profile update email.
        
        :param instance: Instance refers to the object or instance of a user that needs to be updated
        with the validated data. In this context, it likely represents a user profile that is being
        modified with new information such as username, email, and password
        :param validated_data: Validated data is the data that has been processed and validated
        according to the rules defined in the serializer class. In this context, it typically refers to
        the data provided in a request that has been validated before updating the user instance
        :return: The `instance` object is being returned after updating it with the validated data and
        saving the changes.
        """
        # Update user instance with validated data
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        
        # Check if the password is provided in the update request
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        
        instance.save()

        # Send profile update email
        self.send_profile_update_email(instance)

        return instance

    def send_welcome_email(self, instance):
        """
        The function sends a welcome email with a verification link to a new user.
        
        :param instance: The `instance` parameter in the `send_welcome_email` function likely represents
        an instance of a user object or a similar model in your application. It contains information
        about the user, such as their username, email, and primary key (pk)
        """
        uidb64 = urlsafe_base64_encode(force_bytes(instance.pk))
        token = PasswordResetTokenGenerator().make_token(instance)

        subject = 'Welcome!'
        message = render_to_string('welcome_email.html', {
            'USERNAME': instance.username,
            'ACCOUNT_VERIFICATION_URL': f"{settings.SPA_URL}/verify-account/?uidb64={uidb64}&token={token}",
            'SPA_URL': settings.SPA_URL,
            'PLATFORM_NAME': settings.PLATFORM_NAME
        })
        send_mail(subject, '', settings.DEFAULT_FROM_EMAIL, [instance.email], html_message=message)

    def send_profile_update_email(self, instance):
        """
        The function sends an email notification to a user after their profile has been updated.
        
        :param instance: The `instance` parameter in the `send_profile_update_email` function likely
        refers to an instance of a user profile or account that has been updated. It contains
        information about the user, such as their username, email address, and possibly other profile
        details
        """
        subject = 'Profile Updated!'
        message = render_to_string('profile_update_email.html', {
            'USERNAME': instance.username,
            'SPA_URL': settings.SPA_URL,
            'PLATFORM_NAME': settings.PLATFORM_NAME
        })
        send_mail(subject, '', settings.DEFAULT_FROM_EMAIL, [instance.email], html_message=message)
