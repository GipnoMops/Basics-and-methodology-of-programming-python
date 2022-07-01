a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a == b == c == d == e == f == 0:
    print('5')
if (a * d - b * c) != 0:
    y = (a * f - c * e) / (a * d - b * c)
    x = (e * d - b * f) / (a * d - b * c)
    print('2', x, y)
if ((a == b == 0) or
        (a == c and b == d and e == f) or
        ((a * d - b * c) == 0 and
         a != 0 and b != 0 and
         c != 0 and d != 0)):
    print('1', -1 * c / d, f / d)
elif c == d == 0:
    print('1', -1 * a / b, e / b)
    if ((a == c and b == d and e != f) or
            ((e == f) and (a == c or b == d) and
             (a != c or b != d)) or
            (b == d == 0 and e / a != f / c) or
            (a == c == 0 and e / b != f / d)):
        print('0')
if b == d == 0 and e / a == f / c:
    print('3', e / a)
if a == c == 0 and e / b == f / d:
    print('4', e / b)
