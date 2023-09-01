### Zadatak 5. Napiši program koji izračunava zapreminu i površinu sfere za dati poluprečnik. Zapremina
### sfere se izračunava kao
### V = 4 / 3 * Pi * r ** 3, a površina kao A = 4 * Pi * r ** 2

import math

# Unos poluprecnika od korisnika
r = float(input("Unesite poluprecnik sfere: "))

# Računanje zapremine sfere
V = (4 / 3) * math.pi * r ** 3

# Računanje površine sfere
P = 4 * math.pi * r ** 2

# Ispis rezultata
print("Zapremina sfere je:", round(V, 2))
print("Povrsina sfere je:", round(P, 2))