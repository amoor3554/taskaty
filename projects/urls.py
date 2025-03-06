from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='projects_list'),
    path('project/create', views.ProjectCreateView.as_view(), name='create_project'),
    path('project/update<int:pk>', views.ProjectUpdateView.as_view(), name='update_project'),
    path('project/delete<int:pk>', views.ProjectDeleteView.as_view(), name='delete_project'),
    path('task/create', views.TaskCreateView.as_view(), name='create_task'),
    path('task/update<int:pk>', views.TaskUpdateView.as_view(), name='update_task'),
    path('task/delete<int:pk>', views.TaskDeleteView.as_view(), name='delete_task'),




]