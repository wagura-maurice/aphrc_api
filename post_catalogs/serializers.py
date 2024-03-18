# application/post_catalogs/serializers.py'
from rest_framework import serializers
from .models import Catalog

# This class is a serializer in Python for a catalog model.
class CatalogSerializer(serializers.ModelSerializer):
    # The class Meta defines metadata for the Catalog model including fields and read-only fields.
    class Meta:
        model = Catalog
        fields = ['id', 'title', 'content', 'category', 'owner', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

