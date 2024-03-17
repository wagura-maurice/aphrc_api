# post_catalogs/models.py

from django.db import models
from django.contrib.auth import get_user_model
from post_categories.models import Category

User = get_user_model()

class Catalog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='catalogs')
    title = models.CharField(max_length=255)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_catalogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
