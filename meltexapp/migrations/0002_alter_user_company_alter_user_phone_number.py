# Generated by Django 4.1.2 on 2023-10-12 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meltexapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='meltexapp.company'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
    ]