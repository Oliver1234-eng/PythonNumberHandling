### Zadatak 9. Prodavnica kafe prodaje kafu za 105 dinara za kilogram. Za kućnu dostavu naplaćuje se
### 18 dinara po kilogramu i 15 dinara fiksnih troškova. Napiši program koji izračunava ukupnu cenu kućne
### porudžbine.
# Unos količine kafe u kg
kolicina = float(input("Unesite kolicinu kafe u kg: "))

# Izračunavanje cene kafe i dostave
cena_kg = 105
cena_dostave = 18 * kolicina + 15

# Izračunavanje ukupne cene
ukupna_cena = cena_kg * kolicina + cena_dostave

# Ispis rezultata
print("Ukupna cena porudzbine je: ", ukupna_cena, "dinara")