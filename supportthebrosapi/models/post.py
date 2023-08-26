from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=65)
    post_image = models.URLField()
    post_content = models.CharField(max_length=2000)
    goal = models.IntegerField()
    created_on = models.DateTimeField(null=True, blank=True)
    uid = models.CharField(max_length=50)
