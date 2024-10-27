# Generated by Django 5.1.2 on 2024-10-27 20:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0004_schemeapplication'),
    ]

    operations = [
        migrations.CreateModel(
            name='VegetablePermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farm_name', models.CharField(max_length=250)),
                ('farm_place', models.CharField(max_length=250)),
                ('total_land_area', models.CharField(max_length=255)),
                ('land_survay_no', models.CharField(max_length=5)),
                ('sign', models.ImageField(upload_to='vegetable_permission/sign/')),
                ('aadhar', models.FileField(upload_to='vegetable_permission/aadhar/')),
                ('land_tax', models.FileField(upload_to='vegetable_permission/land_tax/')),
                ('applied_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=50)),
                ('officer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officer.agricultural_officer')),
                ('vayal_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officer.vayal_user')),
            ],
        ),
    ]
