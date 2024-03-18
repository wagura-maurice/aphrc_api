# post_categories/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Post Categories'
        db_table = 'post_categories'  # Set the database table name explicitly

    def __str__(self):
        return self.name
    