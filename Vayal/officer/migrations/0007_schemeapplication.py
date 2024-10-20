# Generated by Django 5.1.2 on 2024-10-19 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0006_scheme'),
        ('vayal_user', '0005_remove_vayal_user_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchemeApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benefiting', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50)),
                ('house_number', models.CharField(max_length=250)),
                ('ward_number', models.CharField(max_length=250)),
                ('total_land_area', models.CharField(max_length=255)),
                ('land_survay_no', models.CharField(max_length=5)),
                ('bank_name', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=255)),
                ('account_no', models.CharField(max_length=19)),
                ('photo', models.ImageField(upload_to='documents/photo/')),
                ('sign', models.ImageField(upload_to='documents/sign/')),
                ('aadhar', models.ImageField(upload_to='documents/aadhar/')),
                ('land_tax', models.ImageField(upload_to='documents/land_tax/')),
                ('bank_pass', models.ImageField(upload_to='documents/bank_pass/')),
                ('scheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officer.scheme')),
                ('vayal_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vayal_user.vayal_user')),
            ],
        ),
    ]