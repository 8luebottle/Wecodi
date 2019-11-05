from django.db      import models
from articles.models import Article
from users.models    import User

class Comment(models.Model):
    article    = models.ForeignKey(Article, on_delete=models.CASCADE)
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    comment    = models.TextField()
    deleted    = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'
