# Generated by Django 5.0.8 on 2024-09-15 16:34

import modelcluster.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_category_options_alter_gallery_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallerydetailspage',
            name='gallery',
        ),
        migrations.AddField(
            model_name='gallerydetailspage',
            name='galleries',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='gallery_details_pages', to='home.gallery'),
        ),
    ]
