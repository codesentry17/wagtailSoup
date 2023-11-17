# Generated by Django 4.2.6 on 2023-11-05 13:57

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=True, populate_from=models.CharField(max_length=100)),
        ),
    ]
