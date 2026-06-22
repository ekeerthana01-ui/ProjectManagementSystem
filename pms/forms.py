from django import forms
from .models import Company, Project, Task

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'company']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'project', 'status']