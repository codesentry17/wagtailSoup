# Generated by Django 4.2.6 on 2023-11-22 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0003_advert'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advert',
            name='text',
        ),
        migrations.RemoveField(
            model_name='advert',
            name='url',
        ),
    ]
