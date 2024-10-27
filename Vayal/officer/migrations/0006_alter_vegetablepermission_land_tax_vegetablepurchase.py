# Generated by Django 5.1.2 on 2024-10-27 05:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0005_alter_vegetablepermission_aadhar_and_more'),
        ('vayal_user', '0004_alter_vayal_user_vegetable_permission_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vegetablepermission',
            name='land_tax',
            field=models.FileField(upload_to='vegetable_permission/land_tax/'),
        ),
        migrations.CreateModel(
            name='VegetablePurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('token_number', models.CharField(max_length=100, unique=True)),
                ('vayal_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vayal_user.vayal_user')),
                ('vegetable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officer.vegetable')),
            ],
        ),
    ]