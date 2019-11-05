from django.db import models

class User(models.Model):
    email       = models.EmailField(max_length=50)
    password    = models.CharField(max_length=200, null=True)
    first_name  = models.CharField(max_length=20)
    last_name   = models.CharField(max_length=20)
    social_id   = models.CharField(max_length=100, null=True)
    is_admin    = models.BooleanField(default=False)
    is_blocked  = models.BooleanField(default=False)
    deleted     = models.BooleanField(default=False)
    visit_count = models.IntegerField(default=0)
    last_login  = models.DateTimeField(blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

class Profile(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname    = models.CharField(max_length=50)
    bio         = models.CharField(max_length=254)
    profile_img = models.CharField(max_length=500, default=None, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'profiles'

