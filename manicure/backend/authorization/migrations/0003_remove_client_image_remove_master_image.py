# Generated by Django 5.0.3 on 2024-05-23 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0002_customuser_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='image',
        ),
        migrations.RemoveField(
            model_name='master',
            name='image',
        ),
    ]
