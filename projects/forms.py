from django import forms
from .models import Company, Project, Task


# 🏢 COMPANY FORM
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']


# 📁 PROJECT FORM
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'company']


# 📝 TASK FORM
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'project', 'status', 'assigned_to']