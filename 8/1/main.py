def IsAscending(a):
    i = 0
    while i <= len(a) - 2 and a[i] < a[i + 1]:
        i += 1
    return i


a = list(map(int, input().split()))
b = IsAscending(a)
if b == len(a) - 1:
    print('YES')
else:
    print('NO')
