n = int(input())
poteryashka = n * (n + 1) // 2
for i in range(n - 1):
    m = int(input())
    poteryashka -= m
print(poteryashka)
