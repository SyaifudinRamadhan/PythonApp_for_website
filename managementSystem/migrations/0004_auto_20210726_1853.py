# Generated by Django 3.2.5 on 2021-07-26 11:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('managementSystem', '0003_auto_20210724_0722'),
    ]

    operations = [
        migrations.CreateModel(
            name='minTank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('levelMin', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='regression_eq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('M', models.FloatField()),
                ('C_and_Error', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='tankLevelNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
                ('level', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='energy_saver',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='water_prediction',
            name='current',
            field=models.FloatField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='energy_saver',
            name='powerMain',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='energy_saver',
            name='powerSun',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='water_prediction',
            name='volume_d',
            field=models.FloatField(),
        ),
    ]
