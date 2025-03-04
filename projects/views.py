from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from . import models
from . import forms



class ProjectView(ListView):
    model = models.Project
    template_name = "project/projects_list.html"


class ProjectCreateView(CreateView):
    model = models.Project
    form_class = forms.ProjectModelForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('projects_list')

