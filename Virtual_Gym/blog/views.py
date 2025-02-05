from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from rest_framework import viewsets
from .models import *
from .serializers import *
from .forms import CategoryForm, SubCategoryForm, CommentForm, PostForm, TagForm

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the welcoming page!")

class blogs(ListView):
    model = Post
    template_name = 'blog/blogtest_template.html'
    
    # This method that will allow for a context dict to be added onto the view
    def get_context_data(self, *args,**kwargs):
        posts = Post.objects.all()
        context = super(blogs, self).get_context_data(*args, **kwargs) # The view inside is the view the method is used in
        context['posts'] = posts
        context['blogform'] = PostForm
        return context

class allBlogs(viewsets.ModelViewSet):
    queryset = Post.objects.prefetch_related("category", "tags").all()
    serializer_class = PostSerializer
    # form_class = PostForm
    # template_name = 'blog/blogtest.html'
    
    def list(self, request):
        return render(request, 'blog/blogtest.html', {'blogform':PostForm})
    
    def get_context_data(self, *args, **kwargs):
        context = super(allBlogs, self).get_context_data(*args,**kwargs)
        post_form = PostForm
        context['post_form'] = post_form
        return context
    
    
class author(viewsets.ModelViewSet):
    queryset = User.objects.filter(groups__name="Author")
    serializer_class = AuthorSerializer
    
class Comment(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related("post", "user").all()
    serializer_class = CommentSerializer
    # form_class = CommentForm
    
class Category(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # form_class = CategoryForm
    
class Tag(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # form_class = TagForm