"""
Tasks application views

"""

import uuid

from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from tasks.models import TaskModel


def task_list_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to task list view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    ctx = {
        "object_list": TaskModel.objects.all(),
    }

    return render(request, "tasks/task_list.html", ctx)


def task_create_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to task create view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    return render(request, "tasks/task_form.html")


def task_detail_view(request: HttpRequest, pk: uuid.UUID) -> HttpResponse:
    """
    Handle requests to task detail view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`
    :param pk: task primary key
    :type pk: :class: `uuid.UUID`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    :raise: Http404

    """

    # DoesNotExist exception usage example
    try:
        task = TaskModel.objects.get(pk=pk)
        ctx = {"object": task}
    except TaskModel.DoesNotExist:
        raise Http404

    return render(request, "tasks/task_detail.html", ctx)


def task_update_view(request: HttpRequest, pk: uuid.UUID) -> HttpResponse:
    """
    Handle requests to task update view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`
    :param pk: task primary key
    :type pk: :class: `uuid.UUID`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    :raise: Http404

    """

    ctx = {"object": get_object_or_404(TaskModel, pk=pk)}

    return render(request, "tasks/task_form.html", ctx)


def task_delete_view(request: HttpRequest, pk: uuid.UUID) -> HttpResponse:
    """
    Handle requests to task delete view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`
    :param pk: task primary key
    :type pk: :class: `uuid.UUID`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    :raise: Http404

    """

    get_object_or_404(TaskModel, pk=pk)

    return redirect("tasks:list")
