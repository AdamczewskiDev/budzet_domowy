# transakcje/urls.py

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import KategoriaViewSet, TransakcjaViewSet, register_user

router = DefaultRouter()
router.register(r'kategorie', KategoriaViewSet)      # Ścieżka dla kategorii
router.register(r'transakcje', TransakcjaViewSet)    # Ścieżka dla transakcji

urlpatterns = [
    path('register/', register_user, name='register'),  # Endpoint rejestracji
]

urlpatterns += router.urls
