# Generated by Django 5.0.1 on 2024-06-16 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libs', '0012_question_function'),
    ]

    operations = [
        migrations.AddField(
            model_name='bench',
            name='system_template',
            field=models.TextField(blank=True, max_length=4096, null=True),
        ),
    ]
