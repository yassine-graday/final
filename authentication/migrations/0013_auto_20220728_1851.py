# Generated by Django 3.1.6 on 2022-07-28 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_auto_20220725_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True, unique=True),
        ),
    ]
