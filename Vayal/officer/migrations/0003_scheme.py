# Generated by Django 5.1.2 on 2024-10-27 19:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0002_agricultural_officer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('type', models.CharField(choices=[('Janakeeyasoothranam', 'Janakeeyasoothranam'), ('Department of agriculture', 'Department of agriculture')], max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('criteria', models.CharField(max_length=250)),
                ('cast_eligibility', models.CharField(choices=[('General', 'General'), ('OBC', 'OBC'), ('SC/ST', 'SC/ST')], default='All', max_length=50)),
                ('land_ownership', models.CharField(choices=[('Own', 'Own'), ('Lease', 'Lease')], default='All', max_length=20)),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('officer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officer.agricultural_officer')),
            ],
        ),
    ]
