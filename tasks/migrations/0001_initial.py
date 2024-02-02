import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TaskModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID"
                    )
                ),
                (
                    "summary",
                    models.CharField(max_length=128)
                ),
                (
                    "description",
                    models.TextField(blank=True)
                ),
                (
                    "completed",
                    models.BooleanField(default=False)
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True)
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True)
                ),
                (
                    "assignee",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="tasks_assigned",
                        to=settings.AUTH_USER_MODEL
                    )
                ),
                (
                    "reporter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="tasks_reported",
                        to=settings.AUTH_USER_MODEL
                    )
                ),
            ],
        ),
    ]
