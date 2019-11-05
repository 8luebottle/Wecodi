import bcrypt
import datetime
import json
import jwt
import requests

from django.http  import HttpResponse, JsonResponse
from django.views import View

"""
SignUp
LogIn
    - Email
    - Kakao
    - Google
    - Facebook
LogOut
Delete Account
Change PW
Profile
    - Create
    - Update
    - View
User List View (Admin)
    - All
    - Blocked
    - Unblocked
Blocking User View (Admin)
"""

class SignUpView(View): # User SignUp
    def post(self, request):
        request_dict = json.loads(request.body)
        print(request_dict)

        """
            new_user = (
                email      : request_dict['email']
                first_name : request_dict['first_name']
                last_name  : request_dict['last_name']
            ).create()
        """

        return JsonResponse({'message' : 'SUCCESS'})

