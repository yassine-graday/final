# Generated by Django 3.1.6 on 2021-03-30 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='team',
        ),
        migrations.AddField(
            model_name='profile',
            name='branch',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='firstName',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastName',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='pdfResult',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='school',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='tel',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
