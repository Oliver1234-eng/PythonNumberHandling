### Zadatak 16. Napiši program koji izračunava zbir kvadrata prvih n prirodnih brojeva, gde se n unosi sa tastature.
n = int(input("Unesite n: "))
suma_kvadrata = 0

for i in range(1, n+1):
    suma_kvadrata += i**2

print("Zbir kvadrata prvih", n, "prirodnih brojeva je", suma_kvadrata)