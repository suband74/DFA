from unittest.mock import MagicMock
from django.core.files import File
from rest_framework import status
from rest_framework.test import APITestCase
# from rest_framework.authtoken.models import Token
# from rest_framework.test import APIClient
from .models import User, PhotoCollection


class PhotoTest(APITestCase):

    def setUp(self) -> None:
        
        file_mock = MagicMock(spec=File)
        file_mock.name = "photo_for_test.jpg"

        file_mock2 = MagicMock(spec=File)
        file_mock2.name = "photo_for_test_2.jpg"

        us1 = User.objects.create(username = "nemo", password = "1234567*")
        us1.save()
        us2 = User.objects.create(username = "mane", password = "1234567*")
        us2.save()

        self.client.force_authenticate(user=us1)

        self.photo1 = PhotoCollection.objects.create(owner = us1, file = file_mock.name)
        self.photo2 = PhotoCollection.objects.create(owner = us2, file = file_mock2.name)


    # def test_photolist(self):
    #     response = self.client.get("/api/v1/gallery/")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 2)
    #     self.assertTrue({"id": 1, "file": 'http://testserver/media/photo.jpg', "owner": 1} in response.data)


    def test_currient(self):
        response = self.client.get("/api/v1/currient")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)


    # def test_photo(self):
    #     response = self.client.get("/api/v1/gallery/1/")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, {"id": 1, "file": 'http://testserver/media/photo.jpg', "owner": 1})
