# import jwt
# from django.conf import settings
# from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager)
# from django.utils import timezone
# from datetime import datetime, timedelta

from django.db import models


class Proyecto(models.Model):
    centro_de_coste = models.CharField(max_length = 20, unique=True)
    nombre_proyecto = models.CharField(max_length = 100)
    ubicacion = models.CharField(max_length = 100)
    cliente = models.CharField(max_length = 100)
    rut_cliente = models.CharField(max_length = 20)
    mandante = models.CharField(max_length = 100)
    rut_mandante = models.CharField(max_length = 20)
    mandante_final = models.CharField(max_length = 100)

    def __str__(self):
        return self.centro_de_coste

class Administrador(models.Model):
    username_admin = models.CharField(max_length = 20, unique=True)
    password_admin = models.CharField(max_length=128)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    # id_proyecto = models.ForeignKey(Proyecto, related_name='administradores', on_delete=models.CASCADE)

    def __str__(self):
        return self.username_admin

    class Meta:
        verbose_name_plural = "Administradores"

class Despachador(models.Model):
    rut_despachador = models.CharField(max_length = 20, unique=True)
    password_despachador = models.CharField(max_length=128)
    nombre_despachador = models.CharField(max_length = 50)
    apellido_despachador = models.CharField(max_length = 50)
    telefono_despachador = models.CharField(max_length = 20)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    # id_proyecto = models.ForeignKey(Proyecto, related_name='despachadores', on_delete=models.CASCADE)

    def __str__(self):
        return self.rut_despachador

    class Meta:
        verbose_name_plural = "Despachadores"

# class Voucher(models.Model):
#     id_despachador = models.ForeignKey(Despachador, on_delete=models.CASCADE, null=True)
#     proyecto = models.CharField(max_length = 100)
#     nombre_cliente = models.CharField(max_length = 50)
#     rut_cliente = models.CharField(max_length = 20)
#     nombre_subcontratista = models.CharField(max_length = 100)
#     rut_subcontratista = models.CharField(max_length = 20)
#     nombre_conductor_principal = models.CharField(max_length = 50)
#     apellido_conductor_principal = models.CharField(max_length = 50)
#     fecha = models.CharField(max_length = 20)
#     hora = models.CharField(max_length = 20)
#     patente = models.CharField(max_length = 20)
#     volumen = models.CharField(max_length = 20)
#     tipo_material = models.CharField(max_length = 50)
#     punto_origen = models.CharField(max_length = 100)
#     punto_suborigen = models.CharField(max_length = 100)
#     punto_destino = models.CharField(max_length = 100)
#     contador_impresiones = models.IntegerField()

# class Subcontratista(models.Model):
#     id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True)
#     rut = models.CharField(max_length = 20)
#     razon_social = models.CharField(max_length = 100)
#     nombre_subcontratista = models.CharField(max_length = 100)
#     nombre_contacto = models.CharField(max_length = 50)
#     apellido_contacto = models.CharField(max_length = 50)
#     email_contacto = models.CharField(max_length = 100, blank=True, default='')
#     telefono_contacto = models.CharField(max_length = 20)

# class Camion(models.Model):
#     id_subcontratista = models.ForeignKey(Subcontratista, on_delete=models.CASCADE, null=True)
#     patente_camion = models.CharField(max_length = 20)
#     marca_camion = models.CharField(max_length = 20)
#     modelo_camion = models.CharField(max_length = 20)
#     capacidad_camion = models.CharField(max_length = 20)
#     nombre_conductor_principal = models.CharField(max_length = 50)
#     apellido_conductor_principal = models.CharField(max_length = 50)
#     telefono_conductor_principal = models.CharField(max_length = 20)
#     descripcion = models.CharField(max_length = 20)
#     QR = models.CharField(max_length = 200)    #almacenar la imagen del QR? id?

# class Origen(models.Model):
#     id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True)
#     nombre_origen = models.CharField(max_length = 100)
#     longitud = models.CharField(max_length = 20)
#     latitud = models.CharField(max_length = 20)

# class Suborigen(models.Model):
#     id_origen = models.ForeignKey(Origen, on_delete=models.CASCADE, null=True)
#     nombre_suborigen = models.CharField(max_length = 20)
#     activo = models.BooleanField()

# class Destino(models.Model):
#     id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True)
#     nombre_destino = models.CharField(max_length = 100)
#     nombre_propietario = models.CharField(max_length = 100)
#     rut_propietario = models.CharField(max_length = 20)
#     direccion = models.CharField(max_length = 100)
#     longitud = models.CharField(max_length = 20)
#     latitud = models.CharField(max_length = 20)

# class Material(models.Model):
#     id_destino = models.ForeignKey(Destino, on_delete=models.CASCADE, null=True)
#     material = models.CharField(max_length = 50)














# #Autenticacion y Autorizacion
# class UserManager(BaseUserManager):
#     def get_by_natural_key(self, rut):
#         return self.get(rut=rut)
 
# class AdministradorManager(BaseUserManager):
#     def create_administrador(self, first_name, last_name, rut, email, id_proyecto, password=None):
#         if rut is None:
#             raise TypeError('Users must have a rut.')
#         administrador = Administrador(first_name=first_name, last_name=last_name, 
#                           rut=rut, email=self.normalize_email(email),
#                           id_proyecto=id_proyecto)
#         administrador.set_password(password)
#         administrador.save()
#         return administrador
 
# class DespachadorManager(BaseUserManager):
#     def create_despachador(self, first_name, last_name, rut, email, phone, password=None):
#         if rut is None:
#             raise TypeError('Users must have a rut.')
#         despachador = Despachador(first_name=first_name, last_name=last_name, 
#                             rut=rut, email=self.normalize_email(email),
#                             phone=phone)
#         despachador.set_password(password)
#         despachador.save()
#         return despachador


# #Primero se crea la clase user de la cual heredaran Administrador y Despachador
# class User(AbstractBaseUser, PermissionsMixin):
#     rut = models.CharField(db_index=True, max_length=13, unique=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)

#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
 
#     USERNAME_FIELD = 'rut'
#     REQUIRED_FIELDS = ['first_name','last_name',]
    
#     objects = UserManager()
 
#     @property
#     def token(self):
#         dt = datetime.now() + timedelta(hours=12)
#         token = jwt.encode({
#             'id': user_id,
#             'exp': int(time.mktime(dt.timetuple()))
#         }, settings.SECRET_KEY, algorithm='HS256')
#         return token.decode('utf-8')
 
#     def get_full_name(self):
#         return (self.first_name+' '+self.last_name)

#     def get_short_name(self):
#         return self.first_name
 
#     def natural_key(self):
#         return (self.first_name, self.last_name)
 
#     def __str__(self):
#         return self.rut


# class Administrador(User, PermissionsMixin):
#     id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True)
#     email = models.EmailField(db_index=True, unique=True)
 
#     USERNAME_FIELD = 'rut'
#     REQUIRED_FIELDS = ['first_name', 'last_name','email' ]
 
#     objects = AdministradorManager()
 
#     def __str__(self):
#         return self.first_name

# class Despachador(User, PermissionsMixin):
#     id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True)
#     phone= models.CharField(max_length = 20)
 
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']
 
#     objects = DespachadorManager()
 
#     def __str__(self):
#         return self.first_name

