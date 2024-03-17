# post_catalogs/models.py

from django.db import models
from django.contrib.auth import get_user_model
from post_categories.models import Category

User = get_user_model()

class Catalog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_catalogs')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='catalogs')

    def __str__(self):
        return self.title
