n = int(input())
Fn = 0
i = 2
F1 = 1
F2 = 1
while i < n:
    if (n != 1) and (n != 2) and (n != 0):
        i += 1
        Fn = F1 + F2
        F1 = F2
        F2 = Fn
    elif (n == 1) or (n == 2):
        print(1)
        i += 1
if (n != 1) and (n != 2) and (n != 0):
    print(Fn)
if n == 0:
    print(0)
if (n == 1) or (n == 2):
    print(1)
