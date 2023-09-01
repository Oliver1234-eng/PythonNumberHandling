### Zadatak 19. Napiši program koji izračunava aproksimaciju broja Pi kao delimičnu sumu ovog reda:
### 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ... Program treba da zatraži broj članova ovog niza koje treba sabrati.
def pi_aprox(n):
    pi_sum = 0
    sign = 1
    for i in range(n):
        denom = 2 * i + 1
        pi_sum += sign * 4 / denom
        sign *= -1
    return pi_sum

n = int(input("Unesite broj clanova reda: "))
print("Aproksimacija broja Pi iznosi:", pi_aprox(n))