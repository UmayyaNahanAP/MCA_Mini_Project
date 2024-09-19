# Generated by Django 5.1.1 on 2024-09-19 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0002_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('dob', models.DateField()),
                ('genter', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20)),
                ('phone_number', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=225, unique=True)),
                ('password', models.CharField(max_length=8)),
                ('conform_password', models.CharField(max_length=8)),
            ],
        ),
    ]
