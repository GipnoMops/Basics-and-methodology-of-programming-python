chislo1 = 1
chislo2 = 0
max1 = 0
max2 = 0
while chislo1 != 0:
    chislo2 = chislo1
    chislo1 = int(input())
    if chislo2 == chislo1:
        max2 += 1
    elif max2 > max1:
        max1 = max2
    else:
        max2 = 1
    if chislo2 != chislo1:
        max2 = 1
print(max1)
