from django.apps import AppConfig

# The UsersConfig class in the Django application "users" sets the default auto field to
# 'BigAutoField'.
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
