from django.db.models.query import QuerySet
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms



class ProjectListView(LoginRequiredMixin ,ListView):
    model = models.Project
    template_name = "projects_list.html"
    paginate_by = 6

    def get_queryset(self):
        query_set = super().get_queryset()
        where = {}
        q = self.request.GET.get('q', None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)
    


class ProjectCreateView(LoginRequiredMixin ,CreateView):
    model = models.Project
    form_class = forms.ProjectModelForm
    template_name = 'create.html'
    success_url = reverse_lazy('projects_list')

class ProjectUpdateView(LoginRequiredMixin ,UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = 'update.html'
    success_url = reverse_lazy('projects_list')

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('update_project', args=[self.object.id])
    
class ProjectDeleteView(LoginRequiredMixin ,DeleteView):
    model = models.Project
    template_name = 'delete.html'
    success_url = reverse_lazy('projects_list')



class TaskCreateView(LoginRequiredMixin ,CreateView):
    model = models.Task
    fields = ['project', 'description']
    http_method_names = ['post']

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('update_project', args=[self.object.project.id])
    
class TaskUpdateView(LoginRequiredMixin ,UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = ['post']

    success_url = reverse_lazy('projects_list')

class TaskDeleteView(LoginRequiredMixin ,DeleteView):
    model = models.Task

   
    def get_success_url(self):
        return reverse('update_project', args=[self.get_object().project.id])


