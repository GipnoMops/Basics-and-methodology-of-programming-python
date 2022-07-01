from math import sqrt
a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4 * a * c
if a == 0 and b == 0 and c == 0:
    print(3)
elif (D < 0):
    print(0)
elif a == 0 and b != 0:
    x1 = -1 * c / b
    print(1, x1)
elif a == 0 and b == 0:
    print(0)
elif a == 0 and b == 0 and c == 0:
    print(3)
else:
    x1 = (-1 * b + sqrt(D)) / (2 * a)
    x2 = (-1 * b - sqrt(D)) / (2 * a)
    if x1 > x2:
        print(2, x2, x1)
    elif x2 > x1:
        print(2, x1, x2)
    elif x1 == x2:
        print(1, x1)
