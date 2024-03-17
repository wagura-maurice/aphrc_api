# post_categories/views.py

from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.db.models import Q
from .models import Category
from .serializers import CategorySerializer

class CategoryPagination(PageNumberPagination):
    page_size = 10  # Define the number of categories per page
    page_size_query_param = 'page_size'
    max_page_size = 100

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination  # Apply pagination logic

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get(self, request, *args, **kwargs):
        search_query = request.query_params.get('search', None)
        if search_query:
            self.queryset = self.queryset.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
        return super().get(request, *args, **kwargs)

class CreateCategory(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ShowCategory(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UpdateCategory(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        category = self.get_object()
        if category.created_by != self.request.user:
            raise PermissionDenied("You do not have permission to perform this action.")
        serializer.save()

class DeleteCategory(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.created_by != self.request.user:
            raise PermissionDenied("You do not have permission to perform this action.")
        instance.delete()
