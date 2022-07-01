a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = 0
for i in range(1001):
    if i != e:
        if a * i * i * i + b * i ** 2 + c * i + d == 0:
            k += 1
print(k)
