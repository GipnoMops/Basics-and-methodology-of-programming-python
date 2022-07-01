a = list(map(int, input().split()))
b = []
for i in range(len(a) - 1, -1, -1):
    b.append(a[i])
print(*b)
