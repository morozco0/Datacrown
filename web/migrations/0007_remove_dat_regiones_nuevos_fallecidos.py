# Generated by Django 2.2.4 on 2020-06-28 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_dat_regiones_total_muertosanterior'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dat_regiones',
            name='nuevos_fallecidos',
        ),
    ]
