# post_catalogs/views.py

from rest_framework import generics, permissions, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.db.models import Q
from .models import Catalog
from .serializers import CatalogSerializer

class CatalogPagination(PageNumberPagination):
    page_size = 10  # Define the number of catalogs per page
    page_size_query_param = 'page_size'
    max_page_size = 100

class CatalogList(generics.ListCreateAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    pagination_class = CatalogPagination  # Apply pagination logic
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        owner_username = self.request.query_params.get('owner_username', None)
        category_name = self.request.query_params.get('category_name', None)

        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
        if start_date and end_date:
            queryset = queryset.filter(created_at__range=[start_date, end_date])
        if owner_username:
            queryset = queryset.filter(owner__username=owner_username)
        if category_name:
            queryset = queryset.filter(category__name=category_name)

        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CreateCatalog(generics.CreateAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ShowCatalog(generics.RetrieveAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer

class UpdateCatalog(generics.UpdateAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        catalog = self.get_object()
        if catalog.owner != self.request.user:
            raise PermissionDenied("You do not have permission to perform this action.")
        serializer.save()

class DeleteCatalog(generics.DestroyAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionDenied("You do not have permission to perform this action.")
        instance.delete()
