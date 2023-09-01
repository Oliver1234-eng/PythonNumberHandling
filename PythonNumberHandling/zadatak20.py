### Zadatak 20. Fibonačijev niz brojeva je niz kod koga svaki broj predstavlja zbir prethodna dva. Ovaj
### niz počinje sa 1, 1, 2, 3, 5, 8, 13, ... Napiši program koji izračunava n-ti Fibonačijev broj gde n unosi
### korisnik. Fibonačijevi brojevi rastu vrlo brzo, program mora da rukuje vrlo velikim brojevima.
n = int(input("Unesite redni broj Fibonacijevog broja: "))
def fib(n):
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for i in range(3, n+1):
        c = a + b
        a, b = b, c
    return b

print("Fibonacijev broj na poziciji {} je {}".format(n, fib(n)))