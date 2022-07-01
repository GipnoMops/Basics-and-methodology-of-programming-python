def faktorial(n):
    if n == 1:
        return 1
    return n * faktorial(n - 1)


n = int(input())
summ = 0
for i in range(1, n + 1):
    summ += faktorial(i)
print(summ)
