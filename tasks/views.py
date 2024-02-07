"""
Tasks application views

"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)

from tasks.forms import TaskModelForm
from tasks.mixins import IsNotAdminMixin
from tasks.models import TaskModel


class TaskListView(ListView):
    http_method_names = ["get"]
    model = TaskModel
    template_name = "tasks/task_list.html"
    paginate_by = 5


class TaskCreateView(LoginRequiredMixin, IsNotAdminMixin, CreateView):
    http_method_names = ["get", "post"]
    model = TaskModel
    form_class = TaskModelForm
    template_name = "tasks/task_form.html"
    login_url = reverse_lazy("users:sign-in")

    def form_valid(self, form):
        form.instance.reporter = self.request.user

        return super().form_valid(form)


class TaskDetailView(DetailView):
    http_method_names = ["get"]
    model = TaskModel
    template_name = "tasks/task_detail.html"


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    http_method_names = ["get", "post"]
    model = TaskModel
    form_class = TaskModelForm
    template_name = "tasks/task_form.html"
    login_url = reverse_lazy("users:sign-in")

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if not self.get_object().can_edit(request.user):
            raise PermissionDenied

        return super().get(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if not self.get_object().can_edit(request.user):
            raise PermissionDenied

        return super().post(request, *args, **kwargs)


class TaskDeleteView(DeleteView):
    http_method_names = ["post"]
    model = TaskModel
    success_url = reverse_lazy("tasks:list")

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if not self.get_object().can_delete(request.user):
            raise PermissionDenied

        return super().post(request, *args, **kwargs)
