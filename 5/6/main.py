from math import fabs


def IsPointInSquare(x, y):
    return fabs(x) + fabs(y) <= 1


x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
