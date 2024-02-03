from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0005_change_uuid_default"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="taskmodel",
            options={
                "ordering": ("-created_at", "-updated_at"),
                "verbose_name": "task",
                "verbose_name_plural": "tasks"
            },
        ),
        migrations.AlterModelTable(
            name="taskmodel",
            table="task",
        ),
    ]
