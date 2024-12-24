from django.db import models
from django.contrib.auth.models import User

# Create your models here.
action_types = [('offense', 'Offense'), ('defense', 'Defense'), ('offense & defense', 'Offense & Defense')]
body_level = [('upper', 'Upper'), ('lower', 'Lower'), ('head', 'Head'), ('full-body', 'Full-body')]
difficty_level = [('novice', 'Novice'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')]

class AddedElement(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=150)
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

class Category(AddedElement):
    description = models.CharField(max_length=250)
    added_by= models.ForeignKey(User, on_delete=models.PROTECT,
                                related_name='practice_category_added_by')
    
    def __str__(self):
        return self.name
    
class SubCategory(AddedElement):
    description = models.CharField(max_length=250)
    proper_execution = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    added_by= models.ForeignKey(User, on_delete=models.PROTECT,
                                related_name='practice_subcategory_added_by')
    
    def __str__(self):
        return self.name
 
class Tag(AddedElement):
    description = models.CharField(max_length=250)
    added_by= models.ForeignKey(User, on_delete=models.PROTECT,
                                related_name='practice_tag_added_by')
    
    def __str__(self):
        return self.name
    
class Target(models.Model):
    name = models.CharField(max_length=150)
    body_level = models.CharField(max_length=50, choices=body_level)
    reason = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class Technique(Moves):
    steps = models.TextField()
    application = models.CharField(max_length=250)
    target = models.ManyToManyField(Target, related_name='practice_technique_target_related')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    
class Combo(Moves):
    target = models.ManyToManyField(Target, related_name='practice_combot_target')
    description = models.CharField(max_length=250, default='A cool combo!')
    technique = models.ManyToManyField(Technique, related_name='practice_combo_technique')
    
    def __str__(self):
        return self.name