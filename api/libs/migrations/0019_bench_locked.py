# Generated by Django 5.0.1 on 2024-07-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libs", "0018_evaluationtask_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="bench",
            name="locked",
            field=models.BooleanField(default=True),
        ),
    ]