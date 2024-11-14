# transakcje/models.py

from django.db import models

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa


class Transakcja(models.Model):
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    kwota = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    opis = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.kwota} PLN - {self.kategoria.nazwa} - {self.data}"
