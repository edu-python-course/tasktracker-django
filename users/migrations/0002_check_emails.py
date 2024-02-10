"""
This migration will deactivate all users who have no email addresses,
or have duplicated email addresses.

"""

import uuid

from django.db import migrations
from django.db.models.aggregates import Count


def deactivate_users_without_emails(apps, schema_editor):
    model = apps.get_model("users", "UserModel")
    qs = model.objects.filter(email="")
    for counter, user in enumerate(qs, 1):
        user.is_active = False
        user.email = f"{uuid.uuid4()}@fake-email.com"
    model.objects.bulk_update(qs, ["email", "is_active"])


def deactivate_users_with_duplicated_emails(apps, schema_editor):
    model = apps.get_model("users", "UserModel")
    duplicates = model.objects.values(
        "email"
    ).annotate(
        email_seen=Count("email")
    ).filter(
        email_seen__gt=1
    )
    qs = model.objects.filter(email__in=duplicates.values("email"))
    for user in qs:
        user.is_active = False
        user.email = f"{uuid.uuid4()}@fake-email.com"
    model.objects.bulk_update(qs, ["email", "is_active"])


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            deactivate_users_with_duplicated_emails,
            migrations.RunPython.noop
        ),
        migrations.RunPython(
            deactivate_users_without_emails,
            migrations.RunPython.noop
        ),
    ]
