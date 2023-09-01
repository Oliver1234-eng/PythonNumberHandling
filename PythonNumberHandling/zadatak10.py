### Zadatak 10. Dve tačke u ravni date su koordinatama (x1; y1) i (x2; y2). Napiši program koji izračunava
### nagib prave koja prolazi kroz date tacke. m = (y2 - y1) / (x2 - x1)
x1 = float(input("Unesite x-koordinatu tacke 1: "))
y1 = float(input("Unesite y-koordinatu tacke 1: "))
x2 = float(input("Unesite x-koordinatu tacke 2: "))
y2 = float(input("Unesite y-koordinatu tacke 2: "))

# Izracunavanje nagiba prave
nagib = (y2 - y1) / (x2 - x1)

# Ispisivanje rezultata
print("Nagib prave je:", round(nagib, 2))