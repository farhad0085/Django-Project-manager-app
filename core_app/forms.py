from django import forms
from .models import Project

class ProjectCreationForm(forms.ModelForm):
    """Forms for create new project"""
    
    class Meta:
        fields = '__all__'
        model = Project
    