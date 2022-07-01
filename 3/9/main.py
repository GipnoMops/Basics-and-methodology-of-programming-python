sum = 0
chislo = 1
k = 0
while chislo != 0:
    k += 1
    chislo = int(input())
    sum += chislo
print(sum / (k - 1))
