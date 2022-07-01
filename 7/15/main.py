a = list(map(int, input().split()))
last = a[-1]
for i in range(len(a) - 1):
    a[len(a) - 1 - i] = a[len(a) - i - 2]
a[0] = last
print(*a)
