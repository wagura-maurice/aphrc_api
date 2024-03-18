# application/post_categories/serializers.py
from rest_framework import serializers
from .models import Category

# The CategorySerializer class is a serializer in Python used for serializing and deserializing
# category objects.
class CategorySerializer(serializers.ModelSerializer):
    # The class `Meta` defines metadata for the `Category` model including fields and read-only
    # fields.
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

