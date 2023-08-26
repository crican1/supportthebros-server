from datetime import datetime
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from supportthebrosapi.models import Post

class PostView(ViewSet):
    """Supportthebros posts view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single post
        Returns:
            Response -- JSON serialized post
        """
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all posts

        Returns:
            Response -- JSON serialized list of posts
        """
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized Post instance
        """

        post = Post.objects.create(
            title=request.data["title"],
            postt_image=request.data["post_image"],
            post_content=request.data["post_content"],
            goal=request.data["goal"],
            created_one=datetime.now(),
            uid=request.data["uid"]
        )
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a postt

        Returns:
        Response -- Empty body with 204 status code
        """

        post = Post.objects.get(pk=pk)
        post.title=request.data["title"],
        post.post_image=request.data["post_image"],
        post.post_content=request.data["post_content"],
        post.goal=request.data["goal"],
        post.created_one=datetime.now(),
        post.uid=request.data["uid"]
        post.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Delete Post
        """
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class  PostSerializer(serializers.ModelSerializer):
    """JSON serializer for posts
    """
    class Meta:
        model = Post
        fields = ('id', 'title', 'post_image', 'post_content', 'goal', 'created_on', 'uid')
        depth = 1
