from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProjectView.as_view(), name='projects_list'),
    path('project/create', views.ProjectCreateView.as_view(), name='create_project'),
]