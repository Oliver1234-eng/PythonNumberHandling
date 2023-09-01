### Zadatak 8. Napiši program koji određuje udaljenost posmatrača od munje na bazi vremenske razlike
### trenutka pojavljivanja munje i trenutka kada zvuk stigne do posmatrača. Brzina zvuka iznosi 340 m/s.
v = 340  # brzina zvuka u m/s
t = float(input("Unesite vremensku razliku u sekundama: "))
d = v * t
print("Udaljenost posmatraca od munje je: ", d, "metara")