# Generated by Django 5.1.2 on 2024-10-27 19:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vayal_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20)),
                ('phone_number', models.CharField(max_length=10)),
                ('aadhar_number', models.CharField(max_length=12)),
                ('cast', models.CharField(choices=[('General', 'General'), ('OBC', 'OBC'), ('SC/ST', 'SC/ST')], max_length=20)),
                ('house_name', models.CharField(max_length=225)),
                ('place', models.CharField(max_length=225)),
                ('village', models.CharField(max_length=225)),
                ('pincode', models.CharField(max_length=6)),
                ('muncipality', models.CharField(default='Kozhikode', max_length=225)),
                ('district', models.CharField(default='Kozhikode', max_length=225)),
                ('land_ownership', models.CharField(choices=[('Own', 'Own'), ('Lease', 'Lease')], max_length=20)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
                ('vegetable_permission_applied', models.CharField(default='False', max_length=225)),
                ('vegetable_permission', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=225)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
