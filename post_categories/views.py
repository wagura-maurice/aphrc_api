# post_categories/views.py
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import CategorySerializer
from .models import Category

# The `CategoryPagination` class sets up pagination for categories with a page size of 10, allowing
# customization of the page size and limiting the maximum page size to 100.
class CategoryPagination(PageNumberPagination):
    page_size = 10  # Define the number of categories per page
    page_size_query_param = 'page_size'
    max_page_size = 100

# This class represents an API view for listing and creating Category objects with pagination and
# search functionality based on name and description.
class CategoryIndex(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination  # Apply pagination logic

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(name__icontains=search_query) | queryset.filter(description__icontains=search_query)
        return queryset

# This class represents a view for creating instances of the Category model with authentication and
# permission settings.
class StoreCategory(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save()

# This class is a Django REST framework API view for retrieving a single Category object.
class ShowCategory(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# The `UpdateCategory` class is a Django REST framework API view for updating Category objects with
# authentication and permission settings.
class UpdateCategory(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_update(self, serializer):
        serializer.save()

# This class is a Django REST framework view for deleting a Category object with authentication and
# permission checks.
class DeleteCategory(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_destroy(self, instance):
        instance.delete()