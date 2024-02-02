import uuid

from django.db import migrations


def populate_uuid_values(apps, schema_editor):
    model = apps.get_model("tasks", "TaskModel")
    qs = model.objects.all()
    for task in qs:
        task.uuid = uuid.uuid4()
    model.objects.bulk_update(qs, ["uuid"])


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0002_add_uuid_field"),
    ]

    operations = [
        migrations.RunPython(populate_uuid_values, migrations.RunPython.noop),
    ]
