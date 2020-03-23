import jwt
from django.conf import settings
from rest_framework import (authentication, exceptions) #authentication cambiar por api?
from .models import Administrador, Despachador
 
class JWTAdministradorAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'
 
    def authenticate(self, request):
        """
        Se llama al método `authenticate` en cada solicitud, independientemente de
         si el punto final requiere autenticación.
 
         `authenticate` tiene dos posibles valores de retorno:
 
         1) `None`: devolvemos` Ninguno` si no deseamos autenticarnos. Generalmente
                     Esto significa que sabemos que la autenticación fallará. Un ejemplo de
                     esto es cuando la solicitud no incluye un token en el
                     encabezados
 
         2) `(user,token)` - Devolvemos una combinación de usuario/token cuando
                              La autenticación es exitosa.
 
                             Si ninguno de los casos se cumple, eso significa que hay un error
                             y no devolvemos nada.
                             Simplemente planteamos el `AuthenticationFailed`
                             excepción y dejar Django REST Framework
                             manejar el resto
        """
        request.user = None
 
        # `auth_header` should be an array with two elements: 
        # 1) the name of the authentication header (in this case, "Token") and 
        # 2) the JWT that we should authenticate against.
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()
 
        if not auth_header:
            return None
 
        if len(auth_header) == 1:
            # Invalid token header. No credentials provided. Do not attempt to
            # authenticate.
            return None
 
        elif len(auth_header) > 2:
            # Invalid token header. The Token string should not contain spaces. Do
            # not attempt to authenticate.
            return None
 
        # The JWT library we're using can't handle the `byte` type, which is
        # commonly used by standard libraries in Python 3. To get around this,
        # we simply have to decode `prefix` and `token`. This does not make for
        # clean code, but it is a good decision because we would get an error
        # if we didn't decode these values.
        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')
 
        if prefix.lower() != auth_header_prefix:
            return None
        return self._authenticate_credentials(request, token)
 
    def _authenticate_credentials(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except:
            msg = 'Invalid authentication. Could not decode token.'
            raise exceptions.AuthenticationFailed(msg)
 
        try:
            user = Administrador.objects.get(pk=payload['id'])
        except Administrador.DoesNotExist:
            msg = 'No user matching this token was found.'
            raise exceptions.AuthenticationFailed(msg)
 
        if not user.is_active:
            msg = 'This user has been deactivated.'
            raise exceptions.AuthenticationFailed(msg)
        return (user, token)
 
class JWTDespachadorAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'
 
    def authenticate(self, request):
        """
        lo mismo que Administrador
        """
        request.user = None
 
        # `auth_header` should be an array with two elements: 1) the name of
        # the authentication header (in this case, "Token") and 2) the JWT
        # that we should authenticate against.
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()
 
        if not auth_header:
            return None
 
        if len(auth_header) == 1:
            # Invalid token header. No credentials provided. Do not attempt to
            # authenticate.
            return None
 
        elif len(auth_header) > 2:
            # Invalid token header. The Token string should not contain spaces. Do
            # not attempt to authenticate.
            return None
 
        # The JWT library we're using can't handle the `byte` type, which is
        # commonly used by standard libraries in Python 3. To get around this,
        # we simply have to decode `prefix` and `token`. This does not make for
        # clean code, but it is a good decision because we would get an error
        # if we didn't decode these values.
        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')
 
        if prefix.lower() != auth_header_prefix:
            return None
        return self._authenticate_credentials(request, token)
 
    def _authenticate_credentials(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except:
            msg = 'Invalid authentication. Could not decode token.'
            raise exceptions.AuthenticationFailed(msg)
 
        try:
            user = Despachador.objects.get(pk=payload['id'])
        except Despachador.DoesNotExist:
            msg = 'No user matching this token was found.'
            raise exceptions.AuthenticationFailed(msg)
            return
 
        if not user.is_active:
            msg = 'This user has been deactivated.'
            raise exceptions.AuthenticationFailed(msg)
        return (user, token)