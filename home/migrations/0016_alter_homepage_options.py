# Generated by Django 5.0.8 on 2024-11-14 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0015_alter_homepage_body"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="homepage",
            options={"verbose_name": "Home Page", "verbose_name_plural": "Home Pages"},
        ),
    ]