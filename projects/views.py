from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Company, Project, Task
from .forms import CompanyForm, ProjectForm, TaskForm


@login_required
def home(request):

    # 🏢 ADD COMPANY
    if request.method == "POST" and "add_company" in request.POST:
        form = CompanyForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.save()
            return redirect("home")

    # 📁 ADD PROJECT
    if request.method == "POST" and "add_project" in request.POST:
        form = ProjectForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.save()
            return redirect("home")

    # 📝 ADD TASK
    if request.method == "POST" and "add_task" in request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {
        "company_form": CompanyForm(),
        "project_form": ProjectForm(),
        "task_form": TaskForm(),
        "companies": Company.objects.all(),
        "projects": Project.objects.all(),
        "tasks": Task.objects.all(),
    }

    return render(request, "home.html", context)


# ✏️ EDIT COMPANY
@login_required
def edit_company(request, pk):
    company = get_object_or_404(Company, id=pk)

    form = CompanyForm(request.POST or None, instance=company)
    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "edit.html", {"form": form})


# ❌ DELETE COMPANY
@login_required
def delete_company(request, pk):
    company = get_object_or_404(Company, id=pk)
    company.delete()
    return redirect("home")


# ✏️ EDIT PROJECT
@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, id=pk)

    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "edit.html", {"form": form})


# ❌ DELETE PROJECT
@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, id=pk)
    project.delete()
    return redirect("home")


# ✏️ EDIT TASK
@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)

    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "edit.html", {"form": form})


# ❌ DELETE TASK
@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect("home")