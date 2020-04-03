##### Auth #####
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.signals import user_logged_in
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework_jwt.utils import jwt_payload_handler

from django.conf import settings
import jwt
################


from rest_framework.parsers import MultiPartParser, FormParser #Para Subir imagen

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import *
from .models import *


class IngresarDespachoApiView(APIView):
    serializer_class = IngresarDespachoSerializer

    def post(self, request, *args, **kwargs):
        resp = {}
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        for objeto in serializer.data["vouchers"]:
            parser_classes = (MultiPartParser, FormParser)
            file_serializer = VoucherSerializer(data=objeto)
            if file_serializer.is_valid():
                file_serializer.save()
            else:
                resp['request']= False
                resp['error'] = file_serializer.errors
                return Response(resp, status=status.HTTP_201_CREATED)
        resp['request']= True
        resp['data'] = serializer.data
        return Response(resp, status=status.HTTP_201_CREATED)


class SincronizacionDescargaApiView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        serializerDespachador = DespachadorSerializer(request.user) 
        serializerDespachador.is_valid(raise_exception=True)
        id_despachador = serializerDespachador.data['id']
        origen_asignado = serializerDespachador.data['origen_asignado']
        id_proyecto = serializerDespachador.data['proyecto']

        queryproyecto = Proyecto.objects.get(id=id_proyecto)
        serializerProyecto = ProyectoAnidadoSerializer(queryproyecto)

        queryvoucher = Voucher.objects.filter(despachador=id_despachador)
        serializerVoucher = VoucherSerializer(queryvoucher, many=True)

        serializerProyecto.data['origen']= True
        descarga = {}
        descarga['request']= True
        descarga['data']= {
            "id_despachador": id_despachador,
            "id_origenAsignado": origen_asignado,
            "dataproyecto": serializerProyecto.data,
            "voucher": serializerVoucher.data
        }
        return Response(descarga, status=status.HTTP_200_OK)


# class SincDesc(RetrieveUpdateAPIView):
#     serializer_class = ProyectoAnidadoSerializer
#     queryset = Proyecto.objects.all()


class ProyectoViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

class SubcontratistaViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Subcontratista.objects.all()
    serializer_class = SubcontratistaSerializer

class CamionViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Camion.objects.all()
    serializer_class = CamionSerializer

class OrigenViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Origen.objects.all()
    serializer_class = OrigenSerializer

class SuborigenViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Suborigen.objects.all()
    serializer_class = SuborigenSerializer

class DestinoViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class VoucherViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer

class CodigoQRViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = CodigoQR.objects.all()
    serializer_class = VoucherSerializer



# Registra un nuevo usuario General (ni despachador ni administrador)
# class CreateUserAPIView(APIView):
#     # permission_classes = (IsAuthenticated,)
#     permission_classes = (AllowAny,) # permitir que cualquier usuario (autenticado o no) acceda a esta URL.
#     def post(self, request):
#         user = request.data
#         print(user)
#         serializer = UserSerializer(data=user)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# Registra un nuevo usuario Administrador
class CreateAdminAPIView(APIView):
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,) # permitir que cualquier usuario (autenticado o no) acceda a esta URL.
    serializer_class = AdministradorSerializer
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        resp = {}
        resp['request']= True
        resp['data']= serializer.data
        return Response(resp, status=status.HTTP_201_CREATED)


# Registra un nuevo usuario Despachador
class CreateDespAPIView(APIView):
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,) # permitir que cualquier usuario (autenticado o no) acceda a esta URL.
    def post(self, request):
        user = request.data
        serializer = DespachadorSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save() #el metodo .save del serializador llamará al metodo create cuando desee crear un objeto y al método update cuando desee actualizar.
        resp = {}
        resp['request']= True
        resp['data']= serializer.data
        return Response(resp, status=status.HTTP_201_CREATED)


# Obtener información de usuario o Actualizarlo (con token)
class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    # permission_classes = (IsAuthenticated,)# Allow only authenticated users to access this url
    serializer_class = UserSerializer
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user) #serializador para manejar la conversión de nuestro objeto `Usuario` en algo que puede ser JSONified y enviado al cliente.
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})
        serializer = UserSerializer(request.user, data=serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        resp = {}
        resp['request']= True
        resp['data']= serializer.data
        return Response(resp, status=status.HTTP_200_OK)


# Login (Devuelve el Token)
@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
    try:
        rut = request.data['rut']
        password = request.data['password']
        if User.objects.filter(rut=rut).exists():
            user = User.objects.get(rut=rut)
        else:
            res = {'request': False, 'error': 'no puede autenticarse con las credenciales dadas o la cuenta ha sido desactivada'}
            return Response(res)
        if user.check_password(password):
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)
                resp = {}
                resp['request']= True
                resp['data']= {'token': token}
                user_logged_in.send(sender=user.__class__, request=request, user=user) # almacenamos el último tiempo de inicio de sesión del usuario con este código.
                return Response(resp, status=status.HTTP_200_OK)

            except Exception as e:
                raise e
        else:
            res = {'request': False, 'error': 'no puede autenticarse con las credenciales dadas o la cuenta ha sido desactivada'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {'request': False, 'error': 'por favor proporcione un rut y una password'}
        return Response(res)
    



# class Texto(APIView):
#     def post(self,request):
#         # serializer_context = {
#         #     'request': request,
#         # }
#         if(request.data['proyect_id']>0):
#             adminregister=Administrador.objects.all().filter(proyecto=request.data['proyect_id'])
#             if(len(adminregister)>0):
#                 serializer = AdministradorSerializer(adminregister, many=True)
#                 return Response(serializer.data)
#             else:
#                 return Response("No existen administradores en este proyecto")
#         else:
#             return Response("Proyecto no existe")
