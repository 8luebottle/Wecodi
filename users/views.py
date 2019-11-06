# A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z.

import bcrypt
import datetime
import json
import jwt
import re
import requests

from django.http  import HttpResponse, JsonResponse
from django.views import View

from .models import User, Profile

"""
LogIn (Email, Kakao, Google, Facebook)
LogOut
Delete Account
Change PW
Profile(Create, Update, View)
ADMIN User List View (All, Blocked, Unblocked)
Blocking User View (Admin) --> UserStatusView
"""

class SignUpView(View): # User SignUp
    """
    [VALID_PASSWORD]
    Min 6 characters, at least 1 uppercase letter, 
    1 lowercase letter, 1 number and 1 special character
    """
    def password_validation(self, password):
        regex_pw = re.compile(
            r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$'
        )
        return True if regex_pw.match(password) else False

    def email_validation(self, email):
        regex_email = re.compile(
            r'(\w+[.|\w])*@(\w+[.])*\w+'
        )
        return True if regex_email.match(email) else False

    def post(self, request):
        request_dict = json.loads(request.body)

        email      = request_dict['email']
        password   = request_dict['password']
        first_name = request_dict['first_name']
        last_name  = request_dict['last_name']

        if(not(first_name and first_name.strip())):
            return JsonResponse({'error':'INPUT_FIRST_NAME'}, status=401)

        if(not(last_name and last_name.strip())):
            return JsonResponse({'error':'INPUT_LAST_NAME'}, status=401)

        if User.objects.filter(email=email).exists():
            return JsonResponse({'error' : 'EMAIL_EXISTS'}, status=409)
        elif not self.email_validation(email):
            return JsonResponse({'error': 'INVALID_EMAIL'}, status=401)

        if self.password_validation(password):
            password     = bytes(password, 'UTF-8')
            salt         = bcrypt.gensalt()
            encrypted_pw = bcrypt.hashpw(password, salt)
        else:
            return JsonResponse({'error': 'WEAK_PASSWORD'}, status=400)
        
        User(
            email      = email,
            password   = encrypted_pw,
            first_name = first_name,
            last_name  = last_name
        ).save()

        return JsonResponse({'message' : 'SUCCESS'})


class LogInView(View): # User Login with their email
    """ WIP """
    def post(self, request):
        request_dict = json.loads(request.body)
        email    = request_dict['email']
        password = request_dict['password']

        print(request_dict)
        print('This is email', email)
        print('This is Password', password)

        user = User.objects.filter(email=email)

        if user.exists():
            user = user.get()
            print('THIS IS DB PASSWORD', user.password)
            
            print('\n bcrpyt.check', password.encode('UTF-8'))
            print('\n user.pass', user.password.encode('UTF-8'))

            if bcrypt.checkpw(password.encode('UTF-8'), user.password.encode('UTF-8')):
                """ADD Payload Later"""
                return JsonResponse({'message' : 'SUCCESS'})
        else:
            return JsonResponse({'error': 'INVALID_EMAIL'}, status=401)


class KakaoLogInView(View):
    pass


class GoogleLogInView(View):
    pass


class FacebookLogInView(View):
    pass


class UserListView(View): #ADMIN ONLY (Need decorator)
    pass


class BlockUserView(View): # ADMIN Block user
    pass


class UserSatatusView(View): #Segmentation by User Status
    pass


class ProfileView(View): # User & Admin can Update their Profile
    pass


