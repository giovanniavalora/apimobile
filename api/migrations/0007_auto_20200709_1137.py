# Generated by Django 3.0.7 on 2020-07-09 15:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200518_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='id_qr',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
