# Generated by Django 4.2.6 on 2023-11-22 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0004_remove_advert_text_remove_advert_url'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Advert',
        ),
    ]