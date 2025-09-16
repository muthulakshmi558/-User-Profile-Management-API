from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

class UserProfileTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", email="test@test.com", password="password123")
        response = self.client.post("/api/v1/token/", {"username": "testuser", "password": "password123"})
        self.token = response.data["access"]

    def test_unauthorized_access(self):
        response = self.client.get("/api/v1/profile/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_profile_v1_access(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        response = self.client.get("/api/v1/profile/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_v2_access(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        response = self.client.get("/api/v2/profile/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_throttle_limit(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        for i in range(6):  # exceed limit
            response = self.client.get("/api/v1/profile/")
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)
