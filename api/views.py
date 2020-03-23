#from django.shortcuts import render
# from rest_framework import status
# from rest_framework.decorators import action
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.renderers import JSONRenderer
# from .renderers import UserJSONRenderer
from rest_framework.response import Response

from rest_framework import viewsets
from .serializers import *
from .models import *

# import requests

# req = requests.Request('POST','http://stackoverflow.com',headers={'X-Custom':'Test'},data='a=1&b=2')
# prepared = req.prepare()

# def pretty_print_POST(req):
#     """
#     At this point it is completely built and ready
#     to be fired; it is "prepared".

#     However pay attention at the formatting used in 
#     this function because it is programmed to be pretty 
#     printed and may differ from the actual request.
#     """
#     print('{}\n{}\r\n{}\r\n\r\n{}'.format(
#         '-----------START-----------',
#         req.method + ' ' + req.url,
#         '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
#         req.body,
#     ))

# pretty_print_POST(prepared)

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


# class SincronizacionDescarga(APIView):
#     def get(self, request):
#         camiones = Camion.objects.all()
#         origen = Origen.objects.all()
#         serializerCamion = CamionSerializer(camiones, many=True)
#         serializerOrigen = OrigenSerializer(origen, many=True)
#         return Response([serializerCamion.data,serializerOrigen.data])


class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

class AdministradorTest(APIView):
    def post(self, request, format=None):
        print(request)
        serializer = AdministradorSerializer(data=request.data)
        serializer.save()
        return Response(request.POST)

    def get(self, request, format=None):
        queryset = Administrador.objects.all()
        serializer_class = AdministradorSerializer(queryset, many=True)
        return Response(serializer_class.data)

class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

#     def post(self, request, format=None):
#         print(request)
        # serializer = AdministradorSerializer(data=request.data)
        # return request
# from api.models import Administrador
# p = Administrador(username_admin='administrator', password_admin="terminator", proyecto_id=1)
# p.save()


    
class DespachadorViewSet(viewsets.ModelViewSet):
    queryset = Despachador.objects.all()
    serializer_class = DespachadorSerializer

# class SubcontratistaViewSet(viewsets.ModelViewSet):
#     queryset = Subcontratista.objects.all()
#     serializer_class = SubcontratistaSerializer

# class CamionViewSet(viewsets.ModelViewSet):
#     queryset = Camion.objects.all()
#     serializer_class = CamionSerializer

# class OrigenViewSet(viewsets.ModelViewSet):
#     queryset = Origen.objects.all()
#     serializer_class = OrigenSerializer

# class SuborigenViewSet(viewsets.ModelViewSet):
#     queryset = Suborigen.objects.all()
#     serializer_class = SuborigenSerializer

# class DestinoViewSet(viewsets.ModelViewSet):
#     queryset = Destino.objects.all()
#     serializer_class = DestinoSerializer

# class MaterialViewSet(viewsets.ModelViewSet):
#     queryset = Material.objects.all()
#     serializer_class = MaterialSerializer

# class VoucherViewSet(viewsets.ModelViewSet):
#     queryset = Voucher.objects.all()
#     serializer_class = VoucherSerializer




#Autenticación y Autorización
# class AdministradorRegistration(APIView): #vista para crear un administrador
#     permission_classes = (AllowAny,)
#     renderer_classes = (UserJSONRenderer,)
#     serializer_class = AdministradorRegistrationSerializer
 
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
 
# class DespachadorRegistration(APIView): #vista para crear un despachador
#     permission_classes = (AllowAny,)
#     renderer_classes = (UserJSONRenderer,)
#     serializer_class = DespachadorRegistrationSerializer
 
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
 
# class UserLogin(APIView):
#     permission_classes = (AllowAny,)
#     renderer_classes = (UserJSONRenderer,)
#     serializer_class = UserLoginSerializer
 
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)