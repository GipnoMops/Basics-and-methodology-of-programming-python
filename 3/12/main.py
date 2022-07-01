k = 0
i = 0
chislo1 = 1
chislo2 = 1
while chislo1 != 0:
    chislo1 = int(input())
    if (chislo1 > chislo2) and (i > 0):
        k += 1
        i += 1
        chislo2 = chislo1
    else:
        chislo2 = chislo1
        i += 1
print(k)
