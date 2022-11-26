from rest_framework import serializers

from .models import PhotoCollection, User


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoCollection
        fields = "__all__"


class CreateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoCollection
        fields = ("file", )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name")
