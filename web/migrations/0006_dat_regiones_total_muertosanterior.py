# Generated by Django 2.2.4 on 2020-06-27 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20200627_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='dat_regiones',
            name='total_muertosanterior',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]