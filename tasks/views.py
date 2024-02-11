"""
Tasks application views

"""

import uuid

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import (
    DeleteView,
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


def task_detail_view(request: HttpRequest, pk: uuid.UUID) -> HttpResponse:
    """
    Handle requests to task details

    """

    try:
        task = TaskModel.objects.get(pk=pk)
    except TaskModel.DoesNotExist:
        raise Http404

    ctx = {
        "object": task,
    }

    return render(request, "tasks/task_detail.html", ctx)


@login_required(login_url=reverse_lazy("users:sign-in"))
@require_http_methods(["GET", "POST"])
def task_create_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to create a new task instance

    """

    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.instance.reporter = request.user
            form.save()

            return redirect(form.instance.get_absolute_url())

    else:
        form = TaskModelForm()

    return render(request, "tasks/task_form.html", {"form": form})


@login_required(login_url=reverse_lazy("users:sign-in"))
@require_http_methods(["GET", "POST"])
def task_update_view(request: HttpRequest, pk: uuid.UUID) -> HttpResponse:
    """
    Handle requests to update an existing task instance

    """

    instance = get_object_or_404(TaskModel, pk=pk)
    if request.method == "POST":
        form = TaskModelForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()

            return redirect(form.instance.get_absolute_url())

    else:
        form = TaskModelForm(instance=instance)

    return render(request, "tasks/task_form.html", {"form": form})


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete task instance

    """

    http_method_names = ["post"]
    model = TaskModel
    success_url = reverse_lazy("tasks:list")
    login_url = reverse_lazy("users:sign-in")
