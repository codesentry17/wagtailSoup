# Generated by Django 4.2.6 on 2023-11-14 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0006_flexpage_supernova'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flexpage',
            name='superNova',
        ),
    ]
