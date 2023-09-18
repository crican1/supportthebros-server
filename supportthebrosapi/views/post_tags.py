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
        organizer_post_id = request.query_params.get('organizerPostId', None)

        post_tag = PostTag.objects.all().filter(organizer_post_id=organizer_post_id)

        serializer = PostTagSerializer(post_tag, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized post_tag instance
        """
        organizer_post_id = Post.objects.get(pk=request.data["organizerPostId"])
        tag_id = Tag.objects.get(pk=request.data["tagId"])

        post_tag = PostTag.objects.create(
            organizer_post_id=organizer_post_id,
            tag_id=tag_id,
        )

        serializer = PostTagSerializer(post_tag)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handles PUT requests for post tags

        Returns:
            Response -- Empty body with 204 status code
        """
        post_tag = PostTag.objects.get(pk=pk)
        organizer_post_id = Post.objects.get(pk=request.data["organizerPostId"])
        tag_id = Tag.objects.get(pk=request.data["tagId"])

        post_tag.organizer_post_id = organizer_post_id
        post_tag.tag_id = tag_id
        post_tag.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handles DELETE requests for post tags

        Returns:
            Response -- Empty body with 204 status code
        """
        organizer_post_id = Post.objects.get(pk=pk)
        tag_id = request.query_params.get('tag_id', None)
        if tag_id is not None:
            # Filter the PostTag instances for the matching organizer_post_id and tag_id
            post_tag = PostTag.objects.get(organizer_post_id_id=organizer_post_id, tag_id=tag_id)

            if post_tag:
                # Delete the first matching post_tag instance
                post_tag.delete()
                return Response(None, status=status.HTTP_204_NO_CONTENT)

        return Response({"detail": "SessionEngineer not found"}, status=status.HTTP_404_NOT_FOUND)

class PostTagSerializer(serializers.ModelSerializer):
    """JSON serializer for post_tags"""
    class Meta:
        model = PostTag
        fields = ('id', 'organizer_post_id', 'tag_id')
        depth = 3
