# application/post_catalogs/serializers.py'
from rest_framework import serializers
from .models import Catalog

class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'title', 'content', 'category', 'owner', 'created_at', 'updated_at']

