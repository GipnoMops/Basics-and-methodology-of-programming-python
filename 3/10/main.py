sum = 0
chislo = 1
k = 0
while chislo != 0:
    chislo = int(input())
    if chislo % 2 == 0:
        k += 1
print(k - 1)
