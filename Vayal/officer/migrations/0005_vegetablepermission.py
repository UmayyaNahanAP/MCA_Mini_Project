# Generated by Django 5.1.1 on 2024-10-17 13:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0004_complaint'),
        ('vayal_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VegetablePermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vegetable_names', models.JSONField()),
                ('farm_name', models.CharField(max_length=250)),
                ('farm_address', models.CharField(max_length=250)),
                ('applied_date', models.DateTimeField(auto_now_add=True)),
                ('vayal_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vayal_user.vayal_user')),
            ],
        ),
    ]
