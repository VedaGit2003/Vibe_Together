# Generated by Django 4.1.7 on 2024-01-06 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(default="", max_length=8, unique=True)),
                ("host", models.CharField(max_length=50, unique=True)),
                ("guest_can_wait", models.BooleanField(default=False)),
                ("votes_to_skip", models.IntegerField(default=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
