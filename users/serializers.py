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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'middle_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'password', 'last_login', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()

        # Send welcome email with account verification link
        self.send_welcome_email(instance)

        return instance

    def update(self, instance, validated_data):
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
        subject = 'Profile Updated!'
        message = render_to_string('profile_update_email.html', {
            'USERNAME': instance.username,
            'SPA_URL': settings.SPA_URL,
            'PLATFORM_NAME': settings.PLATFORM_NAME
        })
        send_mail(subject, '', settings.DEFAULT_FROM_EMAIL, [instance.email], html_message=message)
