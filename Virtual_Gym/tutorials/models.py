from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
action_types = [('offense', 'Offense'), ('defense', 'Defense'), ('offense & defense', 'Offense & Defense')]
body_level = [('upper-body', 'Upper-body'), ('lower-body', 'Lower-body'), ('head', 'Head'), ('full-body', 'Full-body')]
difficty_level = [('novice', 'Novice'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')]

#Abstract model classes that well feel the other model with reused fields
class AddedElement(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Moves(AddedElement):
    body_level = models.CharField(max_length=50, choices=body_level)
    action_types = models.CharField(max_length=50, choices=action_types)
    difficty_level = models.CharField(max_length=50, choices=difficty_level)
    
    class Meta:
        abstract = True

# Models for the app
class Category(AddedElement):
    description = models.CharField(max_length=250)
    added_by= models.ForeignKey(User, on_delete=models.PROTECT,
                                related_name='tutorials_category_added_by')
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.added_by = request.user
        super().save_model(request, obj, form, change)
    
    def __str__(self):
        return self.name

class Tag(AddedElement):
    added_by= models.ForeignKey(User, on_delete=models.PROTECT)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.added_by = request.user
        super().save_model(request, obj, form, change)
    
    def __str__(self):
        return self.name

class SubCategory(AddedElement):
    description = models.CharField(max_length=250)
    proper_execution = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    added_by= models.ForeignKey(User, on_delete=models.PROTECT,
                                related_name='tutorials_subcategory_added_by')
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.added_by = request.user
        super().save_model(request, obj, form, change)
    
    def __str__(self):
        return self.name
    
class Target(AddedElement):
    body_level = models.CharField(max_length=50, choices=body_level)
    reason = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class Technique(Moves):
    steps = models.TextField()
    application = models.CharField(max_length=250)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT,
                                related_name='tutorials_technique_subcategory')
    target = models.ManyToManyField(Target, related_name='tutorials_technique_target')
    
    def __str__(self):
        return self.name
    
class Combo(Moves):
    description = models.CharField(max_length=250, default='A cool combo!')
    technique = models.ManyToManyField(Technique, related_name='technique')
    target = models.ManyToManyField(Target, related_name='tutorials_combo_target')
    
    def __str__(self):
        return self.name

class TextTutorial(AddedElement):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body = RichTextField(blank=True, null=True)
    sub_category = models.ManyToManyField(SubCategory, related_name='sub_category')
    tag = models.ManyToManyField(Tag, related_name='tag')
    
    def __str__(self):
        return self.name

class VideoTutorial(AddedElement):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="videos")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='static/images/tutorials')
    url = models.URLField()

    def __str__(self):
        return self.name