### Zadatak 6. Napiši program koji izračunava cenu pice po kvadratnom centimetru za dati poluprečnik i
### cenu cele pice. A = r ** 2 * Pi
import math

# Unos podataka
poluprecnik = float(input("Unesite poluprecnik pice (u cm): "))
cena = float(input("Unesite cenu cele pice (u dinarima): "))

# Računanje površine pice
povrsina = poluprecnik ** 2 * math.pi

# Računanje cene po cm^2
cena_po_cm2 = cena / povrsina

# Ispis rezultata
print("Cena po kvadratnom centimetru je: ", round(cena_po_cm2, 2), "din/cm^2")