# Generated by Django 5.0.1 on 2024-01-20 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='username',
        ),
    ]