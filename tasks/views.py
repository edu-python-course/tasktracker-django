"""
Tasks application views

"""

from django.http import HttpRequest, HttpResponse


def task_list_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to task list view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    return HttpResponse(b"task list view")


def task_create_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to task create view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    return HttpResponse(b"task create view")


def task_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Handle requests to task detail view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`
    :param pk: task primary key
    :type pk: int

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    return HttpResponse(b"task detail view: %d" % pk)


def task_update_view(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Handle requests to task update view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`
    :param pk: task primary key
    :type pk: int

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    return HttpResponse(b"task update view: %d" % pk)


def task_delete_view(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Handle requests to task delete view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`
    :param pk: task primary key
    :type pk: int

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    return HttpResponse(b"task delete view: %d" % pk)
