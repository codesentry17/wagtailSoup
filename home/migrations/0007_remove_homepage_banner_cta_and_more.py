# Generated by Django 4.2.6 on 2023-10-31 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_homepage_banner_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='banner_cta',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='banner_image',
        ),
    ]
