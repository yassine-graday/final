# Generated by Django 3.1.6 on 2021-05-09 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultat', '0007_auto_20210507_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultat',
            name='imagePdf',
            field=models.FileField(blank=True, default='settings.MEDIA_ROOT/test1.pdf', null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
