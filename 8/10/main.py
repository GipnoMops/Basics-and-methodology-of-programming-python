kol = int(input())
b = [0] * kol
for i in range(kol):
    n, h = input().split()
    b[i] = (int(h), n)
b.sort(reverse=True)
for i in range(kol):
    print(b[i][1])
