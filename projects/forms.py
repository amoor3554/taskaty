from django import forms
from . import models

attr = {"class" : 'form-control'}


class ProjectModelForm(forms.ModelForm):
    
    class Meta():
        model = models.Project

        fields = ['title', 'description', 'category']
        
        widgets = {'category' : forms.Select(attrs=attr),
                   'title' : forms.TextInput(attrs=attr),
                    'description' : forms.Textarea(attrs=attr) }

class ProjectUpdateForm(forms.ModelForm):
    
    class Meta():
        model = models.Project

        fields = ['category', 'title', 'status']
        
        widgets = {'category' : forms.Select(attrs=attr),
                   'title' : forms.TextInput(attrs=attr),
                    'status' : forms.Select(attrs=attr)}
