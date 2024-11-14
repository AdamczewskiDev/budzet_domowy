# transakcje/views.py

from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum

from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Kategoria, Transakcja
from .serializers import KategoriaSerializer, TransakcjaSerializer



@api_view(['GET'])
def home(request):
    return Response({"message": "Witamy w aplikacji Budżet Domowy API. Użyj /api/ do dostępu do zasobów."})
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Tylko dla zalogowanych użytkowników
def statystyki(request):
    total_expenses = Transakcja.objects.filter(
        użytkownik=request.user,
        kwota__lt=0  # Zakładając, że wydatki mają ujemną kwotę
    ).aggregate(total=Sum('kwota'))['total'] or 0

    total_income = Transakcja.objects.filter(
        użytkownik=request.user,
        kwota__gt=0  # Zakładając, że przychody mają dodatnią kwotę
    ).aggregate(total=Sum('kwota'))['total'] or 0

    return Response({
        "wydatki": total_expenses,
        "przychody": total_income,
    })


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
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Kategoria.objects.filter(użytkownik=self.request.user)  # Filtruje kategorie zalogowanego użytkownika

    def perform_create(self, serializer):
        serializer.save(użytkownik=self.request.user)  # Ustawia zalogowanego użytkownika jako właściciela


# Widok dla transakcji budżetu (CRUD)
class TransakcjaViewSet(viewsets.ModelViewSet):
    queryset = Transakcja.objects.all()               # Pobiera wszystkie obiekty transakcji
    serializer_class = TransakcjaSerializer           # Serializator dla transakcji
    permission_classes = [IsAuthenticated]
    
    # Konfiguracja filtrowania
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['kategoria', 'data']   # Filtruj po kategorii i dacie
    ordering_fields = ['kwota', 'data']        # Sortuj po kwocie i dacie
    search_fields = ['opis']                   # Szukaj w polu "opis"
    
    def get_queryset(self):
        return Transakcja.objects.filter(użytkownik=self.request.user)  # Filtruje transakcje zalogowanego użytkownika

    def perform_create(self, serializer):
        serializer.save(użytkownik=self.request.user)  # Ustawia zalogowanego użytkownika jako właściciela
