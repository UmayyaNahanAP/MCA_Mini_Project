# Generated by Django 5.1.1 on 2024-09-17 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchemApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schem_name', models.CharField(max_length=225)),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20)),
                ('house_name', models.CharField(max_length=255)),
                ('village', models.CharField(max_length=255)),
                ('panchayath', models.CharField(choices=[('Feroke', 'Feroke')], max_length=100)),
                ('district', models.CharField(choices=[('Kozhikode', 'Kozhikode')], max_length=100)),
                ('pincode', models.CharField(max_length=6)),
                ('contact_no', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('land_ownership', models.CharField(choices=[('own', 'own'), ('lease', 'lease')], max_length=50)),
                ('land_area', models.CharField(max_length=255)),
                ('survay_no', models.CharField(max_length=5)),
                ('benefinting', models.BooleanField(default=False)),
                ('bank_name', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=255)),
                ('account_no', models.CharField(max_length=19)),
                ('ifsc_code', models.CharField(max_length=11)),
                ('photo', models.ImageField(upload_to='documents/photo/')),
                ('sign', models.ImageField(upload_to='documents/sign/')),
                ('aadhar', models.ImageField(upload_to='documents/aadhar/')),
                ('land_tax', models.ImageField(upload_to='documents/land_tax/')),
                ('bank_pass', models.ImageField(upload_to='documents/bank_pass/')),
            ],
        ),
    ]
