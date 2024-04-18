# Generated by Django 4.1.2 on 2024-03-15 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("meltexapp", "0008_geography_key_delete_message"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("deleted_on", models.DateTimeField(blank=True, null=True)),
                ("message", models.TextField(max_length=1000)),
                ("read", models.BooleanField(default=False)),
                (
                    "register_interest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="meltexapp.registerinterest",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
