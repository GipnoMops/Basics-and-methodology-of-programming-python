a = list(map(int, input().split()))
b = [100000]
for i in range(len(a)):
    if b[0] > a[i] > 0:
        b[0] = a[i]
print(*b)
