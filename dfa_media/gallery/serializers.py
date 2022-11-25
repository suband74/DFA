from rest_framework import serializers

from .models import PhotoCollection


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoCollection
        fields = "__all__"


class CreateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoCollection
        fields = ("file", )