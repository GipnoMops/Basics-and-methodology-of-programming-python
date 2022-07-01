def gcd(a, b):
    if b == 0:
        return a
    if b == 1 or a == 1:
        return b
    return (gcd(b, a % b))


a = int(input())
b = int(input())
print(gcd(a, b))
