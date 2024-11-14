# transakcje/models.py

from django.db import models
from django.contrib.auth.models import User

class Kategoria(models.Model):
    użytkownik = models.ForeignKey(User, on_delete=models.CASCADE)  # Przypisanie użytkownika do kategorii
    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa


class Transakcja(models.Model):
    użytkownik = models.ForeignKey(User, on_delete=models.CASCADE)  # Przypisanie użytkownika do transakcji
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    kwota = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    opis = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.kwota} PLN - {self.kategoria.nazwa} - {self.data}"
