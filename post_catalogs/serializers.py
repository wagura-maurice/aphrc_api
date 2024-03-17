# application/post_catalogs/serializers.py'

from rest_framework import serializers
from .models import Catalog

class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'owner', 'category']
        read_only_fields = ['created_at', 'updated_at', 'owner']
