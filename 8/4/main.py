a = list(map(int, input().split()))
max = [a[0], 0]
max2 = [a[0], 0]
for i in range(len(a)):
    if max[0] <= a[i]:
        max[0] = a[i]
        max[1] = i
for i in range(len(a)):
    if max2[0] <= a[i] and i != max[1]:
        max2[0] = a[i]
        max2[1] = i
min1 = [a[0], 0]
min2 = [a[0], 0]
for i in range(len(a)):
    if min1[0] >= a[i]:
        min1[0] = a[i]
        min1[1] = i
for i in range(len(a)):
    if min2[0] >= a[i] and i != min1[1]:
        min2[0] = a[i]
        min2[1] = i
if min1[0] * min2[0] > max[0] * max2[0]:
    print(min1[0], min2[0])
else:
    print(max2[0], max[0])
