import bcrypt
import datetime
import json
import jwt
import requests

from django.http  import HttpResponse, JsonResponse
from django.views import View

from .models import User, Profile

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
Blocking User View (Admin) --> UserStatusView
"""

class SignUpView(View): # User SignUp
    def post(self, request):
        request_dict = json.loads(request.body)
        print(request_dict)

        new_user = User(
            email      = request_dict['email'],
            password   = request_dict['password'],
            first_name = request_dict['first_name'],
            last_name  = request_dict['last_name']
        ).save()

        return JsonResponse({'message' : 'SUCCESS'})


class LoginView(View): # User Login with their email
    pass


class KakaoLoginView(View):
    pass


class GoogleLoginView(View):
    pass


class FacebookLoginView(View):
    pass


class UserListView(View): #ADMIN ONLY (Need decorator)
    pass


class BlockUserView(View): # ADMIN Block user
    pass


class UserSatatusView(View): #Segmentation by User Status
    pass


class ProfileView(View): # User & Admin can Update their Profile
    pass


