# Generated by Django 4.2.2 on 2023-12-20 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Designation', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Company_Name', models.CharField(max_length=40)),
            ],
        ),
    ]
