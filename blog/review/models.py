from django.db import models
from post.models import User, Post

# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add - показывает времясоздания коомента
    updated_at = models.DateTimeField(auto_now=True)
    #auto_now - показывает время изменения коомента