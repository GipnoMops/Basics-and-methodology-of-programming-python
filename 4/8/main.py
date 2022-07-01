from math import sqrt
a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4 * a * c
if D < 0:
    print()
else:
    x1 = (-1 * b + sqrt(D)) / (2 * a)
    x2 = (-1 * b - sqrt(D)) / (2 * a)
    if x1 > x2:
        print(x2, x1)
    elif x2 > x1:
        print(x1, x2)
    else:
        print(x1)
