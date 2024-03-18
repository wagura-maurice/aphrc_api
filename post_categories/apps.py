from django.apps import AppConfig

# This class defines the configuration for the "post_categories" Django app with a default auto field
# set to 'BigAutoField'.
class PostCategoriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post_categories'
