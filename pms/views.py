from django.shortcuts import render, redirect
from .models import Company, Project, Task
from .forms import CompanyForm, ProjectForm, TaskForm

def home(request):

    company_form = CompanyForm()
    project_form = ProjectForm()
    task_form = TaskForm()

    if request.method == "POST":

        if "add_company" in request.POST:
            company_form = CompanyForm(request.POST)
            if company_form.is_valid():
                obj = company_form.save(commit=False)
                obj.created_by = request.user
                obj.save()
                return redirect("home")

        if "add_project" in request.POST:
            project_form = ProjectForm(request.POST)
            if project_form.is_valid():
                obj = project_form.save(commit=False)
                obj.created_by = request.user
                obj.save()
                return redirect("home")

        if "add_task" in request.POST:
            task_form = TaskForm(request.POST)
            if task_form.is_valid():
                obj = task_form.save(commit=False)
                obj.assigned_to = request.user
                obj.save()
                return redirect("home")

    companies = Company.objects.filter(created_by=request.user)
    projects = Project.objects.filter(created_by=request.user)
    tasks = Task.objects.filter(assigned_to=request.user)

    return render(request, "home.html", {
        "company_form": company_form,
        "project_form": project_form,
        "task_form": task_form,
        "companies": companies,
        "projects": projects,
        "tasks": tasks,
    })