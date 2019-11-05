from django.db   import models
from user.models import User

class Article(models.Model):
    category   = models.ForignKey(ArticleCategory,on_delete=models.PROTECT)
    tags       = models.ManyToManyField(Tag, blank=True, on_delete=models.PROTECT)
    title      = models.CharField(max_length=300)
    thumb_img  = models.CharField(max_length=2500)
    content    = models.TextField()
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'articles'


class ArticleCategory(models.Model):
    name = models.CharField(max_length=150)
    
    class Meta:
        db_table = 'article_categories'


class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tag

    class Meta:
        db_table = 'style_tags'


class Like(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    article    = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'likes'
