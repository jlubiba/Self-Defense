from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse, reverse_lazy

#Abstract model classes that well feel the other model with reused fields
class AddedElement(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, blank=True)
    
    class Meta:
        abstract = True

# Models for the app
class Category(AddedElement):
    description = models.CharField(max_length=250)
    added_by= models.ForeignKey(User, on_delete=models.PROTECT,
                                related_name='blog_category_added_by', null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('', kwargs={'pk': self.pk}) # Need to add the link to the place to be

class Tag(AddedElement):
    added_by= models.ForeignKey(User, on_delete=models.PROTECT,
                                related_name='blog_tag_added_by', null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('', kwargs={'pk': self.pk}) # Need to add the link to the place to be

class SubCategory(AddedElement):
    description = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    added_by= models.ForeignKey(User, on_delete=models.PROTECT,
                                related_name='blog_subcategory_added_by', null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('', kwargs={'pk': self.pk}) # Need to add the link to the place to be

class Post(AddedElement):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='blog_post_added_by', null=True)
    body = RichTextField(blank=True, null=True)
    sub_category = models.ManyToManyField(SubCategory, related_name='sub_category')
    tag = models.ManyToManyField(Tag, related_name='tag')
    
    def save(self, request, *args, **kwargs):
        self.slug = slugify(self.name)
        self.author = User.objects.filter(id=self.user)
        super(Post, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('', kwargs={'pk': self.pk}) # Need to add the link to the place to be
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                                related_name='blog_comment_post')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='blog_comment_added_by')
    body = RichTextField(max_length=750)
    slug = models.SlugField(unique=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Comment, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.user}: \n {self.text}"
    
    def get_absolute_url(self):
        return reverse('', kwargs={'pk': self.pk}) # Need to add the link to the place to be