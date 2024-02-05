"""
Tasks application views

"""

import uuid

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from tasks.forms import TaskModelForm
from tasks.models import TaskModel

TASKS_PER_PAGE = 10


def task_list_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to task list view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    qs = TaskModel.objects.all()
    paginator = Paginator(qs, TASKS_PER_PAGE)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)

    ctx = {
        "object_list": page.object_list,
        "is_paginated": True,
        "page_obj": page,
    }

    return render(request, "tasks/task_list.html", ctx)


@login_required
@require_http_methods(["GET", "POST"])
def task_create_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to task create view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

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


@login_required
@require_http_methods(["GET", "POST"])
def task_update_view(request: HttpRequest, pk: uuid.UUID) -> HttpResponse:
    """
    Handle requests to task update view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`
    :param pk: task primary key
    :type pk: :class: `uuid.UUID`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    :raise: Http404, PermissionDenied

    """

    instance = get_object_or_404(TaskModel, pk=pk)
    if request.user != instance.reporter and request.user != instance.assignee:
        raise PermissionDenied

    if request.method == "POST":
        form = TaskModelForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()

            return redirect(form.instance.get_absolute_url())

    else:
        form = TaskModelForm(instance=instance)

    return render(request, "tasks/task_form.html", {"form": form})


@require_http_methods(["POST"])
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

    instance = get_object_or_404(TaskModel, pk=pk)
    if request.user != instance.reporter:
        raise PermissionDenied

    instance.delete()

    return redirect("tasks:list")
