# Generated by Django 4.2.6 on 2023-11-01 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_delete_checker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ad/%Y/%m/%d/')),
                ('title', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('days_open', models.CharField(max_length=50)),
                ('google_maps_link', models.URLField()),
                ('nice', models.CharField(max_length=100)),
            ],
        ),
    ]
