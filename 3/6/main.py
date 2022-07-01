n = int(input())
i = 1
k = 0
while i <= n:
    if i == n or n == 1:
        i *= 2
    elif i <= n:
        i *= 2
        k += 1
print(k)
