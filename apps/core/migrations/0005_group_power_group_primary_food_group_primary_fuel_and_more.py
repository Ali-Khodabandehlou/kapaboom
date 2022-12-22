# Generated by Django 4.1.4 on 2022-12-22 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='power',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='group',
            name='primary_food',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='group',
            name='primary_fuel',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='group',
            name='primary_water',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='group',
            name='reputation',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='group',
            name='secondary_copper',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='group',
            name='secondary_diamond',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='group',
            name='secondary_gold',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='group',
            name='secondary_iron',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='group',
            name='wealth',
            field=models.IntegerField(default=0),
        ),
    ]
