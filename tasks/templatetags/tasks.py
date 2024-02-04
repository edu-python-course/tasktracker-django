"""
Tasks application templatetags

"""

import datetime

from django import template
from django.utils import timezone

register = template.Library()


@register.filter(name="is_within_days")
def is_within_days(value: datetime.datetime, days: int) -> bool:
    """
    Check if passed datetime is within the specified number of days from
    current date

    """

    return timezone.now() - value <= datetime.timedelta(days=days)


@register.inclusion_tag("widgets/task_row.html", takes_context=True)
def task_row(context, obj) -> dict:
    return {"user": context["user"], "object": obj}
