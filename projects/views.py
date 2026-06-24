from django.shortcuts import redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Company, Project, Task
from .forms import CompanyForm, ProjectForm, TaskForm


# 🏠 HOME PAGE
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    # 🏢 ADD COMPANY
    if request.method == "POST" and "add_company" in request.POST:
        form = CompanyForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)

            if request.user.is_authenticated:
                obj.created_by = request.user
            else:
                obj.created_by = None

            obj.save()
            return redirect("home")

    # 📁 ADD PROJECT
    if request.method == "POST" and "add_project" in request.POST:
        form = ProjectForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)

            if request.user.is_authenticated:
                obj.created_by = request.user
            else:
                obj.created_by = None

            obj.save()
            return redirect("home")

    # 📝 ADD TASK
    if request.method == "POST" and "add_task" in request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)

            if request.user.is_authenticated:
                obj.assigned_to = request.user

            obj.save()
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
def edit_company(request, pk):
    company = get_object_or_404(Company, id=pk)
    form = CompanyForm(request.POST or None, instance=company)

    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "edit.html", {"form": form})


# ❌ DELETE COMPANY
def delete_company(request, pk):
    company = get_object_or_404(Company, id=pk)
    company.delete()
    return redirect("home")


# ✏️ EDIT PROJECT
def edit_project(request, pk):
    project = get_object_or_404(Project, id=pk)
    form = ProjectForm(request.POST or None, instance=project)

    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "edit.html", {"form": form})


# ❌ DELETE PROJECT
def delete_project(request, pk):
    project = get_object_or_404(Project, id=pk)
    project.delete()
    return redirect("home")


# ✏️ EDIT TASK
def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "edit.html", {"form": form})


# ❌ DELETE TASK
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect("home")


# 🔐 SIGNUP VIEW
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})