from django.urls import path, include
from rest_framework import routers

from .views import CRUDPhotoViewSet, DestroyAdminAll

router = routers.DefaultRouter()

router.register("gallery", CRUDPhotoViewSet, basename="gallery")

urlpatterns = [
    path("", include(router.urls), name="api"),
    path("destroy", DestroyAdminAll.as_view()),
]