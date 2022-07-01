def IsPointInSquare(x, y):
    return ((x + y >= 0 and y - 2 * x - 2 >= 0 and
             (x + 1) ** 2 + (y - 1) ** 2 <= 4) or
            (x + y <= 0 and y - 2 * x - 2 <= 0 and
             (x + 1) ** 2 + (y - 1) ** 2 >= 4))


x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
