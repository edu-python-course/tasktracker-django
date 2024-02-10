"""
Tasks application templatetags

"""

import datetime
from typing import Any, Dict

from django import template
from django.contrib.humanize.templatetags import humanize
from django.utils import timezone

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


@register.inclusion_tag("tasks/_task_tr.html", takes_context=True)
def task_row(context: Dict[str, Any], obj):
    # TODO: GH-78
    return {"object": obj}
