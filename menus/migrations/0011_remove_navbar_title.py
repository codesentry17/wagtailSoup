# Generated by Django 4.2.6 on 2023-12-01 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0010_navbar_navitem_pagelist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navbar',
            name='title',
        ),
    ]
