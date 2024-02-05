"""
Tasks application views

"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)

from tasks.forms import TaskModelForm
from tasks.models import TaskModel


class TaskListView(ListView):
    http_method_names = ["get"]
    model = TaskModel
    template_name = "tasks/task_list.html"


class TaskCreateView(LoginRequiredMixin, CreateView):
    http_method_names = ["get", "post"]
    model = TaskModel
    form_class = TaskModelForm
    template_name = "tasks/task_form.html"


class TaskDetailView(DetailView):
    http_method_names = ["get"]
    model = TaskModel
    template_name = "tasks/task_detail.html"


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    http_method_names = ["get", "post"]
    model = TaskModel
    form_class = TaskModelForm
    template_name = "tasks/task_form.html"


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    http_method_names = ["post"]
    model = TaskModel
    success_url = reverse_lazy("tasks:list")
