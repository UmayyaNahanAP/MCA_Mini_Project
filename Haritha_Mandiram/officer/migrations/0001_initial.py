# Generated by Django 5.1.1 on 2024-09-23 15:04

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
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('published', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Schem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('type', models.CharField(choices=[('Janakeeyasoothranam', 'Janakeeyasoothranam'), ('Department of agriculture', 'Department of agriculture')], max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('criteria', models.CharField(max_length=250)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Vegitable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('expiry', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VegitableForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_applicant', models.CharField(max_length=225)),
                ('dob', models.DateField()),
                ('genter', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=225)),
                ('farm_name', models.CharField(max_length=225)),
                ('location_of_farm', models.URLField(max_length=250)),
                ('photo', models.ImageField(upload_to='vegitable_form/photo/')),
                ('sign', models.ImageField(upload_to='vegitable_form/sign/')),
                ('declaration', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HM_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('dob', models.DateField()),
                ('genter', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20)),
                ('phone_number', models.CharField(max_length=10)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved'), ('Unresolvable', 'Unresolvable')], default='Pending', max_length=50)),
                ('hm_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officer.hm_user')),
            ],
        ),
    ]
