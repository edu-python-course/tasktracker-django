from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="usermodel",
            name="image",
            field=models.ImageField(
                blank=True,
                default="avatars/default.svg",
                upload_to="avatars"
            ),
        ),
    ]
