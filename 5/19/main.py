def Summ(n):
    n = int(input())
    if n != 0:
        return n + Summ(n)
    return n


print(Summ(1))
