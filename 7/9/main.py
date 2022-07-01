a = list(map(int, input().split()))
b = 0
k = 0
for i in range(len(a)):
    if k == 0 and a[i] % 2 != 0:
        b = a[i]
        k += 1
    if a[i] % 2 != 0:
        if a[i] < b:
            b = a[i]
print(b)
