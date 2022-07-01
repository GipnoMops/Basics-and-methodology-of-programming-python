p = int(input())
x = int(input())
y = float(input())
Y = x * 100 + y
g = Y + p * Y / 100
y2 = g % 100
y2 = int(y2)
x2 = (g - y2) // 100
x2 = int(x2)
print(x2, y2)
