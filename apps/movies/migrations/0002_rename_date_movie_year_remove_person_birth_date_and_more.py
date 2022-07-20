# Generated by Django 4.0.6 on 2022-07-20 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='date',
            new_name='year',
        ),
        migrations.RemoveField(
            model_name='person',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='person',
            name='death_date',
        ),
        migrations.AddField(
            model_name='person',
            name='birth_year',
            field=models.DateField(null=True, verbose_name='Birth Year'),
        ),
        migrations.AddField(
            model_name='person',
            name='death_year',
            field=models.DateField(null=True, verbose_name='Death Year'),
        ),
    ]