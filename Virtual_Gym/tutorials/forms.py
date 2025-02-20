from django import forms
from .models import *
import bleach
from django.forms import Textarea

category_options = Category.objects.all().values_list('name', 'name') # This returns an obaject with a list a queryset
subcategory_options = SubCategory.objects.all().values_list('name', 'name') # This returns an obaject with a list a queryset

# Turning the 'category_options' queryset into a python list to use for choices
category_options_list = []
for item in category_options:
    category_options_list.append(item)
# Turning the 'subcategory_options' queryset into a python list to use for choices
subcategory_options_list = []
for item in category_options:
    subcategory_options_list.append(item)

class categoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        exclude = ("slug",)
        
        #Styling the fields of the form with bootsrap
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col-md-4'},),
            'description': forms.Textarea(attrs={'class': 'form-control col-md-4', 'rows':4},),
            'added_by': forms.TextInput(attrs={'class': 'form-control col-md-4', 'value':'', 'id':'author', 'type':'hidden'}),
            # 'added_by': forms.Select(attrs={'class': 'form-control col-md-4', 'value':'', 'id':'author', 'type':'hidden'}),
            }
    
    def validate(self, attrs):
        attrs['slug'] = bleach.clean(attrs['slug'])
        attrs['name'] = bleach.clean(attrs['name'])
        attrs['description'] = bleach.clean(attrs['description'])
        
        if (attrs['name'])<3:
            return forms.ValidationError('Name should be at least 3 character long.')
        if (attrs['slug'])<3:
            return forms.ValidationError('Slug should be at least 3 character long.')
        
        return super().validate(attrs)

class tagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
        exclude = ("slug",)
    
    def validate(self, attrs):
        attrs['slug'] = bleach.clean(attrs['slug'])
        attrs['name'] = bleach.clean(attrs['name'])
        
        if (attrs['name'])<3:
            return forms.ValidationError('Name should be at least 3 character long.')
        if (attrs['slug'])<3:
            return forms.ValidationError('Slug should be at least 3 character long.')
        
        return super().validate(attrs)

class subCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = "__all__"
        exclude = ("slug",)
        
        #Styling the fields of the form with bootsrap
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col-md-4'},),
            'description': forms.TextInput(attrs={'class': 'form-control col-md-4', 'rows':4},),
            'proper_execution': forms.Textarea(attrs={'class': 'form-control col-md-4', 'rows':4},),
            'added_by': forms.TextInput(attrs={'class': 'form-control col-md-4', 'value':'', 'id':'author', 'type':'hidden'}),
            'category': forms.Select(attrs={'class': 'form-control col-md-4'}, choices = category_options),
        }
    
    def validate(self, attrs):
        attrs['slug'] = bleach.clean(attrs['slug'])
        attrs['name'] = bleach.clean(attrs['name'])
        attrs['description'] = bleach.clean(attrs['description'])
        
        if (attrs['name'])<3:
            return forms.ValidationError('Name should be at least 3 character long.')
        if (attrs['slug'])<3:
            return forms.ValidationError('Slug should be at least 3 character long.')
        if (attrs['description'])<5:
            return forms.ValidationError('Description should be at least 5 character long.')
        
        return super().validate(attrs)

class targetForm(forms.ModelForm):
    class Meta:
        model = Target
        fields = "__all__"
        exclude = ("slug",)
    
    def validate(self, attrs):
        attrs['slug'] = bleach.clean(attrs['slug'])
        attrs['name'] = bleach.clean(attrs['name'])
        attrs['reason'] = bleach.clean(attrs['description'])
        
        if (attrs['name'])<3:
            return forms.ValidationError('Name should be at least 3 character long.')
        if (attrs['slug'])<3:
            return forms.ValidationError('Slug should be at least 3 character long.')
        if (attrs['reason'])<5:
            return forms.ValidationError('Reason should be at least 5 character long.')
        
        return super().validate(attrs)

class techniqueForm(forms.ModelForm):
    target = forms.ModelMultipleChoiceField(queryset=Target.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Technique
        fields = "__all__"
        exclude = ("slug",)
        
        #Styling the fields of the form with bootsrap
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col-md-4'},),
            'body_level': forms.Select(attrs={'class': 'form-control col-md-4'},),
            'action_types': forms.Select(attrs={'class': 'form-control col-md-4'},),
            'difficulty_level': forms.Select(attrs={'class': 'form-control col-md-4'},),
            'application': forms.TextInput(attrs={'class': 'form-control col-md-4'},),
            'steps': forms.Textarea(attrs={'class': 'form-control col-md-4',},),
            'sub_category': forms.Select(attrs={'class': 'form-control col-md-4'}),
            'target': forms.Select(attrs={'class': 'form-check form-check-inline col-md-4',},),
        }
    
    def validate(self, attrs):
        attrs['slug'] = bleach.clean(attrs['slug'])
        attrs['name'] = bleach.clean(attrs['name'])
        attrs['steps'] = bleach.clean(attrs['steps'])
        attrs['application'] = bleach.clean(attrs['application'])
        
        if (attrs['name'])<3:
            return forms.ValidationError('Name should be at least 3 character long.')
        if (attrs['slug'])<3:
            return forms.ValidationError('Slug should be at least 3 character long.')
        if (attrs['steps'])<8:
            return forms.ValidationError('Steps should be at least 8 character long.')
        if (attrs['application'])<8:
            return forms.ValidationError('Application should be at least 8 character long.')
        
        return super().validate(attrs)
        
class comboForm(forms.ModelForm):
    target = forms.ModelMultipleChoiceField(queryset=Target.objects.all(), widget=forms.CheckboxSelectMultiple)
    technique = forms.ModelMultipleChoiceField(queryset=Technique.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Combo
        fields = "__all__"
        exclude = ("slug",)
        
        #Styling the fields of the form with bootsrap
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col-md-4'},),
            'body_level': forms.Select(attrs={'class': 'form-control col-md-4'},),
            'action_types': forms.Select(attrs={'class': 'form-control col-md-4'},),
            'difficulty_level': forms.Select(attrs={'class': 'form-control col-md-4'},),
            'description': forms.TextInput(attrs={'class': 'form-control col-md-4'},),
            'technique': forms.Select(attrs={'class': 'form-check form-check-inline col-md-4',},),
            'target': forms.Select(attrs={'class': 'form-check form-check-inline col-md-4',},),
        }
    
    def validate(self, attrs):
        attrs['slug'] = bleach.clean(attrs['slug'])
        attrs['name'] = bleach.clean(attrs['name'])
        attrs['description'] = bleach.clean(attrs['description'])
        
        if (attrs['name'])<3:
            return forms.ValidationError('Name should be at least 3 character long.')
        if (attrs['slug'])<3:
            return forms.ValidationError('Slug should be at least 3 character long.')
        if (attrs['description'])<5:
            return forms.ValidationError('Description should be at least 5 character long.')
        
        return super().validate(attrs)

class textTutorialForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(queryset=TextTutorial.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = TextTutorial
        fields = "__all__"
        exclude = ("slug",)
    
    def validate(self, attrs):
        attrs['slug'] = bleach.clean(attrs['slug'])
        attrs['name'] = bleach.clean(attrs['name'])
        attrs['body'] = bleach.clean(attrs['body'])
        
        if (attrs['name'])<3:
            return forms.ValidationError('Name should be at least 3 character long.')
        if (attrs['slug'])<3:
            return forms.ValidationError('Slug should be at least 3 character long.')
        if (attrs['body'])<5:
            return forms.ValidationError('Body should be at least 5 character long.')
        
        return super().validate(attrs)

class videoTutorialForm(forms.ModelForm):
    class Meta:
        model = VideoTutorial
        fields = "__all__"
        exclude = ("slug",)
    
    def validate(self, attrs):
        attrs['slug'] = bleach.clean(attrs['slug'])
        attrs['name'] = bleach.clean(attrs['name'])
        attrs['description'] = bleach.clean(attrs['description'])
        
        if (attrs['name'])<3:
            return forms.ValidationError('Name should be at least 3 character long.')
        if (attrs['slug'])<3:
            return forms.ValidationError('Slug should be at least 3 character long.')
        if (attrs['description'])<5:
            return forms.ValidationError('Description should be at least 5 character long.')
        
        return super().validate(attrs)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'video', 'body')
        
        #Styling the fields of the form with bootsrap
        widgets = {
            'video': forms.TextInput(attrs={'class': 'form-control', 'value':'{{video_tutorial.id}}', 'id':'video_tutorial', 'type':'hidden'},),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'{{user.id}}', 'id':'author', 'type':'hidden'}),
            'body': forms.TextInput(attrs={'id':'comments', 'placeholder':'Enter comment...'}),
        }