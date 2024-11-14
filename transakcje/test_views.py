# transakcje/test_views.py

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Kategoria, Transakcja
from decimal import Decimal
from datetime import date


class UserTests(APITestCase):
    def test_user_registration(self):
        """
        Test rejestracji nowego użytkownika.
        """
        url = reverse('register')
        data = {"username": "testuser", "password": "testpassword"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "testuser")

    def test_user_login(self):
        """
        Test logowania użytkownika i uzyskania tokenu.
        """
        # Najpierw utwórz użytkownika
        user = User.objects.create_user(username="testuser", password="testpassword")
        url = reverse('token_obtain_pair')
        data = {"username": "testuser", "password": "testpassword"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)


class KategoriaTests(APITestCase):
    def setUp(self):
        # Tworzenie użytkownika i uzyskanie tokenu przed testami
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {"username": "testuser", "password": "testpassword"}, format='json')
        self.access_token = response.data["access"]
        
        # Dodanie tokenu do nagłówków autoryzacyjnych
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_create_kategoria(self):
        """
        Test tworzenia nowej kategorii.
        """
        url = reverse('kategoria-list')
        data = {"nazwa": "Jedzenie", "użytkownik": self.user.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Kategoria.objects.count(), 1)
        self.assertEqual(Kategoria.objects.get().nazwa, "Jedzenie")


class TransakcjaTests(APITestCase):
    def setUp(self):
        # Tworzenie użytkownika i uzyskanie tokenu
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {"username": "testuser", "password": "testpassword"}, format='json')
        self.access_token = response.data["access"]

        # Dodanie tokenu do nagłówków autoryzacyjnych
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # Tworzenie kategorii
        self.kategoria = Kategoria.objects.create(nazwa="Transport", użytkownik=self.user)

    def test_create_transakcja(self):
        """
        Test tworzenia nowej transakcji.
        """
        url = reverse('transakcja-list')
        data = {
            "kategoria": self.kategoria.id,
            "kwota": Decimal("-15.00"),
            "data": date.today(),
            "opis": "Bilet autobusowy"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transakcja.objects.count(), 1)
        self.assertEqual(Transakcja.objects.get().opis, "Bilet autobusowy")

    def test_get_transakcje(self):
        """
        Test pobierania listy transakcji użytkownika.
        """
        Transakcja.objects.create(
            użytkownik=self.user,
            kategoria=self.kategoria,
            kwota=Decimal("-15.00"),
            data=date.today(),
            opis="Bilet autobusowy"
        )
        url = reverse('transakcja-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["opis"], "Bilet autobusowy")
