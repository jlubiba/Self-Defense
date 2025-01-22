from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    # slug = serializers.StringRelatedField(read_only=True)
    added_by = serializers.StringRelatedField()
    last_update = serializers.DateTimeField(source='update_date', read_only=True)
    class Meta:
        model = Category
        fields = ["name", "description","last_update", "added_by"]

class TagSerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField(read_only=True)
    added_by = serializers.StringRelatedField()
    class Meta:
        model = Tag
        fields = ["name", "update_date", "added_by"]

class SubCategorySerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField()
    added_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = SubCategory
        fields = ["slug", "name", "description", "proper_execution", "category", "update_date", "added_by"]

class TargetSerializer(serializers.ModelSerializer):
    # slug = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Target
        fields = ["name", "body_level","reason"]

class TechniqueSerializer(serializers.ModelSerializer):
    # slug = serializers.StringRelatedField(read_only=True)
    target = serializers.StringRelatedField(read_only=True, many=True)
    class Meta:
        model = Technique
        fields = ["name", "steps","target", "application"]

class ComboSerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField(read_only=True)
    technique = serializers.StringRelatedField(read_only=True, many=True)
    target = serializers.StringRelatedField(read_only=True, many=True)
    class Meta:
        model = Combo
        fields = ["name", "description","technique", "target"]

class TextTutorialSerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = TextTutorial
        fields = ["name", "body","subcategory","update_date", "author","added_by", "url", "tag"]

class VideoTutorialSerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = VideoTutorial
        fields = ["name", "subcategory","update_date", "author","added_by", "url"]