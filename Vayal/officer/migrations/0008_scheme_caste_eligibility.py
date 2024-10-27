# Generated by Django 5.1.2 on 2024-10-27 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0007_remove_notification_published_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheme',
            name='caste_eligibility',
            field=models.CharField(choices=[('All', 'All'), ('General', 'General'), ('OBC', 'OBC'), ('SC/ST', 'SC/ST')], default='All', max_length=50),
        ),
    ]
