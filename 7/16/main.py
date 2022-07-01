a = list(map(int, input().split()))
min = a[0]
min_ind = 0
max = a[0]
max_ind = 0
for i in range(len(a)):
    if a[i] < min:
        min = a[i]
        min_ind = i
    elif a[i] > max:
        max = a[i]
        max_ind = i
b = a[max_ind]
a[max_ind] = a[min_ind]
a[min_ind] = b
print(*a)
