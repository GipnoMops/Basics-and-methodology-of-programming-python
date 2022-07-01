def CountSort(a):
    global b
    k = 0
    b = [0] * 101
    for now in a:
        b[now] += 1
    for i in range(101):
        if b[i] != 0:
            for j in range(b[i]):
                a[k] = i
                k += 1
    return a


a = list(map(int, input().split()))
CountSort(a)
print(*a)
