from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Company
    path('edit-company/<int:pk>/', views.edit_company, name='edit_company'),
    path('delete-company/<int:pk>/', views.delete_company, name='delete_company'),

    # Project
    path('edit-project/<int:pk>/', views.edit_project, name='edit_project'),
    path('delete-project/<int:pk>/', views.delete_project, name='delete_project'),

    # Task
    path('edit-task/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete-task/<int:pk>/', views.delete_task, name='delete_task'),
]