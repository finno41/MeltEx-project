# Generated by Django 4.1.2 on 2024-02-09 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("meltexapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="assetclass",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="assetclass",
            name="deleted_on",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="assetclass",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="assetclassinterest",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="assetclassinterest",
            name="deleted_on",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="assetclassinterest",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="company",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="company",
            name="deleted_on",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="company",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="geography",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="geography",
            name="deleted_on",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="geography",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="listing",
            name="sold",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="subassetclass",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subassetclass",
            name="deleted_on",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="subassetclass",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="tag",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="tag",
            name="deleted_on",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="tag",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="taginstance",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="taginstance",
            name="deleted_on",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="taginstance",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="listing",
            name="created_on",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="listing",
            name="geography",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="meltexapp.geography"
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="sub_asset_class",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="meltexapp.subassetclass",
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name="RegisterInterest",
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
                (
                    "buyer_message_permissions",
                    models.CharField(
                        choices=[("user", "Private"), ("company", "Company")],
                        default="user",
                        max_length=30,
                    ),
                ),
                (
                    "seller_message_permissions",
                    models.CharField(
                        choices=[("user", "Private"), ("company", "Company")],
                        default="user",
                        max_length=30,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("accepted", "Accepted"),
                            ("pending", "Pending"),
                            ("rejected", "Rejected"),
                        ],
                        default="pending",
                        max_length=30,
                    ),
                ),
                (
                    "buyer_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="buyer_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "listing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "seller_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="seller_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
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
