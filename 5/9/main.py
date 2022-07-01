from math import sqrt


def MinDivisor(n):
    global i
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return i
        else:
            i += 1
    return n


n = int(input())
print(MinDivisor(n))
