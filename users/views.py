# application/users/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
from decouple import config
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model
import jwt, datetime, re

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        # Extracting name, email, and password from request data
        name = request.data.get('name', '')
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        # Splitting name into first name, middle name, and last name
        names = name.split()
        first_name = names[0] if len(names) > 0 else ''
        middle_name = names[1] if len(names) > 1 else ''
        last_name = names[-1] if len(names) > 2 else ''

        # Extracting username from email address
        username = email.split('@')[0] if email else ''

        # Creating data dictionary for serializer
        serializer_data = {
            'first_name': first_name,
            'middle_name': middle_name,
            'last_name': last_name,
            'username': username,
            'email': email,
            'password': password,
        }

        # Serializing and saving user data
        serializer = UserSerializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response
    
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Logout successful'
        }
        return response

class PasswordResetRequestView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if email:
            user = User.objects.filter(email=email).first()
            if user:
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                token = PasswordResetTokenGenerator().make_token(user)
                DOMAIN_URL = config('DOMAIN_URL')  # Access DOMAIN_URL variable
                reset_link = f"{DOMAIN_URL}/api/password-reset-confirm/{uidb64}/{token}/"

                # Send the password reset email
                subject = 'Password Reset Request!'
                message = render_to_string('password_reset_confirm_email.html', {
                    'USERNAME': user.username,
                    'RESET_LINK': '',
                    'DOMAIN_URL': settings.DOMAIN_URL,
                    'PLATFORM_NAME': settings.PLATFORM_NAME
                })
                send_mail(subject, '', settings.DEFAULT_FROM_EMAIL, [email], html_message=message)

                return Response({'message': 'Password reset email sent'})
        return Response({'error': 'User with this email does not exist'})

class PasswordResetConfirmView(APIView):
    def post(self, request):
        uidb64 = request.data.get('uidb64')
        token = request.data.get('token')
        password = request.data.get('password')

        if uidb64 and token and password:
            try:
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)
                if PasswordResetTokenGenerator().check_token(user, token):
                    user.set_password(password)
                    user.save()
                    return Response({'message': 'Password reset successfully'})
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                pass
        return Response({'error': 'Invalid reset link'})

class AccountVerificationView(APIView):
    def post(self, request):
        uidb64 = request.data.get('uidb64')
        token = request.data.get('token')

        if uidb64 and token:
            try:
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)
                if PasswordResetTokenGenerator().check_token(user, token):
                    user.is_active = True
                    user.save()
                    return Response({'message': 'Account verified successfully'})
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                pass
        return Response({'error': 'Invalid verification link'})
