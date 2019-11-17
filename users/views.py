# A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z.

import bcrypt
import datetime
import json
import jwt
import re
import requests

from django.http     import HttpResponse, JsonResponse
from django.views    import View

from wecodi.settings       import SECRET_KEY
from users.utils.authority import requires_logged_in, requires_admin
from .models               import User, Profile

"""
LogIn (Kakao, Google, Facebook),LogOut
Delete Account
Change PW
Profile(Update, View)
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
            password   = encrypted_pw.decode('UTF-8'),
            first_name = first_name,
            last_name  = last_name
        ).save()

        return JsonResponse({'message' : 'SUCCESS'})


class LogInView(View): # User Login with their email
    def post(self, request):
        request_dict = json.loads(request.body)

        email     = request_dict['email']
        password  = request_dict['password']
        user      = User.objects.filter(email=email, deleted=False)

        if user.exists():
            user = user.get()
            now  = datetime.datetime.utcnow()

            # Instead of get email, use id
            if bcrypt.checkpw(password.encode('UTF-8'), user.password.encode('UTF-8')):
                payload = {
                    'sub': user.id,
                    'iat': now,
                    'exp': now + datetime.timedelta(weeks=1),
                }
                encoded = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

                return JsonResponse({'access_token': encoded.decode('UTF-8')})

            else:
                return JsonResponse({'error': 'INVALID_PASSWORD'}, status=401)

        else:
            return JsonResponse({'error': 'INVALID_EMAIL'}, status=401)

    
class KakaoLogInView(View):
    pass


class GoogleLogInView(View):
    pass


class FacebookLogInView(View):
    pass


class DeleteUserView(View):
    @requires_logged_in
    def post(self, request):
        user = request.user
        print('\nUSER\n', user.id, user.email)

        #return JsonResponse({'message':})
    


class UserListView(View): #ADMIN ONLY (Need decorator)
    #@requires_admin
    pass


class UserDetailListView(View):
    #@requires_admin
    pass


class BlockUserView(View): # ADMIN Block user
    #@requires_admin
    pass


class UserSatatusView(View): #Segmentation by User Status
    #@requires_admin
    pass


class ProfileView(View): # User & Admin can Update their Profile
    @requires_logged_in
    def post(self, request): # Update Profile
        user = request.user
        profile_dict = json.loads(request.body)

        Profile(
            nickname    = profile_dict['nickname'],
            bio         = profile_dict['bio'],
            profile_img = profile_dict['image'],
            user_id     = user.id,
        ).save()

        return JsonResponse({'message':'SUCCESS'})


    @requires_logged_in
    def get(self, request): # Own Profile View
        user = request.user
        user_profile = Profile.objects.filter(user_id=user.id).get()
       
        return JsonResponse(
            {
                'nickname'    : user_profile.nickname,
                'bio'         : user_profile.bio,
                'profile_img' : user_profile.profile_img,
                'last_update' : user_profile.updated_at
            }
        )


class DeleteUserView(View):
    @requires_logged_in
    def get(self, request): # Own Profile View
        user = request.user
        user_profile = Profile.objects.filter(user_id=user.id).get()
       
        return JsonResponse(
            {
                'nickname'    : user_profile.nickname,
                'bio'         : user_profile.bio,
                'profile_img' : user_profile.profile_img,
                'last_update' : user_profile.updated_at
            }
        )
