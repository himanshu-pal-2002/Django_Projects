# Generated by Django 4.2.2 on 2024-01-07 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=100)),
                ('texp', models.IntegerField()),
                ('School', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.school')),
            ],
        ),
    ]
