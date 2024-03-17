# application/users/urls.py

from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    UserView,
    LogoutView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
    AccountVerificationView
)

# Define your URLs for user-related views
urlpatterns = [
    path('sign-up/', RegisterView.as_view(), name='sign-up'),
    path('sign-in/', LoginView.as_view(), name='sign-in'),
    path('profile/', UserView.as_view(), name='profile'),
    path('sign-out/', LogoutView.as_view(), name='sign-out'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset-request'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('verify-account/', AccountVerificationView.as_view(), name='account-verification'),
]
