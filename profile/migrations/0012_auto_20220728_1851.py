# Generated by Django 3.1.6 on 2022-07-28 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0011_auto_20210616_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, max_length=512, null=True, upload_to='staticfiles/assets/images/profile/'),
        ),
    ]
