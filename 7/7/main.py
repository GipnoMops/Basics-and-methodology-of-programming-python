a = list(map(int, input().split()))
b = [0, 0]
for i in range(len(a)):
    if i == 0:
        b[0] = a[i]
        b[1] = i
    if a[i] > b[0]:
        b[0] = a[i]
        b[1] = i
print(b[0], b[1])
