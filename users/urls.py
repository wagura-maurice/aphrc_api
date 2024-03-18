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

# This code block is defining URL patterns for the user-related views in a Django application. Each
# `path` function call specifies a URL pattern along with the corresponding view class that should be
# executed when that URL is accessed. Here's a breakdown of what each line is doing:
urlpatterns = [
    path('sign-up/', RegisterView.as_view(), name='sign-up'),
    path('sign-in/', LoginView.as_view(), name='sign-in'),
    path('profile/', UserView.as_view(), name='profile'),
    path('sign-out/', LogoutView.as_view(), name='sign-out'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset-request'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('verify-account/', AccountVerificationView.as_view(), name='account-verification'),
]
