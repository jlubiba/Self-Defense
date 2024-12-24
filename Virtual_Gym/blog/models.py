from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    sub_category = models.ManyToManyField(SubCategory, related_name='sub_category')
    tag = models.ManyToManyField(Tag, related_name='tag')
    upload_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    text = RichTextField(max_length=750)
    
    def __str__(self):
        return f"{self.user}: \n {self.text}"