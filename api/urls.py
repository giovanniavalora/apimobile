from django.urls import path, include
from rest_framework import routers
from . import views
from api.views import *


# app_name = "api"


router = routers.DefaultRouter()
router.register(r'Proyecto', views.ProyectoViewSet)

# router.register(r'Administrador', views.AdministradorViewSet)
# router.register(r'Despachador', views.DespachadorViewSet)
# router.register(r'auth', views.UserLogin)

router.register(r'Subcontratista', views.SubcontratistaViewSet)
router.register(r'Camion', views.CamionViewSet)
router.register(r'Origen', views.OrigenViewSet)
router.register(r'Suborigen', views.SuborigenViewSet)
router.register(r'Destino', views.DestinoViewSet)
router.register(r'Material', views.MaterialViewSet)
router.register(r'Voucher', views.VoucherViewSet)
router.register(r'CodigoQR', views.VoucherViewSet)
# rouer.register(r'SincronizacionDescarga', SincronizacionDescarga.as_view())


urlpatterns = [
    path('', include(router.urls)),
    # path('crearUsuario/', CreateUserAPIView.as_view()),
    path('crearAdministrador/', CreateAdminAPIView.as_view()),
    path('crearDespachador/', CreateDespAPIView.as_view()),
    path('login/', authenticate_user),
    path('update/', UserRetrieveUpdateAPIView.as_view()),
    path('SincronizacionDescarga/', SincronizacionDescarga.as_view()),
    # path('SincronizacionDescarga/<int:pk>/', SincronizacionDescarga.as_view()),

    # path('AdministradorTest/', AdministradorTest.as_view()),
    # path('Texto/', Texto.as_view()),
    # path('userlogin', UserLogin.as_view()),
    # path('user-admin/', AdministradorRegistration.as_view()),
    # path('user-desp/', DespachadorRegistration.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
