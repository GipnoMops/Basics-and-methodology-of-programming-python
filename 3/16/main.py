A = int(input())
Fn = 0
k = 2
F1 = 1
F2 = 1
while Fn < A:
    k += 1
    Fn = F1 + F2
    F1 = F2
    F2 = Fn
if A != Fn:
    print(-1)
else:
    print(k)
