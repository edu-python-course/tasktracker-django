from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_add_task_model"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="taskmodel",
            options={
                "ordering": (
                    "-updated_at",
                    "-created_at"
                ), "verbose_name": "task",
                "verbose_name_plural": "tasks"
            },
        ),
        migrations.AlterModelTable(
            name="taskmodel",
            table="task",
        ),
    ]
