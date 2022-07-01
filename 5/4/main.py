from math import sqrt


def distance(a, b, c, d):
    return sqrt((a - c) ** 2 + (b - d) ** 2)


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
print(distance(x1, y1, x2, y2) +
      distance(x2, y2, x3, y3) + distance(x1, y1, x3, y3))
