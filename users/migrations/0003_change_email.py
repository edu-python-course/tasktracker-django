from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_check_emails"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermodel",
            name="email",
            field=models.EmailField(
                max_length=254,
                unique=True,
                verbose_name="email address"
            ),
        ),
    ]
