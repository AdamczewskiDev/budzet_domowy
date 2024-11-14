# transakcje/views.py

from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Kategoria, Transakcja
from .serializers import KategoriaSerializer, TransakcjaSerializer

@api_view(['GET'])
def home(request):
    return Response({"message": "Witamy w aplikacji Budżet Domowy API. Użyj /api/ do dostępu do zasobów."})


# Widok rejestracji użytkownika
@api_view(['POST'])
@permission_classes([AllowAny])  # Pozwala na dostęp bez uwierzytelnienia
def register_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Sprawdza, czy użytkownik o danej nazwie już istnieje
        if User.objects.filter(username=username).exists():
            return Response({"error": "Użytkownik już istnieje"}, status=status.HTTP_400_BAD_REQUEST)

        # Tworzy nowego użytkownika
        user = User.objects.create_user(username=username, password=password)
        user.save()

        return Response({"message": "Użytkownik został utworzony"}, status=status.HTTP_201_CREATED)


# Widok dla kategorii budżetu (CRUD)
class KategoriaViewSet(viewsets.ModelViewSet):
    queryset = Kategoria.objects.all()                # Pobiera wszystkie obiekty kategorii
    serializer_class = KategoriaSerializer            # Serializator dla kategorii


# Widok dla transakcji budżetu (CRUD)
class TransakcjaViewSet(viewsets.ModelViewSet):
    queryset = Transakcja.objects.all()               # Pobiera wszystkie obiekty transakcji
    serializer_class = TransakcjaSerializer           # Serializator dla transakcji
