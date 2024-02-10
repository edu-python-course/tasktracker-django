"""
Tasks application views

"""

from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render


def task_list_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to tasks list

    """

    return render(request, "task_list.html")


def task_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Handle requests to task details

    """

    return render(request, "task_detail.html")


def task_create_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to create a new task instance

    """

    return render(request, "task_form.html")


def task_update_view(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Handle requests to update an existing task instance

    """

    return render(request, "task_form.html")


def task_delete_view(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Handle requests to delete an existing task instance

    """

    return redirect("tasks:list")
