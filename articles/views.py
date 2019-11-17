# A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z.

import json
import random

from django.http  import HttpResponse, JsonResponse
from django.views import Viewi

from users.utils.authority import requires_logged_in
from .models               import (
    Article, ArticleCategory, 
    Tag, Like
)

"""
ADMIN
    Write a post, delete a post, update a post
USER 
    Read a post(Show 5?)
"""

class ArticleView(View): # New Post  | Update Post
    pass


class ArticleDeleteView(View): # Delete Article
    pass
