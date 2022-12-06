from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from api.models import Category


class CategoryTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_user_email = "test_user1@example.com"
        cls.test_user_password = "123456789"
        test_user1 = get_user_model().objects.create(email="test_user1@example.com")
        test_user1.set_password(cls.test_user_password)
        test_user1.save()

        cls.data_create = {
            "name": "category name",
        }

        cls.data_update = {
            "name": "update category",
        }

    def setUp(self):
        token_url = reverse("token_obtain_pair")
        credentials = {
            "email": self.test_user_email,
            "password": self.test_user_password,
        }
        response = self.client.post(token_url, credentials, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + response.data["access"])

    def test_category_create(self):
        url = reverse("api:category-list", kwargs={"user_pk": 1})
        response = self.client.post(url, self.data_create, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_category_update(self):
        self.test_category_create()
        url = reverse("api:category-detail", kwargs={"user_pk": 1, "pk": 1})
        response = self.client.put(url, self.data_create, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
