# Generated by Django 5.1.2 on 2024-10-26 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vayal_user', '0002_alter_leaseland_land_lease_rent'),
    ]

    operations = [
        migrations.AddField(
            model_name='vayal_user',
            name='vegetable_permission_applied',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='leaseland',
            name='photo',
            field=models.ImageField(upload_to='photo/'),
        ),
    ]
