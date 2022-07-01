a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.append(0)
for i in range(len(a) - 1, b[0], -1):
    a[i] = a[i - 1]
a[b[0]] = b[1]
print(*a)
