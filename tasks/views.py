"""
Tasks application views

"""

from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render

# TODO: blocker GH-62, GH-63
from tasks import _fake_db


def task_list_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to tasks list

    """

    ctx = {
        "object_list": _fake_db.tasks,
    }

    return render(request, "tasks/task_list.html", ctx)


def task_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Handle requests to task details

    """

    task = _fake_db.get_task(pk)
    if task is None:
        raise Http404

    ctx = {
        "object": task,
    }

    return render(request, "tasks/task_detail.html", ctx)


def task_create_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to create a new task instance

    """

    return render(request, "tasks/task_form.html")


def task_update_view(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Handle requests to update an existing task instance

    """

    task = _fake_db.get_task(pk)
    if task is None:
        raise Http404

    return render(request, "tasks/task_form.html")


def task_delete_view(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Handle requests to delete an existing task instance

    """

    task = _fake_db.get_task(pk)
    if task is None:
        raise Http404

    return redirect("tasks:list")
