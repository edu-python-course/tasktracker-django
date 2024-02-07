import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0003_populate_uuid_vals"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="taskmodel",
            name="id",
        ),
        migrations.AlterField(
            model_name="taskmodel",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                verbose_name="primary key"
            ),
        ),
    ]
