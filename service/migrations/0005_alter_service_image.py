# Generated by Django 3.2.5 on 2022-08-19 15:35

from django.db import migrations, models
import service.models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_alter_service_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, default='services/logo2.png', null=True, upload_to=service.models.image_upload),
        ),
    ]
