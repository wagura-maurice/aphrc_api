from django.apps import AppConfig

# The `ManagementConfig` class in this Python code snippet sets the default auto field to
# `django.db.models.BigAutoField` for the `management` app.
class ManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'management'
