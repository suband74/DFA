from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PhotoCollection(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец фото"
    )
    file = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Фото")

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def __str__(self) -> str:
        return f"{self.owner}"