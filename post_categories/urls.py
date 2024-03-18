# application/post_categories/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # List all categories
    path('', views.CategoryIndex.as_view(), name='category-index'),  # GET request

    # Create a new category
    path('store/', views.StoreCategory.as_view(), name='category-store'),  # POST request

    # Show details of a specific category
    path('<int:pk>/show', views.ShowCategory.as_view(), name='category-show'),  # GET request

    # Update a specific category
    path('<int:pk>/update/', views.UpdateCategory.as_view(), name='category-update'),  # PUT/PATCH request

    # Delete a specific category
    path('<int:pk>/delete/', views.DeleteCategory.as_view(), name='category-delete'),  # DELETE request
]