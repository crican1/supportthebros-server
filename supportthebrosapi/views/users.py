from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from supportthebrosapi.models import User
class UserView(ViewSet):

    def retrieve(self, request, pk):

        user= User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        data = serializer.data

        return Response(data)

    def list(self,request):

        users = User.objects.all()
        user = request.query_params.get('user', None)
        if user is not None:
            users = users.filter(user_id = user)

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        """POST request to create a rare user"""
        uid=request.data["uid"]
        name=request.data["name"]
        profile_image_url=request.data["profile_image_url"]
        email=request.data["email"]
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(uid=uid)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """PUT request to update a rare user"""
        user = User.objects.get(pk=pk)
        uid=request.data.get("uid", user.uid)
        name=request.data.get("name", user.name)
        profile_image_url=request.data["profile_image_url"]
        email=request.data["email"]
        user.uid = uid
        user.name = name
        user.save()
        return Response({'message': 'User Updated'}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """DELETE request to destroy a rare user"""
        user = User.objects.get(pk=pk)
        user.delete()
        return Response({'message': 'User Destroyed'}, status=status.HTTP_204_NO_CONTENT)

class  UserSerializer(serializers.ModelSerializer):
    """JSON serializer for user
    """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'profile_image_url', 'email', 'uid')
        depth = 1
