from django import forms
from . import models




class ProjectModelForm(forms.ModelForm):
    
    class Meta():
        model = models.Project

        fields = ['title', 'description', 'category']
        
        widgets = {'category' : forms.Select(),
                   'title' : forms.TextInput(),
                    'description' : forms.Textarea }

