from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class TestSampleApi(APITestCase):

    def test_testing(self):
        response = self.client.get(reverse("test"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)


