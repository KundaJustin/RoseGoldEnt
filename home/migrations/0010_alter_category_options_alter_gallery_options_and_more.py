# Generated by Django 5.0.8 on 2024-09-15 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_category_alter_homepage_body_gallery_category'),
        ('wagtailcore', '0094_alter_page_locale'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'ordering': ['-date'], 'verbose_name': 'Gallery', 'verbose_name_plural': 'Galleries'},
        ),
        migrations.CreateModel(
            name='GalleryDetailsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('gallery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='detail_pages', to='home.gallery')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]