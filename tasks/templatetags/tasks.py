"""
Tasks application templatetags

"""

import datetime
from typing import Any, Dict

from django import template
from django.contrib.humanize.templatetags import humanize
from django.utils import timezone

from tasks.models import TaskModel

register = template.Library()


@register.filter(name="row_completed_mark")
def get_row_completed_mark(completed: bool) -> str:
    """
    Return row completed marker based on instance completed status value

    :param completed: task instance completed status
    :type completed: bool

    :return: rom completed marker
    :rtype: str

    """
    if completed:
        return "data-task-completed=true"

    return "data-task-completed=false"


@register.filter(name="is_within_days")
def get_task_humanize_timestamp(value: datetime.datetime, days: int = 7) -> str:
    """
    Return human-readable timestamp

    :param value: timestamp
    :type value: :class: `datetime.datetime`
    :param days: number of days in threshold, defaults to 7
    :type days: int

    :return: human-readable timestamp, transformed with humanize app
    :rtype: str

    If given timestamp is within days from current time range, it will
    be transformed using ``naturaltime`` filter. Otherwise, ``naturalday``
    filter will be used.

    """

    if not timezone.is_aware(value):
        # make sure ``value`` is timezone-aware
        value = timezone.make_aware(value, timezone.get_current_timezone())

    if timezone.now() - value <= datetime.timedelta(days=days):
        return humanize.naturaltime(value)

    return humanize.naturalday(value)


def get_context(context, obj: TaskModel) -> Dict[str, Any]:
    user = context["user"]
    can_delete = "disabled" if not obj.has_delete_permission(user) else ""
    can_update = "disabled" if not obj.has_update_permission(user) else ""

    return {
        "object": obj,
        "update_permission": can_update,
        "delete_permission": can_delete,
    }


@register.inclusion_tag("tasks/_task_tr.html", takes_context=True)
def task_row(context: Dict[str, Any], obj: TaskModel) -> Dict[str, Any]:
    return get_context(context, obj)


@register.inclusion_tag("tasks/_actions.html", takes_context=True)
def detail_actions(context: Dict[str, Any], obj: TaskModel) -> Dict[str, Any]:
    return get_context(context, obj)
