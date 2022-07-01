def gcd(a, b):
    if b == 0:
        return a
    if b == 1 or a == 1:
        return b
    return (gcd(b, a % b))


def ReduceFraction(a, b):
    return a // gcd(a, b), b // gcd(a, b)


a = int(input())
b = int(input())
p, q = ReduceFraction(a, b)
print(p, q)
