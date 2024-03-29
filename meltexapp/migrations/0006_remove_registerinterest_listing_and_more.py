# Generated by Django 4.1.2 on 2024-02-22 15:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meltexapp", "0005_remove_geography_parent_id_geography_parent"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="registerinterest",
            name="listing",
        ),
        migrations.AlterField(
            model_name="registerinterest",
            name="buyer_message_permissions",
            field=models.CharField(
                choices=[("user", "Private"), ("company", "Company")],
                default="company",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="registerinterest",
            name="seller_message_permissions",
            field=models.CharField(
                choices=[("user", "Private"), ("company", "Company")],
                default="company",
                max_length=30,
            ),
        ),
    ]
