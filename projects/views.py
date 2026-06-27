from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Company, Project, Task
from .forms import CompanyForm, ProjectForm, TaskForm


# 🏠 HOME PAGE (LOGIN REQUIRED)
@login_required(login_url='/login/')
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
            obj = form.save(commit=False)
            obj.assigned_to = request.user
            obj.save()
            return redirect("home")

    context = {
        "company_form": CompanyForm(),
        "project_form": ProjectForm(),
        "task_form": TaskForm(),

        "companies": Company.objects.filter(created_by=request.user),
        "projects": Project.objects.filter(created_by=request.user),
        "tasks": Task.objects.filter(assigned_to=request.user),
    }

    return render(request, "home.html", context)


# ✏️ EDIT COMPANY
def edit_company(request, pk):
    company = get_object_or_404(Company, id=pk, created_by=request.user)
    form = CompanyForm(request.POST or None, instance=company)

    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "edit.html", {"form": form})


# ❌ DELETE COMPANY
def delete_company(request, pk):
    company = get_object_or_404(Company, id=pk, created_by=request.user)
    company.delete()
    return redirect("home")


# ✏️ EDIT PROJECT
def edit_project(request, pk):
    project = get_object_or_404(Project, id=pk, created_by=request.user)
    form = ProjectForm(request.POST or None, instance=project)

    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "edit.html", {"form": form})


# ❌ DELETE PROJECT
def delete_project(request, pk):
    project = get_object_or_404(Project, id=pk, created_by=request.user)
    project.delete()
    return redirect("home")


# ✏️ EDIT TASK
def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk, assigned_to=request.user)
    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "edit.html", {"form": form})


# ❌ DELETE TASK
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk, assigned_to=request.user)
    task.delete()
    return redirect("home")


# 🔐 SIGNUP
# 🔐 SIGNUP
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})