# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

# The CustomUserAdmin class customizes the User model admin interface by removing references to groups
# and user permissions.
class CustomUserAdmin(BaseUserAdmin):
    # Remove references to groups and user_permissions
    filter_horizontal = []
    list_filter = []

# Register the User model with the custom admin class
admin.site.register(User, CustomUserAdmin)
