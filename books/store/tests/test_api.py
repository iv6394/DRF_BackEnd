from urllib import response
from rest_framework.test import APITestCase
from django.urls import reverse

class BooksApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('book-list')
        print(url)
        response = self.client.get(url)
        print(response)