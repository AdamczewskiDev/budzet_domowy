# init_data.py

import os
import django

# Ustawienia Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'budzet_domowy.settings')
django.setup()

from django.contrib.auth.models import User
from transakcje.models import Kategoria, Transakcja
from datetime import date
from decimal import Decimal

# Utworzenie użytkowników
user1, created = User.objects.get_or_create(username="user1")
user1.set_password("user1password")
user1.save()

user2, created = User.objects.get_or_create(username="user2")
user2.set_password("user2password")
user2.save()

# Utworzenie kategorii
kategoria1, _ = Kategoria.objects.get_or_create(nazwa="Jedzenie", użytkownik=user1)
kategoria2, _ = Kategoria.objects.get_or_create(nazwa="Transport", użytkownik=user1)
kategoria3, _ = Kategoria.objects.get_or_create(nazwa="Rozrywka", użytkownik=user2)

# Utworzenie transakcji
Transakcja.objects.get_or_create(
    użytkownik=user1, kategoria=kategoria1, kwota=Decimal('-25.00'), data=date(2024, 1, 5), opis="Zakupy spożywcze"
)
Transakcja.objects.get_or_create(
    użytkownik=user1, kategoria=kategoria2, kwota=Decimal('-15.00'), data=date(2024, 1, 6), opis="Bilet autobusowy"
)
Transakcja.objects.get_or_create(
    użytkownik=user2, kategoria=kategoria3, kwota=Decimal('-50.00'), data=date(2024, 1, 7), opis="Bilety do kina"
)

print("Przykładowi użytkownicy, kategorie i transakcje zostały dodane!")
