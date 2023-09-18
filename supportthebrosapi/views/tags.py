from datetime import datetime
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from supportthebrosapi.models import Tag

class TagView(ViewSet):
    """Supportthebros tags view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single tag
        Returns:
            Response -- JSON serialized tag
        """
        try:
            tag = Tag.objects.get(pk=pk)
            serializer = TagSerializer(tag)
            return Response(serializer.data)
        except Tag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all tags

        Returns:
            Response -- JSON serialized list of tags
        """
        tag = Tag.objects.all()
        serializer = TagSerializer(tag, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized Post instance
        """

        tag = Tag.objects.create(
            title=request.data["title"],
        )
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a tag

        Returns:
        Response -- Empty body with 204 status code
        """

        tag = Tag.objects.get(pk=pk)
        tag.title=request.data["title"],
        tag.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Delete Tag
        """
        tag = Tag.objects.get(pk=pk)
        tag.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class  TagSerializer(serializers.ModelSerializer):
    """JSON serializer for posts
    """
    class Meta:
        model = Tag
        fields = ('id', 'title')
        depth = 1
