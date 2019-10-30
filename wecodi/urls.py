from django.urls import path, include

urlpatterns = [
    path('article', include('article.urls')),
    path('comment', include('comment.urls')),
    path('user', include('user.urls')),
]
