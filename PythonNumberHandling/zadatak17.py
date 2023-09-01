### Zadatak 17. Napiši program koji izračunava zbir brojeva koje unosi korisnik. Prvo je potrebno uneti
### broj brojeva koje treba sabrati. Potom treba uneti sve brojeve i na kraju ispisati vrednost zbira.
n = int(input("Unesite broj brojeva za sabiranje: "))
suma = 0
for i in range(n):
    broj = int(input("Unesite {}. broj: ".format(i+1)))
    suma += broj

print("Zbir brojeva je: ", suma)
