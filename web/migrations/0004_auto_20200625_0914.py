# Generated by Django 2.2.4 on 2020-06-25 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20200623_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='dat_regiones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=10)),
                ('total_contagiados', models.IntegerField()),
                ('total_fallecidos', models.IntegerField()),
                ('nuevos_contagios', models.IntegerField()),
                ('nuevos_fallecidos', models.IntegerField()),
                ('casos_activos', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Contagios',
        ),
    ]
