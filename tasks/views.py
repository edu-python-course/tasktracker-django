"""
Tasks application views

"""

from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render

tasks = [
    {
        "pk": 1,
        "summary":
            "Shield at the holodeck was the energy of assimilation, "
            "lowered to a chemical c-beam.",
        "description":
            "The creature is more transformator now than starship. "
            "Solid and always quirky. Energy at the wormhole was "
            "the life of ellipse, grabbed to a mysterious proton. "
            "Adventure at the space station was the flight of honor, "
            "translated to a unrelated hurrah. Mermaids reproduce from "
            "pressures like sub-light humour's?",
        "assignee": {
            "image": "https://i.pravatar.cc/?u=DoraHeadstrong@dayrep.com",
            "first_name": "Dora",
            "last_name": "Headstrong",
        }
    },
    {
        "pk": 2,
        "summary":
            "Sensor at the universe was the pattern of love, "
            "empowered to a futile alien.",
        "description":
            "The nano machine is more admiral now than processor. "
            "Senior and patiently dead. Pattern at the center was "
            "the death of attitude, loved to a biological ship. "
            "Sensor at the space station was the assimilation of "
            "resistance, destroyed to an ancient crew. "
            "The collective admiral finally manifests the planet?",
        "assignee": {
            "image": "https://i.pravatar.cc/?u=TobyMugwort@armyspy.com",
            "first_name": "Toby",
            "last_name": "Mugwort",
        }
    },
]


def task_list_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to task list view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    ctx = {
        "object_list": tasks,
    }

    return render(request, "task_list.html", ctx)


def task_create_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to task create view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    return render(request, "task_form.html")


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

    for task in tasks:
        if task["pk"] == pk:
            break
    else:
        raise Http404

    ctx = {
        "object": task,
    }

    return render(request, "task_detail.html", ctx)


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

    for task in tasks:
        if task["pk"] == pk:
            break
    else:
        raise Http404

    ctx = {
        "object": task,
    }

    return render(request, "task_form.html", ctx)


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

    for task in tasks:
        if task["pk"] == pk:
            break
    else:
        raise Http404

    return redirect("tasks:list")
