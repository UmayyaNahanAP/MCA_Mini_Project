# Generated by Django 5.1.2 on 2024-10-25 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vayal_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaseland',
            name='land_lease_rent',
            field=models.IntegerField(),
        ),
    ]