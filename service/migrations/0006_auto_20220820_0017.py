# Generated by Django 3.2.5 on 2022-08-19 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_alter_service_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='service_city',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service_country',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service_region',
        ),
    ]