### Zadatak 4. Odredi izlaz koji bi generisao svaki od sledećih programskih fragmenata:
for i in range(1, 11):
    print(i * i)

print("--------------------")

for i in [1,3,5,7,9]:
    print(i, ":", i ** 3)
    print(i)

print("--------------------")

x = 2
y = 10
for j in range(0, y, x):
    print(j)
    print(x + y)
    print("done")

print("--------------------")

ans = 0
for i in range(1, 11):
    ans = ans + i * i
    print(i)

print(ans)
print("--------------------")