from django.contrib import admin
from .models import Category, SubCategory, Target, Technique, Combo, Tag

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Target)
admin.site.register(Technique)
admin.site.register(Combo)
admin.site.register(Tag)