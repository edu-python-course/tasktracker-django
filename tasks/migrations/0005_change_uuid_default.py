import django.contrib.postgres.functions
from django.contrib.postgres.operations import CryptoExtension
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0004_change_pk_uuid"),
    ]

    operations = [
        # On PostgreSQL < 13, the pgcrypto extension must be installed.
        CryptoExtension(),
        migrations.AlterField(
            model_name="taskmodel",
            name="uuid",
            field=models.UUIDField(
                default=django.contrib.postgres.functions.RandomUUID(),
                editable=False,
                primary_key=True,
                serialize=False,
                verbose_name="primary key"
            ),
        ),
    ]
