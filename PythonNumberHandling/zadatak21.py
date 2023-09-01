### Zadatak 21. Paket math sadrži funkciju za izračunavanje kvadratnog korena. Potrebno je napisati
### sopstvenu funkciju za izračunavanje kvadratnog korena pomocu PiP („probaj-i-ponovo“) pristupa. Prvo
### pokušamo da pogodimo vrednost korena i uporedimo je sa pravom vrednošcu (koju vraća sqrt). Onda
### napravimo sledeći pokušaj i približimo se rešenju. Postupak ponavljamo dok ne naiđemo na pravu
### vrednost korena ili njenu dovoljno dobru aproksimaciju. Za ovaj posao možemo koristiti Njutnov metod.
### Neka je x broj ciji koren tražimo, i guess broj kojim pokušavamo da pogodimo koren. Pokušaj se
### može popraviti korišcenjem vrednosti (guess + x / guess) / 2 u sledećem krugu. Napiši program koji implementira
### Njutnov metod. Program od korisnika traži broj čiji koren tražimo (x) i broj pokušaja. Početna vrednost
### za pokušaj je x=2. Na kraju rada ispisati dobijenu vrednost Njutnovom metodom i vrednost koju vraca sqrt.
import math

def newton_sqrt(x, n):
    guess = x / 2
    for i in range(n):
        guess = (guess + x / guess) / 2
    return guess

x = float(input("Unesite broj ciji koren trazite: "))
n = int(input("Unesite broj pokusaja: "))

approx_sqrt = newton_sqrt(x, n)
true_sqrt = math.sqrt(x)

print("Njutnovom metodom dobijen koren broja {} je {:.5f}.".format(x, approx_sqrt))
print("Prava vrednost korena broja {} je {:.5f}.".format(x, true_sqrt))