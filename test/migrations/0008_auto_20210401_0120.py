# Generated by Django 3.1.6 on 2021-04-01 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0007_auto_20210401_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='elements',
            field=models.ManyToManyField(blank=True, null=True, related_name='tests', to='test.Element'),
        ),
    ]
