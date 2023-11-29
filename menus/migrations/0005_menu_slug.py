# Generated by Django 4.2.6 on 2023-11-22 23:06

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0004_remove_menu_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='menu', editable=True, populate_from='title'),
            preserve_default=False,
        ),
    ]
