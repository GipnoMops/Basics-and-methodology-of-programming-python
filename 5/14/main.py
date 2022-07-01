def power(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    if n == 2:
        return a ** 2
    if n % 2 == 0:
        return (power(a, n // 2)) ** 2
    if n % 2 != 0:
        return a * power(a, n - 1)


a = float(input())
n = int(input())
print(power(a, n))
