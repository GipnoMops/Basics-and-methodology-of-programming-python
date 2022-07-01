n = 1
m = int(input())
chislo = 0
perevernutoe = 0
k = 1
l = 1
K = 0
while n <= m:
    k = 1
    l = 1
    perevernutoe = 0
    while n // (10 ** k):
        k += 1
    while l <= k:
        chislo = (n % (10 ** l) - n % (10 ** (l - 1))) // (10 ** (l - 1))
        l += 1
        perevernutoe += chislo * (10 ** (k - l + 1))
    if n == perevernutoe:
        K += 1
        n += 1
    else:
        n += 1
print(K)
