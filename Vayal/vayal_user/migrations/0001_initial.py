# Generated by Django 5.1.2 on 2024-10-19 02:00

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
                ('cast', models.CharField(choices=[('General', 'General'), ('OBC', 'OBC'), ('OEC', 'OEC')], max_length=20)),
                ('house_name', models.CharField(max_length=225)),
                ('place', models.CharField(max_length=225)),
                ('village', models.CharField(max_length=225)),
                ('pincode', models.CharField(max_length=6)),
                ('muncipality', models.CharField(default='Kozhikode', max_length=225)),
                ('district', models.CharField(default='Kozhikode', max_length=225)),
                ('land_ownership', models.CharField(choices=[('Own', 'Own'), ('Lease', 'Lease')], max_length=20)),
                ('photo', models.ImageField(upload_to='documents/photo/')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]