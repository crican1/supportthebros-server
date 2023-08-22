from django.db import models

class Comment(models.Model):

    post_id = models.IntegerField()
    comment_content = models.CharField(max_length=1000)
    created_on = models.DateTimeField(null=True, blank=True)
    uid = models.CharField(max_length=50)
