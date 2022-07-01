a = list(map(int, input().split()))
max = [a[0], 0]
for i in range(len(a)):
    if max[0] <= a[i]:
        max[0] = a[i]
        max[1] = i
print(*max)
