### Zadatak 14. Napiši program koji izračunava dužinu merdevina za datu visinu koju treba dostići i ugao
### kojim se meri nagib merdevina. d = visina / sin(ugao)
import math

# unos podataka od korisnika
visina = float(input("Unesite visinu koju treba dostici: "))
ugao = float(input("Unesite ugao merdevina: "))

# konvertovanje ugla iz stepeni u radijane
ugao_r = math.radians(ugao)

# izračunavanje dužine merdevina
duzina = visina / math.sin(ugao_r)

# ispisivanje rezultata
print("Potrebna duzina merdevina iznosi {:.2f} metara.".format(duzina))