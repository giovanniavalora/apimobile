# Generated by Django 3.0.4 on 2020-05-01 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200430_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camion',
            name='color_camion',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='camion',
            name='numero_ejes',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]