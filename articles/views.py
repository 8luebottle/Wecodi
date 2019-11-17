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

class ArticleView(View): # New Post  | # Show All Articles (Pagination) 
    pass


class ArticleDetailView(View):
    pass


class ArticleSegmentationView(View): # By. Tags & Categories
    pass


class AtricleCategoryView(View):
    pass


class ArticleDeleteView(View): # Delete Article
    pass


class ClickCountView(View): # Click Tracing in Articles
    pass


class LikeView(View):
    pass


class LikeCountView(View): # How many Likes
    pass
