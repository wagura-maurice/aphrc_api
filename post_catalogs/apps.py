from django.apps import AppConfig

# The `PostCatalogsConfig` class in the Django application `post_catalogs` specifies the default auto
# field as `BigAutoField`.
class PostCatalogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post_catalogs'
