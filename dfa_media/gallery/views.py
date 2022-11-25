import os
import shutil
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import PhotoCollection
from .serializers import ImageSerializer, CreateImageSerializer
from .permissions import IsOwnerOrReadOnly


class CustomCreateModelMixin:
    """
    Create a model instance.
    """

    def create(self, request, *args, **kwargs):

        serializer = CreateImageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        photo_data = serializer.validated_data
        ins = PhotoCollection.objects.create(
            **photo_data,
            owner=request.user,
        )
        data = ImageSerializer(ins).data

        return Response(
            data=data,
            status=status.HTTP_201_CREATED,
        )


class CustomDestroyModelMixin:
    """
    Destroy a model instance.
    """
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        file = "dfa_media/" + instance.file.url
        os.remove(file)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class CRUDPhotoViewSet(
    CustomCreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    CustomDestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = PhotoCollection.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class DestroyAdminAll(APIView):

    permission_classes = [IsAdminUser]

    def delete(self, request, *args, **kwargs):
        PhotoCollection.objects.all().delete()
        try:
            shutil.rmtree("dfa_media/media")
        except OSError:
            Response("There is no such directory")

        return Response({"Message": "image deleted"})
