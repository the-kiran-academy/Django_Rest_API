from django.urls import path
from .views import (
    get_all_posts, get_paginated_posts, get_post, create_post, 
    update_post, delete_post, search_posts
)

urlpatterns = [
    path('posts/all/', get_all_posts, name='get-all-posts'),  # Get all posts (No pagination)
    path('posts/', get_paginated_posts, name='get-paginated-posts'),  # Get posts with pagination
    path('posts/<int:id>/', get_post, name='get-post'),  # Get single post
    path('posts/create/', create_post, name='create-post'),  # Create post
    path('posts/<int:id>/update/', update_post, name='update-post'),  # Update post
    path('posts/<int:id>/delete/', delete_post, name='delete-post'),  # Delete post
    path('posts/search/', search_posts, name='search-posts'),  # Search posts
]


