# application/post_catalogs/urls.py
from django.urls import path
from . import views

# This code snippet is defining URL patterns for handling different HTTP requests related to catalogs
# in a Django application. Here's a breakdown of each URL pattern:
urlpatterns = [
    # List all catalogs
    path('', views.CatalogIndex.as_view(), name='catalog-index'),  # GET request

    # Create a new catalog
    path('store/', views.StoreCatalog.as_view(), name='catalog-store'),  # POST request

    # Show details of a specific catalog
    path('<int:pk>/show', views.ShowCatalog.as_view(), name='catalog-show'),  # GET request

    # Update a specific catalog
    path('<int:pk>/update/', views.UpdateCatalog.as_view(), name='catalog-update'),  # PUT/PATCH request

    # Delete a specific catalog
    path('<int:pk>/delete/', views.DeleteCatalog.as_view(), name='catalog-delete'),  # DELETE request
]