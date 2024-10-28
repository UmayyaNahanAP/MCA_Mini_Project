# Generated by Django 5.1.2 on 2024-10-27 21:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0010_leaseland'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schemeapplication',
            name='officer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='officer.agricultural_officer'),
        ),
        migrations.AlterField(
            model_name='vegetablepermission',
            name='officer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='officer.agricultural_officer'),
        ),
    ]