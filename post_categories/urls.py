# application/post_categories/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # List all categories
    path('categories/', views.CategoryList.as_view(), name='post-categories.index'),  # GET request

    # Create a new category
    path('categories/', views.CreateCategory.as_view(), name='post-categories.store'),  # POST request

    # Show details of a specific category
    path('categories/<int:pk>/', views.ShowCategory.as_view(), name='post-categories.show'),  # GET request

    # Update a specific category
    path('categories/<int:pk>/', views.UpdateCategory.as_view(), name='post-categories.update'),  # PUT/PATCH request

    # Delete a specific category
    path('categories/<int:pk>/', views.DeleteCategory.as_view(), name='post-categories.delete'),  # DELETE request
]
