from math import sqrt
chislo = 1
n = -1
sum = 0
sumkv = 0
while chislo != 0:
    chislo = int(input())
    n += 1
    sum += chislo
    sumkv += chislo ** 2
otvet = sqrt((sumkv - sum * sum / n) / (n - 1))
print(otvet)
