# application/post_catalogs/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # List all catalogs
    path('catalogs/', views.CatalogList.as_view(), name='post-catalogs.index'),  # GET request

    # Create a new Catalog
    path('catalogs/', views.CreateCatalog.as_view(), name='post-catalogs.store'),  # POST request

    # Show details of a specific Catalog
    path('catalogs/<int:pk>/', views.ShowCatalog.as_view(), name='post-catalogs.show'),  # GET request

    # Update a specific Catalog
    path('catalogs/<int:pk>/', views.UpdateCatalog.as_view(), name='post-catalogs.update'),  # PUT/PATCH request

    # Delete a specific Catalog
    path('catalogs/<int:pk>/', views.DeleteCatalog.as_view(), name='post-catalogs.delete'),  # DELETE request
]
