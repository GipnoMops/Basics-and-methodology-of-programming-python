max = int(input())
b = 1
k = 1
while b != 0:
    b = int(input())
    if b > max:
        k = 1
        max = b
    elif b == max:
        k += 1
print(k)
