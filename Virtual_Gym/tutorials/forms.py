from django import forms
from .models import *
import bleach
from django.forms import Textarea

class categoryForm(forms.ModelForm):
    class Meta:
        model = Category
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
        widgets = {
            "application": Textarea(attrs={"col":80, "row":20}),
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