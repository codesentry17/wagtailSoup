# Generated by Django 4.2.6 on 2023-11-22 22:38

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0005_delete_advert'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
                ('text', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=True, populate_from='text')),
            ],
        ),
    ]