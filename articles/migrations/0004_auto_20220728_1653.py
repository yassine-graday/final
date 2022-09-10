# Generated by Django 3.1.6 on 2022-07-28 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20220728_1647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='body',
            new_name='content',
        ),
        migrations.AddField(
            model_name='article',
            name='deadline',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='link',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='ville',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]