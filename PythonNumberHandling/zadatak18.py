### Zadatak 18. Napiši program koji izračunava prosek brojeva koje unosi korisnik (slično prethodnom zadatku). 
### Prosek bi trebalo da bude float.
broj_brojeva = int(input("Unesite broj brojeva: "))
suma = 0
for i in range(broj_brojeva):
    broj = float(input("Unesite {}. broj: ".format(i+1)))
    suma += broj

prosek = suma / broj_brojeva

print("Prosek unetih brojeva iznosi: {:.2f}".format(prosek))