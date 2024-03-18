# post_catalogs/models.py
from django.db import models
from django.contrib.auth import get_user_model
from post_categories.models import Category

User = get_user_model()

# The `Catalog` class defines a model with fields for title, content, category, owner, timestamps, and
# related names for category and owner relationships.
class Catalog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='post_categories'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='users'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post_catalogs'  # Set the database table name explicitly

    def __str__(self):
        return self.title
