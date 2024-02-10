"""
Tasks application admin site

"""

from typing import Union

from django.contrib import admin

from tasks.models import TaskModel


@admin.register(TaskModel)
class TaskModelAdmin(admin.ModelAdmin):
    """
    Task model administration

    """

    list_display = ("summary", "completed", "get_reporter", "get_assignee")
    list_display_links = ("summary",)
    list_filter = ("reporter", "assignee", "completed")
    readonly_fields = ("uuid",)
    list_per_page = 20

    @admin.display(description="assigned to")
    def get_assignee(self, obj: TaskModel) -> Union[str, None]:
        if obj.assignee is None:
            return

        return obj.assignee.get_full_name() or obj.assignee.username

    @admin.display(description="reported by")
    def get_reporter(self, obj: TaskModel) -> str:
        return obj.reporter.get_full_name() or obj.reporter.username
