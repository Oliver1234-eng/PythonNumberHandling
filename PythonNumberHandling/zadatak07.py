### Zadatak 7. Napiši program koji izračunava molekularnu masu molekula ugljovodonika zavisno od broja
### atoma ugljenika i vodonika koji ga čine. Mase atoma su sledeće:
### atom    masa
###  H     1.0079
###  C     12.011

# Unosimo broj atoma ugljenika i vodonika u molekulu
broj_C = int(input("Unesite broj atoma ugljenika: "))
broj_H = int(input("Unesite broj atoma vodonika: "))

# Računamo masu molekula
masa_C = 12.011
masa_H = 1.0079
masa_molekula = broj_C * masa_C + broj_H * masa_H

# Ispisujemo dobijenu masu
print("Molekularna masa molekula je:", round(masa_molekula, 2))