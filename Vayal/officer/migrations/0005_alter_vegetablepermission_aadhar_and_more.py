# Generated by Django 5.1.2 on 2024-10-27 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0004_vegetablepermission_aadhar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vegetablepermission',
            name='aadhar',
            field=models.FileField(upload_to='vegetable_permission/aadhar/'),
        ),
        migrations.AlterField(
            model_name='vegetablepermission',
            name='land_tax',
            field=models.FileField(upload_to='land_tax/'),
        ),
    ]
