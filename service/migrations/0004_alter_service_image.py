# Generated by Django 3.2.5 on 2022-08-18 21:27

from django.db import migrations, models
import service.models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_rename_sub_category_name_subcategory_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, default='static/img/logo2.png', null=True, upload_to=service.models.image_upload),
        ),
    ]