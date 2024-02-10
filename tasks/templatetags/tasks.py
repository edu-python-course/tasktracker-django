"""
Tasks application templatetags

"""

from typing import Any, Dict

from django import template

register = template.Library()


@register.filter(name="is_completed")
def is_completed(obj):
    # TODO: GH-77
    return "true" if obj["completed"] else "false"


@register.inclusion_tag("tasks/_task_tr.html", takes_context=True)
def task_row(context: Dict[str, Any], obj):
    # TODO: GH-78
    return {"object": obj}
