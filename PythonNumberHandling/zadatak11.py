### Zadatak 11. Za dve tačke u ravni (vidi prethodni zadatak) izračunati rastojanje između njih. 
### d = sqrt((x2 - x1)2 + (y2 - y1)2)
import math

# učitavanje koordinata tačaka od korisnika
x1 = float(input("Unesite x koordinatu prve tacke: "))
y1 = float(input("Unesite y koordinatu prve tacke: "))
x2 = float(input("Unesite x koordinatu druge tacke: "))
y2 = float(input("Unesite y koordinatu druge tacke: "))

# računanje rastojanja između tačaka
d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# ispis rastojanja
print("Rastojanje izmedju tacaka ({}, {}) i ({}, {}) je {:.2f}.".format(x1, y1, x2, y2, d))