"""
Tasks application views

"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)

from tasks.forms import TaskModelForm
from tasks.models import TaskModel


def task_list_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to tasks list

    """

    ctx = {
        "object_list": TaskModel.objects.all(),
    }

    return render(request, "tasks/task_list.html", ctx)


class TaskDetailView(DetailView):
    """
    Used to provide details on the task instance

    """

    http_method_names = ["get"]
    model = TaskModel
    template_name = "tasks/task_detail.html"


class TaskCreateView(LoginRequiredMixin, CreateView):
    """
    Used to create a new task instance

    """

    http_method_names = ["get", "post"]
    model = TaskModel
    form_class = TaskModelForm
    template_name = "tasks/task_form.html"
    login_url = reverse_lazy("users:sign-in")

    def form_valid(self, form):
        form.instance.reporter = self.request.user

        return super().form_valid(form)

    # noinspection PyMethodMayBeStatic
    def get_cancel_url(self):
        return reverse_lazy("tasks:list")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["cancel_url"] = self.get_cancel_url()

        return ctx


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """
    Used to update the existing task instance

    """

    http_method_names = ["get", "post"]
    model = TaskModel
    form_class = TaskModelForm
    template_name = "tasks/task_form.html"
    login_url = reverse_lazy("users:sign-in")

    def get_cancel_url(self):
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["cancel_url"] = self.get_cancel_url()

        return ctx


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete task instance

    """

    http_method_names = ["post"]
    model = TaskModel
    success_url = reverse_lazy("tasks:list")
    login_url = reverse_lazy("users:sign-in")
