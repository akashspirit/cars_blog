# Generated by Django 4.1.3 on 2022-12-21 06:26

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=cloudinary.models.CloudinaryField(default=2, max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]
