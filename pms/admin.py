from django.contrib import admin
from .models import Project, Task


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by')


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'project', 'status', 'assigned_to')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)