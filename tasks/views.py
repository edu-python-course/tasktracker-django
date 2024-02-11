"""
Tasks application views

"""

import uuid

from django.contrib.auth.decorators import login_required
from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

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
def task_create_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to create a new task instance

    """

    return render(request, "tasks/task_form.html")


@login_required(login_url=reverse_lazy("users:sign-in"))
def task_update_view(request: HttpRequest, pk: uuid.UUID) -> HttpResponse:
    """
    Handle requests to update an existing task instance

    """

    get_object_or_404(TaskModel, pk=pk)

    return render(request, "tasks/task_form.html")


@login_required(login_url=reverse_lazy("users:sign-in"))
def task_delete_view(request: HttpRequest, pk: uuid.UUID) -> HttpResponse:
    """
    Handle requests to delete an existing task instance

    """

    get_object_or_404(TaskModel, pk=pk)

    return redirect("tasks:list")
