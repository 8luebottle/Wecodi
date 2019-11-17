from django.urls import path
from .views import (
    SignUpView, LogInView, ProfileView,
    DeleteUserView,
)

urlpatterns = [
    path('', SignUpView.as_view()),
    path('/login', LogInView.as_view()),
    path('/profile', ProfileView.as_view()),
    path('/delete', DeleteUserView.as_view()),
]
