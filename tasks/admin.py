"""
Tasks application admin site

"""

from django.contrib import admin

from tasks.models import TaskModel


@admin.register(TaskModel)
class TaskModelAdmin(admin.ModelAdmin):
    """
    Tasks admin site configuration

    """

    list_display = ("summary", "get_reporter", "get_assignee")
    list_display_links = ("summary",)
    list_filter = ("reporter", "assignee")
    readonly_fields = ("uuid", )

    @admin.display(description="reported by")
    def get_reporter(self, obj):
        return obj.reporter

    @admin.display(description="assigned to")
    def get_assignee(self, obj):
        return obj.assignee
