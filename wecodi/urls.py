from django.urls import path, include

urlpatterns = [
    path('articles', include('articles.urls')),
    path('comments', include('comments.urls')),
    path('users', include('users.urls')),
]
