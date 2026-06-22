from django.shortcuts import render, redirect
from .models import Company, Project, Task
from .forms import CompanyForm, ProjectForm, TaskForm


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
def edit_company(request, pk):
    company = Company.objects.get(id=pk)

    form = CompanyForm(request.POST or None, instance=company)

    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "edit.html", {"form": form})


# ❌ DELETE COMPANY
def delete_company(request, pk):
    company = Company.objects.get(id=pk)
    company.delete()
    return redirect("home")


# ✏️ EDIT PROJECT
def edit_project(request, pk):
    project = Project.objects.get(id=pk)

    form = ProjectForm(request.POST or None, instance=project)

    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "edit.html", {"form": form})


# ❌ DELETE PROJECT
def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    return redirect("home")


# ✏️ EDIT TASK
def edit_task(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "edit.html", {"form": form})


# ❌ DELETE TASK
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("home")
# ✏️ EDIT COMPANY
def edit_company(request, pk):
    company = Company.objects.get(id=pk)
    form = CompanyForm(request.POST or None, instance=company)

    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "edit.html", {"form": form})


# ❌ DELETE COMPANY
def delete_company(request, pk):
    company = Company.objects.get(id=pk)
    company.delete()
    return redirect("home")