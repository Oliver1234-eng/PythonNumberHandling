### Zadatak 13. Napiši program koji izračunava površinu trougla za date dužine stranica a, b i c. s = (a+b+c) / 2,
### A = sqrt(s(s - a)(s - b)(s - c))
import math

def povrsina_trougla(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        povrsina = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return povrsina
    else:
        raise ValueError("Duzine stranica ne odgovaraju pravilu trougla")

# primer upotrebe
a = float(input("Unesite duzinu prve stranice trougla: "))
b = float(input("Unesite duzinu druge stranice trougla: "))
c = float(input("Unesite duzinu trece stranice trougla: "))

try:
    print("Povrsina trougla iznosi: ", round(povrsina_trougla(a, b, c), 2))
except ValueError as e:
    print("Greska: ", e)