### Zadatak 15. Napiši program koji izračunava zbir prvih n prirodnih brojeva, gde se n unosi sa tastature.
n = int(input("Unesite n: "))
zbir = 0
for i in range(1, n + 1):
    zbir += i

print("Zbir prvih", n, "prirodnih brojeva je", zbir)