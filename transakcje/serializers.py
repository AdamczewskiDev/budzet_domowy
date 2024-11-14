# transakcje/serializers.py

from rest_framework import serializers
from .models import Kategoria, Transakcja

class KategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategoria
        fields = ['id', 'nazwa']  # Pola, które będą serializowane


class TransakcjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transakcja
        fields = ['id', 'kategoria', 'kwota', 'data', 'opis']
