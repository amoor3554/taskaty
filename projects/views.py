from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from . import models
from . import forms



class ProjectListView(ListView):
    model = models.Project
    template_name = "projects_list.html"


class ProjectCreateView(CreateView):
    model = models.Project
    form_class = forms.ProjectModelForm
    template_name = 'create.html'
    success_url = reverse_lazy('projects_list')

class ProjectUpdateView(UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = 'update.html'
    success_url = reverse_lazy('projects_list')

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('update_project', args=[self.object.id])
    
class ProjectDeleteView(DeleteView):
    model = models.Project
    template_name = 'delete.html'
    success_url = reverse_lazy('projects_list')



class TaskCreateView(CreateView):
    model = models.Task
    fields = ['project', 'description']
    http_method_names = ['post']

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('update_project', args=[self.object.project.id])
    
class TaskUpdateView(UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = ['post']

    success_url = reverse_lazy('projects_list')

class TaskDeleteView(DeleteView):
    model = models.Task

   
    def get_success_url(self):
        return reverse('update_project', args=[self.get_object().project.id])


