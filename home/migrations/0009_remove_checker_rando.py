# Generated by Django 4.2.6 on 2023-10-31 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_checker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checker',
            name='rando',
        ),
    ]