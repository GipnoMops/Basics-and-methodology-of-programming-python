a = list(map(int, input().split()))
for i in range(len(a) // 2):
    b = a[len(a) - 1 - i]
    a[len(a) - 1 - i] = a[i]
    a[i] = b
print(*a)
