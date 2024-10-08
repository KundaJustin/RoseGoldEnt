# Generated by Django 5.0.8 on 2024-08-11 15:18

import modelcluster.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_gallery'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='image',
        ),
        migrations.AddField(
            model_name='gallery',
            name='images',
            field=modelcluster.fields.ParentalManyToManyField(related_name='gallery_images', to='wagtailimages.image'),
        ),
    ]
