def merge(a, b):
    global i, j, c
    i = 0
    j = 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            c.append(a[i])
            i += 1
            j += 1
        elif a[i] > b[j]:
            j += 1
        elif a[i] < b[j]:
            i += 1
    return c


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = merge(a, b)
print(*c)
