# transakcje/admin.py

from django.contrib import admin
from .models import Kategoria, Transakcja

# Rejestracja modeli w panelu administratora
admin.site.register(Kategoria)
admin.site.register(Transakcja)

