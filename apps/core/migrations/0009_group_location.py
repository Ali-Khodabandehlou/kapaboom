# Generated by Django 4.1.4 on 2022-12-22 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_resource_maplocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.maplocation'),
        ),
    ]
