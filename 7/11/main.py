a = list(map(int, input().split()))
k = 1
for i in range(len(a) - 1):
    if a[i] < a[i + 1]:
        k += 1
print(k)
