from django.contrib import admin
from .models import Category, SubCategory, Target, Technique, Combo, Tag, TextTutorial, VideoTutorial

# Register your models here.

class AutoSlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}

admin.site.register(Category, AutoSlugAdmin)
admin.site.register(SubCategory, AutoSlugAdmin)
admin.site.register(Target, AutoSlugAdmin)
admin.site.register(Technique, AutoSlugAdmin)
admin.site.register(Combo, AutoSlugAdmin)
admin.site.register(Tag, AutoSlugAdmin)
admin.site.register(TextTutorial, AutoSlugAdmin)
admin.site.register(VideoTutorial, AutoSlugAdmin)