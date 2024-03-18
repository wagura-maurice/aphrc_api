# application/users/views.py
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        name = request.data.get('name', '')
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        names = name.split()
        first_name = names[0] if len(names) > 0 else ''
        middle_name = names[1] if len(names) > 1 else ''
        last_name = names[-1] if len(names) > 2 else ''

        username = email.split('@')[0] if email else ''

        serializer_data = {
            'first_name': first_name,
            'middle_name': middle_name,
            'last_name': last_name,
            'username': username,
            'email': email,
            'password': password,
        }

        serializer = UserSerializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()

        if user is None or not user.check_password(password):
            raise AuthenticationFailed('Invalid email or password')

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        })

class UserView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        response = Response()
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

                subject = 'Password Reset Request!'
                message = render_to_string('password_reset_confirm_email.html', {
                    'USERNAME': user.username,
                    'RESET_LINK': f"{settings.SPA_URL}/password-reset-confirm/?uidb64={uidb64}&token={token}",
                    'SPA_URL': settings.SPA_URL,
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
    