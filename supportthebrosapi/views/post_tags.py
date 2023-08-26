from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from supportthebrosapi.models import Post, Tag, PostTag

class PostTagView(ViewSet):
    """Rare post_tags view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single post_tag
        Returns:
            Response -- JSON serialized post_tag
        """
        try:
            post_tag = PostTag.objects.get(pk=pk)
            serializer = PostTagSerializer(post_tag)
            return Response(serializer.data)
        except PostTag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all post_tags

        Returns:
            Response -- JSON serialized list of post_tags
        """
        post_tag = PostTag.objects.all()

        serializer = PostTagSerializer(post_tag, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized post_tag instance
        """
        organizer_post_id = Post.objects.get(pk=request.data["organizer_post_id"])
        tag_id = Tag.objects.get(pk=request.data["tag_id"])

        post_tag = PostTag.objects.create(
            organizer_post_id=organizer_post_id,
            tag_id=tag_id,
        )

        serializer = PostTagSerializer(post_tag)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        """Delete post_tags
        """
        post_tag = PostTag.objects.get(pk=pk)
        post_tag.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class PostTagSerializer(serializers.ModelSerializer):
    """JSON serializer for post_tags"""
    class Meta:
        model = PostTag
        fields = ('id', 'organizer_post_id', 'tag_id')
        depth = 1
