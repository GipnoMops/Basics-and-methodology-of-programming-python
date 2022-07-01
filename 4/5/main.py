import math
p = int(input())
x = int(input())
y = int(input())
k = int(input())
Y = x * 100 + y
while k > 0:
    Y = Y + p * Y / 100
    Y = round(Y)
    k -= 1
y2 = Y % 100
y2 = int(y2)
x2 = (Y - y2) / 100
x2 = int(x2)
print(x2, y2)
