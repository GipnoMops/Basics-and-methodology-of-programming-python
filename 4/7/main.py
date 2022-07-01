n = int(input())
x = float(input())
k = 0
Px = 0
while k <= n:
    a = float(input())
    if k == n:
        Px = Px + a
    else:
        Px = (Px + a) * x
    k += 1
print(Px)
