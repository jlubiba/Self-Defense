from django.contrib import admin
from .models import Category, Tag, SubCategory, Post, Comment

# Register your models here.
# This makes it such that when the 'name' field is being filled, the 'slug' field is automatically field at the same time when done in the admin panel.
class AutoSlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}

admin.site.register(Category, AutoSlugAdmin)
admin.site.register(Tag, AutoSlugAdmin)
admin.site.register(SubCategory, AutoSlugAdmin)
admin.site.register(Post, AutoSlugAdmin)
admin.site.register(Comment)