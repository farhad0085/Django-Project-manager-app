from django import forms
from django.http import request
from .models import Project, PROJECT_COLORS

class ProjectCreationForm(forms.Form):
    """Forms for create new project"""
    
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }), label="Project title", max_length=100)

    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 3
    }), label="Short description", max_length=500, required=False)

    
    def save(self, request):
        project = Project.objects.create(
            title=self.cleaned_data.get('title'),
            description=self.cleaned_data.get('description')
        )
        project.users.add(request.user)
        project.save()

    