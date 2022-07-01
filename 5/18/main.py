def C(n, k):
    if k == 0:
        return 1
    if k == n:
        return 1
    if k == 1:
        return n
    return C(n - 1, k - 1) + C(n - 1, k)


n = int(input())
k = int(input())
print(C(n, k))
