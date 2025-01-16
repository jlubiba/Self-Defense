from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    added_by = serializers.StringRelatedField()
    last_update = serializers.DateTimeField(source='update_date', read_only=True)
    class Meta:
        model = Category
        fields = ["name", "description","update_date", "added_by"]

class TagSerializer(serializers.ModelSerializer):
    added_by = serializers.StringRelatedField()
    class Meta:
        model = Tag
        fields = ["name", "update_date", "added_by"]

class SubCategorySerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    added_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = SubCategory
        fields = ["name", "slug", "description", "category", "update_date", "added_by"]

class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    tag = serializers.StringRelatedField(read_only=True, many=True)
    class Meta:
        model = Post
        fields = ["user", "slug", "body", "sub_category","tag", "creation_date"]

class CommentSerializer(serializers.ModelSerializer):
    post = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ["post", "user", "text", "slug", "creation_date"]
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]