# from rest_framework.validators import UniqueValidator
# from django.contrib.auth import authenticate
# from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
# from .models import User, Administrador, Despachador, Proyecto, Subcontratista, Camion, Origen, Suborigen, Destino, Material, Voucher
# from .models import Administrador, Despachador, Proyecto, Subcontratista, Camion, Origen, Suborigen, Destino, Material, Voucher
from .models import *


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()
    is_staff = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    class Meta(object):
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    def update(self, instance, validated_data):
        instance.save()
        return instance

class AdministradorSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()
    is_staff = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
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
    is_staff = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
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

class SubcontratistaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subcontratista
        fields = '__all__'

class CamionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Camion
        fields = '__all__'

class OrigenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Origen
        fields = '__all__'

class SuborigenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Suborigen
        fields = '__all__'

class DestinoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Destino
        fields = '__all__'

class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class VoucherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Voucher
        fields = '__all__'

class codigoQRSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CodigoQR
        fields = '__all__'

