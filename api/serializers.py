# from rest_framework.validators import UniqueValidator
# from django.contrib.auth import authenticate
# from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
# from .models import User, Administrador, Despachador, Proyecto, Subcontratista, Camion, Origen, Suborigen, Destino, Material, Voucher
# from .models import Administrador, Despachador, Proyecto, Subcontratista, Camion, Origen, Suborigen, Destino, Material, Voucher
from .models import *


class ProyectoSerializer(serializers.ModelSerializer):
    # administradores = serializers.RelatedField(many=True, read_only=True)    
    # despachadores = serializers.RelatedField(many=True, read_only=True)
    class Meta:
        model = Proyecto
        fields = '__all__'
        # fields = ('id','centro_de_coste','nombre_proyecto','ubicacion',
        # 'cliente','rut_cliente','mandante','rut_mandante','mandante_final')
        # fields = ('id','url','centro_de_coste','nombre_proyecto','ubicacion',
        # 'cliente','rut_cliente','mandante','rut_mandante','mandante_final',
        # 'despachadores','administradores')


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()
    class Meta(object):
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.save()
        return instance

class AdministradorSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()
    class Meta(object):
        model = Administrador
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        return Administrador.objects.create_superuser(**validated_data)
    def update(self, instance, validated_data):
        instance.rut = validated_data.get('rut', instance.rut)
        instance.nombre = validated_data.get('content', instance.nombre)
        instance.apellido = validated_data.get('content', instance.apellido)
        instance.proyecto = validated_data.get('created', instance.proyecto)
        instance.save()
        return instance

class DespachadorSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()
    class Meta(object):
        model = Despachador
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        return Despachador.objects.create_user(**validated_data)
    def update(self, instance, validated_data):
        instance.rut = validated_data.get('rut', instance.rut)
        instance.nombre = validated_data.get('content', instance.nombre)
        instance.apellido = validated_data.get('content', instance.apellido)
        instance.proyecto = validated_data.get('created', instance.proyecto)
        instance.save()
        return instance




# class AdministradorSerializer(serializers.ModelSerializer):
#     # id_proyecto_id = serializers.RelatedField(source='id_proyecto', read_only=True)
#     class Meta:
#         model = Administrador
#         fields = '__all__'
#         # fields = ('id','url','username_admin','password_admin','id_proyecto_id')
        
# class DespachadorSerializer(serializers.ModelSerializer):
#     # id_proyecto_id = serializers.RelatedField(source='id_proyecto', read_only=True)
#     class Meta:
#         model = Despachador
#         fields = '__all__'
#         # fields = ('id','rut_despachador','password_despachador','nombre_despachador',
#         # 'apellido_despachador','telefono_despachador','id_proyecto_id')




class SubcontratistaSerializer(serializers.HyperlinkedModelSerializer):
    # id_proyecto_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Subcontratista
        fields = '__all__'
        # fields = ('id','url','rut','razon_social','nombre_subcontratista','nombre_contacto',
        # 'apellido_contacto','email_contacto','telefono_contacto','id_proyecto_id')

class CamionSerializer(serializers.HyperlinkedModelSerializer):
    # id_subcontratista_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Camion
        fields = '__all__'
        # fields = ('id','url','patente_camion','marca_camion','modelo_camion','capacidad_camion',
        # 'nombre_conductor_principal','apellido_conductor_principal',
        # 'telefono_conductor_principal','descripcion','QR','id_subcontratista_id')

class OrigenSerializer(serializers.HyperlinkedModelSerializer):
    # id_proyecto_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Origen
        fields = '__all__'
        # fields = ('id','nombre_origen','longitud','latitud','id_proyecto_id')

class SuborigenSerializer(serializers.HyperlinkedModelSerializer):
    # id_origen_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Suborigen
        fields = '__all__'
        # fields = ('id','nombre_suborigen','activo','id_origen_id')

class DestinoSerializer(serializers.HyperlinkedModelSerializer):
    # id_proyecto_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Destino
        fields = '__all__'
        # fields = ('id','nombre_destino','nombre_propietario','rut_propietario','direccion','longitud','latitud','id_proyecto_id')

class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    id_destino_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Material
        fields = '__all__'
        # fields = ('id','material','id_destino_id')

class VoucherSerializer(serializers.HyperlinkedModelSerializer):
    # id_despachador_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Voucher
        fields = '__all__'
        # fields = ('id','proyecto','nombre_cliente','rut_cliente','nombre_subcontratista','rut_subcontratista',
        # 'nombre_conductor_principal','apellido_conductor_principal','fecha','hora','patente','volumen','tipo_material',
        # 'punto_origen','punto_suborigen','punto_destino','contador_impresiones','id_despachador_id')












#autenticación y autorización
# class AdministradorRegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(
#         max_length=128,
#         min_length=8,
#         write_only=True
#     )
#     token = serializers.CharField(max_length=255, read_only=True)
 
#     class Meta:
#         model = Administrador
#         fields = '__all__'
 
#     def create(self, validated_data):
#         return Administrador.objects.create_administrador(**validated_data)
 
# class DespachadorRegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(
#         max_length=128,
#         min_length=8,
#         write_only=True
#     )
#     token = serializers.CharField(max_length=255, read_only=True)
 
#     class Meta:
#         model = Despachador
#         fields = '__all__'
 
#     def create(self, validated_data):
#         return Despachador.objects.create_despachador(**validated_data)



# Los serializadores anteriores AdministradorRS y DespachadorRS devolverán un token de usuario si la autenticación es exitosa. 
# A continuación, crearemos Crearemos UserLoginSerializer para proporcionar na forma de iniciar sesión a los usuarios existentes. 
# class UserLoginSerializer(serializers.Serializer):
#     rut = serializers.CharField(max_length=13)
#     password = serializers.CharField(max_length=128, write_only=True)
#     token = serializers.CharField(max_length=255, read_only=True)
 
#     def validate(self, data):
#         # The `validate` method is where we make sure that the current
#         # instance of `LoginSerializer` has "valid". In the case of logging a
#         # user in, this means validating that they've provided an email
#         # and password and that this combination matches one of the users in
#         # our database.
#         rut = data.get('rut', None)
#         password = data.get('password', None)
 
#         # The `authenticate` method is provided by Django and handles checking
#         # for a user that matches this email/password combination. Notice how
#         # we pass `email` as the `username` value since in our User
#         # model we set `USERNAME_FIELD` as `email`.
#         user = authenticate(username=rut, password=password)
 
#         # If no user was found matching this email/password combination then
#         # `authenticate` will return `None`. Raise an exception in this case.
#         if user is None:
#             raise serializers.ValidationError(
#                 'A user with this rut and password is not found.'
#             )
#         try:
#             userObj = Administrador.objects.get(rut=user.rut)
#         except Administrador.DoesNotExist:
#             userObj = None 
 
#         try:
#             if userObj is None:
#                 userObj = Despachador.objects.get(rut=user.rut)
#         except Despachador.DoesNotExist:
#             raise serializers.ValidationError(
#                 'User with given rut and password does not exists'
#             )        
 
#         # Django provides a flag on our `User` model called `is_active`. The
#         # purpose of this flag is to tell us whether the user has been banned
#         # or deactivated. This will almost never be the case, but
#         # it is worth checking. Raise an exception in this case.
#         if not user.is_active:
#             raise serializers.ValidationError(
#                 'This user has been deactivated.'
#             )
 
#         # The `validate` method should return a dictionary of validated data.
#         # This is the data that is passed to the `create` and `update` methods
#         # that we will see later on.
#         return {
#             'email': user.rut,
#             'token': user.token
#         }