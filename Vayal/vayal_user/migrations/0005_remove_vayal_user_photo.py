# Generated by Django 5.1.2 on 2024-10-19 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vayal_user', '0004_alter_vayal_user_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vayal_user',
            name='photo',
        ),
    ]