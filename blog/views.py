from rest_framework.views import APIView
from tokenize import Token
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

# ✅ 1. Get All Posts (Without Pagination)
@api_view(['GET'])
def get_all_posts(request):
    posts = Post.objects.all().order_by('id')  # Fetch all posts
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)  # Return all posts

# ✅ 2. Get Posts With Pagination
@api_view(['GET'])
def get_paginated_posts(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10  # Show 10 posts per page
    posts = Post.objects.all().order_by('id')  # Fetch all posts
    result_page = paginator.paginate_queryset(posts, request)  # Paginate data
    serializer = PostSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)  # Paginated response

# ✅ 2. Get Single Post
@api_view(['GET'])
def get_post(request, id):
    post = get_object_or_404(Post, id=id)
    serializer = PostSerializer(post)
    return Response(serializer.data)

# ✅ 3. Create New Post
@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ 4. Update Post
@api_view(['PUT'])
def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    serializer = PostSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ 5. Delete Post
@api_view(['DELETE'])
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return Response({"message": "Post deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

# ✅ 6. Search Posts by Title
@api_view(['GET'])
def search_posts(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(title__icontains=query)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
