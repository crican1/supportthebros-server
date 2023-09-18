from django.db import models
from .tag import Tag

class Post(models.Model):

    title = models.CharField(max_length=65)
    post_image = models.URLField()
    post_content = models.CharField(max_length=2000)
    goal = models.CharField(max_length=1000000)
    created_on = models.DateTimeField(null=True, auto_now=True)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    uid = models.CharField(max_length=50)
