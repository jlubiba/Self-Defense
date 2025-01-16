from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the welcoming page!")

class allBlogs(viewsets.ModelViewSet):
    queryset = Post.objects.prefetch_related("category", "tags").all()
    serializer_class = PostSerializer
    
class author(viewsets.ModelViewSet):
    queryset = User.objects.filter(groups__name="Author")
    serializer_class = AuthorSerializer
    
class Comment(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related("post", "user").all()
    serializer_class = CommentSerializer
    
class Category(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class Tag(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer