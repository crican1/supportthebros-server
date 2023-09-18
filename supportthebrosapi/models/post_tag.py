from django.db import models
from .post import Post
from .tag import Tag

class PostTag(models.Model):

    organizer_post_id = models.ForeignKey(
      Post, on_delete=models.CASCADE, related_name='organizer_post_id')
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tag_id')
