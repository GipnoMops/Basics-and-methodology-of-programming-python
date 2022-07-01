def power(a, n):
    global k, otvet
    otvet = 1
    if n < 0:
        k = 1
        n = -1 * n
    else:
        k = 0
    if n == 0:
        return 1
    if n == 1 and k != 1:
        return a
    while n >= 1:
        otvet *= a
        n -= 1
    if k == 1:
        return (1 / otvet)
    else:
        return otvet


a = float(input())
n = int(input())
print(power(a, n))
