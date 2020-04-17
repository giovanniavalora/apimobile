# Generated by Django 3.0.4 on 2020-04-17 20:37

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('rut', models.CharField(max_length=15, unique=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', api.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Camion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente_camion', models.CharField(max_length=20)),
                ('marca_camion', models.CharField(max_length=20)),
                ('modelo_camion', models.CharField(max_length=20)),
                ('capacidad_camion', models.CharField(max_length=20)),
                ('nombre_conductor_principal', models.CharField(max_length=50)),
                ('apellido_conductor_principal', models.CharField(max_length=50)),
                ('telefono_conductor_principal', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=20)),
                ('numero_ejes', models.CharField(max_length=5)),
                ('unidad_medida', models.CharField(choices=[('m3', 'm3'), ('ton', 'ton')], max_length=5)),
                ('color_camion', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Camiones',
            },
        ),
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_destino', models.CharField(max_length=100)),
                ('nombre_propietario', models.CharField(max_length=100)),
                ('rut_propietario', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=100)),
                ('longitud', models.CharField(max_length=20)),
                ('latitud', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Origen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_origen', models.CharField(max_length=100)),
                ('longitud', models.CharField(max_length=20)),
                ('latitud', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Origenes',
            },
        ),
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
            ],
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email', models.CharField(max_length=100)),
                ('cargo', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Administradores',
            },
            bases=('api.user', models.Model),
            managers=[
                ('objects', api.models.AdminManager()),
            ],
        ),
        migrations.CreateModel(
            name='Despachador',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('telefono', models.CharField(blank=True, max_length=30)),
                ('origen_asignado', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Despachadores',
            },
            bases=('api.user', models.Model),
            managers=[
                ('objects', api.models.DespManager()),
            ],
        ),
        migrations.CreateModel(
            name='Suborigen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_suborigen', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Origen')),
            ],
            options={
                'verbose_name_plural': 'Sub-Origenes',
            },
        ),
        migrations.CreateModel(
            name='Subcontratista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=20)),
                ('razon_social', models.CharField(max_length=100)),
                ('nombre_subcontratista', models.CharField(max_length=100)),
                ('nombre_contacto', models.CharField(max_length=50)),
                ('apellido_contacto', models.CharField(max_length=50)),
                ('email_contacto', models.CharField(blank=True, default='', max_length=100)),
                ('telefono_contacto', models.CharField(max_length=20)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Proyecto')),
            ],
        ),
        migrations.AddField(
            model_name='origen',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Proyecto'),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=100)),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Destino')),
            ],
            options={
                'verbose_name_plural': 'Materiales',
            },
        ),
        migrations.AddField(
            model_name='destino',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Proyecto'),
        ),
        migrations.CreateModel(
            name='CodigoQR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField()),
                ('camion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Camion')),
            ],
            options={
                'verbose_name_plural': 'Codigos QR',
            },
        ),
        migrations.AddField(
            model_name='camion',
            name='subcontratista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Subcontratista'),
        ),
        migrations.AddField(
            model_name='user',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Proyecto'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proyecto', models.CharField(max_length=100)),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('rut_cliente', models.CharField(max_length=20)),
                ('nombre_subcontratista', models.CharField(max_length=100)),
                ('rut_subcontratista', models.CharField(max_length=20)),
                ('nombre_conductor_principal', models.CharField(max_length=50)),
                ('apellido_conductor_principal', models.CharField(max_length=50)),
                ('fecha_servidor', models.DateField(auto_now_add=True)),
                ('hora_servidor', models.TimeField(auto_now_add=True)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('patente', models.CharField(max_length=20)),
                ('foto_patente', models.FileField(upload_to=api.models.get_upload_path_patente)),
                ('volumen', models.CharField(max_length=20)),
                ('tipo_material', models.CharField(max_length=50)),
                ('punto_origen', models.CharField(max_length=100)),
                ('punto_suborigen', models.CharField(blank=True, max_length=100)),
                ('punto_destino', models.CharField(max_length=100)),
                ('contador_impresiones', models.IntegerField()),
                ('despachador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Despachador')),
            ],
        ),
        migrations.CreateModel(
            name='OrigenTemporal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_origen', models.IntegerField()),
                ('timestamp_inicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('duracion', models.IntegerField(default=12)),
                ('activo', models.BooleanField(default=True)),
                ('despachador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Despachador')),
            ],
            options={
                'verbose_name_plural': 'Origenes',
            },
        ),
    ]
