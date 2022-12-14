# Generated by Django 3.1.6 on 2021-02-21 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resultat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resultat',
            options={'ordering': ['id'], 'verbose_name_plural': 'resultats'},
        ),
        migrations.RemoveField(
            model_name='resultat',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='resultat',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='resultat',
            name='creatif',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultat',
            name='entreprenant',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultat',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='resultat',
            name='investigateur',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultat',
            name='methodique',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultat',
            name='metier1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultat',
            name='metier10',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultat',
            name='metier11',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultat',
            name='metier12',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultat',
            name='metier13',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultat',
            name='metier14',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultat',
            name='metier2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultat',
            name='metier3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultat',
            name='metier4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultat',
            name='metier5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultat',
            name='metier6',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultat',
            name='metier7',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultat',
            name='metier8',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultat',
            name='metier9',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultat',
            name='pratique',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultat',
            name='social',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resultat',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='ResulatMetier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('pourcentage', models.FloatField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('resultat_metier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resultatmetiers', to='resultat.resultat')),
            ],
            options={
                'verbose_name_plural': 'Metiers',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ResulataPersona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('pourcentage', models.FloatField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('resultat_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resultatpersonna', to='resultat.resultat')),
            ],
            options={
                'verbose_name_plural': 'Personna',
                'ordering': ['id'],
            },
        ),
    ]
