# Generated by Django 5.1.2 on 2024-10-19 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vayal_user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vayal_user',
            name='photo',
        ),
    ]
