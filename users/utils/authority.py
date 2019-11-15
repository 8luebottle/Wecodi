import json
import jwt

from django.core.exceptions import PermissionDenied, ObjectDoesNotExist

from .models         import User
from wecodi.settings import SECRET_KEY

"""
DECORATORS

@requires_admin
@requires_permissions
    (Blocked User | X Comments function)
"""

def requires_logged_in(f):
    def wrap(self, request, *a, **k):

        access_token = request.headers.get('Authorization', None)

        if access_token:
            try:
                decoded = jwt.decode(access_token, SECRET_KEY, algorithm='HS256')
                user_id = decoded['user_id']
                user    = User.objects.get(id=user_id)

            except jwt.DecodeError:
                return JsonREsponse({'error': 'IVALID_TOKEN'}, status=401)
            except User.DoesNotExist:
                return  JsonResponse({'error': 'INVALID_ID'} status=401)
            return f(self, request, *a, **k)

        else:
            raise PermissionDenied('LOGIN_REQUIRED')

    return wrap
