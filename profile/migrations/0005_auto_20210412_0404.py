# Generated by Django 3.1.6 on 2021-04-12 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0004_auto_20210412_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='staticfiles/assets/images/profiles/'),
        ),
    ]
