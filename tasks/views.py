"""
Tasks application views

"""

from django.http.request import HttpRequest
from django.http.response import HttpResponse


def task_list_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to tasks list

    """

    return HttpResponse("tasks")


def task_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Handle requests to task details

    """

    return HttpResponse("tasks")


def task_create_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to create a new task instance

    """

    return HttpResponse("tasks")


def task_update_view(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Handle requests to update an existing task instance

    """

    return HttpResponse("tasks")


def task_delete_view(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Handle requests to delete an existing task instance

    """

    return HttpResponse("tasks")
