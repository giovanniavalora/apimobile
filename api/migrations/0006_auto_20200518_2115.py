# Generated by Django 3.0.4 on 2020-05-19 01:15

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200506_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='camion',
            name='foto_camion',
            field=models.FileField(blank=True, upload_to=api.models.get_upload_path_camion),
        ),
        migrations.AlterField(
            model_name='camion',
            name='numero_ejes',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]