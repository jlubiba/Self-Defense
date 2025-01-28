from django import forms
from .models import Category, SubCategory, Tag, Post, Comment

category_options = []
for item in Category.objects.all():
    category_options.append(item)
subcategory_options = []
for item in SubCategory.objects.all():
    subcategory_options.append(item)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'added_by']
        
        widget = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'desciption': forms.Textarea(attrs={'class':'form-control'}),
            'added_by': forms.TextInput(attrs={'class':'form-control', 'type':'hidden', 'id':'author'}),
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'added_by']
        
        widget = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'added_by': forms.TextInput(attrs={'class':'form-control', 'type':'hidden', 'id':'author'}),
        }
        
class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name', 'description', 'category','added_by']
        
        widget = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'desciption': forms.Textarea(attrs={'class':'form-control'}),
            'categoty': forms.Select(attrs={'class':'form-control'}, choices=category_options),
            'added_by': forms.TextInput(attrs={'class':'form-control', 'type':'hidden', 'id':'author'}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'name', 'sub_category', 'body', 'tag']
        
        widget = {
            'author': forms.TextInput(attrs={'class':'form-control', 'type':'hidden', 'id':'author'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'sub_category': forms.Select(attrs={'class':'form-control'}, choices=subcategory_options),
            'tag': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'post', 'body']
        
        widget = {
            'author': forms.TextInput(attrs={'class':'form-control', 'type':'hidden', 'id':'author'}),
            'post': forms.TextInput(attrs={'class':'form-control', 'type':'hidden', 'id':'post_id'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }