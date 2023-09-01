### Zadatak 12. Epakt predstavlja starost meseca u danima na dan 1. januara. Koristi se za izračunavanje
### termina Uskrsa. Gregorijanski epakt se izračunava po sledećim formulama (int aritmetika):
### C = year / 100
### epakt = (8 + C / 4 - C + ((8C + 13) / 25) + 11(year%19))%30
### Napiši program koji od korisnika traži godinu kao 4-cifreni broj i izračunava epakt po gregorijanskom kalendaru.
year = int(input("Unesite godinu: "))
C = year / 100
epakt = (8 + C / 4 - C + ((8 * C + 13) / 25) + 11 * (year % 19)) % 30
print("Gregorijanski epakt za godinu", year, "iznosi:", epakt)