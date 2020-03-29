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


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import *
from .models import *

# class SincronizacionDescarga(APIView):
#     def get(self, request):
#         # the many param informs the serializer that it will be serializing more than a single article.
#         return Response(
#             {
#                 "id": 1,
#                 "descarga":
#                 [
#                     {"longitud": "123.1313","latitud": "12.3454"},
#                     {"patente": "XCVB23","marca":"scania"}
#                 ]
#             }
#             )

class SincronizacionDescarga(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DespachadorSerializer
    def get(self, request):
        serializerDespachador = self.serializer_class(request.user) 
        queryproyecto = Proyecto.objects.get(id=serializerDespachador.data['proyecto'])
        serializerProyecto = ProyectoSerializer(queryproyecto)
        serializerProyecto.data['origen']= True
        print(serializerProyecto.data)
        descarga = {}
        descarga['request']= True
        descarga['data']= {
            "id_despachador": serializerDespachador.data['id'],
            "id_origenAsignado": serializerDespachador.data['origen_asignado'],
            "dataproyecto": serializerProyecto.data
        }
        return Response(descarga, status=status.HTTP_200_OK)

# class SincronizacionDescarga(APIView):
#     permission_classes = (IsAuthenticated,)
#     def get_object(self, pk):
#         try:
#             return Despachador.objects.get(pk=pk)
#         except Despachador.DoesNotExist:
#             raise Http404
#     def get(self, request, pk):
#         despachador = self.get_object(pk)
#         origen = Origen.objects.all()
#         suborigen = Suborigen.objects.all()
#         destino = Destino.objects.all()


#         material = Material.objects.all()
#         subcontratista = Subcontratista.objects.all()
#         camiones = Camion.objects.all()
#         voucher = Voucher.objects.all() #filtrar: solo mostrar los del día
#         #CodigoQR
#         serializerDespachador = DespachadorSerializer(camiones, many=True)
#         serializerOrigen = OrigenSerializer(origen, many=True)
#         serializerSuborigen = SuborigenSerializer(camiones, many=True)
#         serializerDestino = DestinoSerializer(origen, many=True)

#         serializerMaterial = MaterialSerializer(camiones, many=True)
#         serializerSubcontratista = SubcontratistaSerializer(origen, many=True)
#         serializerCamion = CamionSerializer(camiones, many=True)
#         serializerVoucher = VoucherSerializer(origen, many=True)
#         # serializerCodigoQR = CodigoQRSerializer(origen, many=True)
#         return Response([serializerCamion.data,serializerOrigen.data])

        # user_details = {}
        # user_details['request']= True
        # user_details['data']= {
        #     "id_despachador": id_despachador,
        #     "id_origenAsignado": origen,
        #     'proyecto': {
        #         'centro_de_coste': centrodecoste,
        #         'nombre_proyecto'
        #         'origen':[
        #             {
        #                 'origen':origen,
        #                 'suborigen':[
        #                     {suborigen},
        #                     {suborigen},
        #                     {suborigen}
        #                 ]
        #             },
        #             {
        #                 'origen':origen,
        #                 'suborigen':[
        #                     {suborigen},
        #                     {suborigen},
        #                     {suborigen}
        #                 ]
        #             },
        #         ],
        #         'destino':[
        #             {
        #                 'id_destino':algo,
        #                 'material':[
        #                     {material},
        #                     {material}
        #                 ]
        #             },
        #             {
        #                 'id_destino':algo,
        #                 'material':[
        #                     {material},
        #                     {material}
        #                 ]
        #             }
        #         ],
        #         'subcontratista':[
        #             camion:[
        #                 codigoQR
        #             ]
        #         ]
        #     }
        # }



class ProyectoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer


# Registra un nuevo usuario
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
    def post(self, request):
        user = request.data
        serializer = AdministradorSerializer(data=user)
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
    permission_classes = (IsAuthenticated,)# Allow only authenticated users to access this url
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
        # user = User.objects.get(rut=rut, password=password)
        user = User.objects.get(rut=rut)
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
            res = {'request': 'False', 'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {'request': 'False', 'error': 'please provide a rut and a password'}
        return Response(res)



class SubcontratistaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Subcontratista.objects.all()
    serializer_class = SubcontratistaSerializer

class CamionViewSet(viewsets.ModelViewSet):
    queryset = Camion.objects.all()
    serializer_class = CamionSerializer

class OrigenViewSet(viewsets.ModelViewSet):
    queryset = Origen.objects.all()
    serializer_class = OrigenSerializer

class SuborigenViewSet(viewsets.ModelViewSet):
    queryset = Suborigen.objects.all()
    serializer_class = SuborigenSerializer

class DestinoViewSet(viewsets.ModelViewSet):
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class VoucherViewSet(viewsets.ModelViewSet):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer

class codigoQRViewSet(viewsets.ModelViewSet):
    class Meta:
        model = CodigoQR
        fields = '__all__'



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
