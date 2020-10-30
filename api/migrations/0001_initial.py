# Generated by Django 3.0.7 on 2020-10-30 13:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centro_de_coste', models.CharField(max_length=20, unique=True)),
                ('nombre_proyecto', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=100)),
                ('cliente', models.CharField(max_length=100)),
                ('rut_cliente', models.CharField(max_length=20)),
                ('mandante', models.CharField(max_length=100)),
                ('rut_mandante', models.CharField(max_length=20)),
                ('mandante_final', models.CharField(max_length=100)),
                ('cantidad_voucher_imprimir', models.IntegerField(blank=True, default=1)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_jornada', models.CharField(max_length=100)),
                ('hora_inicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('duracion', models.IntegerField(default=12)),
                ('available', models.BooleanField(default=True)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Proyecto')),
            ],
        ),
        migrations.AddConstraint(
            model_name='jornada',
            constraint=models.UniqueConstraint(fields=('proyecto', 'titulo_jornada'), name='Jrnd_proyecto_titulojornada'),
        ),
    ]
