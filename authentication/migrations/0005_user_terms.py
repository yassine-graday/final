# Generated by Django 3.1.6 on 2021-03-31 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20210331_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='terms',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]