# post_categories/models.py
from django.db import models

# This class represents a category in a Django model.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # The class `Meta` defines metadata options for the `Post Categories` model in Django, including
    # setting the verbose name plural and specifying the database table name explicitly.
    class Meta:
        verbose_name_plural = 'Post Categories'
        db_table = 'post_categories'

    def __str__(self):
        """
        The above function is a Python special method that returns the name attribute of an object when
        it is converted to a string.
        :return: The `__str__` method is returning the `name` attribute of the object.
        """
        return self.name
    