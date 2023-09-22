from django.db import models
from .post import Post
from .user import User

class Comment(models.Model):

    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    auhtor_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=1000)
    created_on = models.DateTimeField(null=True, blank=True)
    uid = models.CharField(max_length=50)
