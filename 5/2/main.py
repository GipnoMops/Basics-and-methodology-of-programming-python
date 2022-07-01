from math import sqrt
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def distance(a, b, c, d):
    return sqrt((a - c) ** 2 + (b - d) ** 2)


print(distance(x1, y1, x2, y2))
