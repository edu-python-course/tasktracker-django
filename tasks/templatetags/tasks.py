"""
Tasks application templatetags

"""

import datetime
from typing import Any, Dict

from django import template
from django.contrib.humanize.templatetags import humanize
from django.utils import timezone

register = template.Library()


@register.filter(name="is_completed")
def is_completed(obj):
    # TODO: GH-77
    return "true" if obj["completed"] else "false"


@register.filter(name="task_timestamp")
def get_task_timestamp(value: datetime.datetime, days: int = 7) -> str:
    # TODO: GH-77
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
