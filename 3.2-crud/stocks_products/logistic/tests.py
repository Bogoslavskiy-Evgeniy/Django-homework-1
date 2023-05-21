from unittest import TestCase
from rest_framework.test import APIClient

class TestSampleView(TestCase):
    def test_sample_view(self):
        client = APIClient()
        url = '/api/v1/test/'
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
