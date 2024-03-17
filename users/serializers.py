# application/users/serializers.py

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
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
        subject = 'Welcome!'
        message = render_to_string('welcome_email.html', {
            'USERNAME': instance.username,
            'ACCOUNT_VERIFICATION_URL': '',
            'DOMAIN_URL': settings.DOMAIN_URL,
            'PLATFORM_NAME': settings.PLATFORM_NAME
        })
        send_mail(subject, '', settings.DEFAULT_FROM_EMAIL, [instance.email], html_message=message)

    def send_profile_update_email(self, instance):
        subject = 'Profile Updated!'
        message = render_to_string('profile_update_email.html', {
            'USERNAME': instance.username,
            'DOMAIN_URL': settings.DOMAIN_URL,
            'PLATFORM_NAME': settings.PLATFORM_NAME
        })
        send_mail(subject, '', settings.DEFAULT_FROM_EMAIL, [instance.email], html_message=message)
