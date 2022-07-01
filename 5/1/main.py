a = int(input())
b = int(input())
c = int(input())
d = int(input())


def min4(a1, a2, a3, a4):
    b1 = min(min(a1, a2), min(a3, a4))
    return b1


print(min4(a, b, c, d))
