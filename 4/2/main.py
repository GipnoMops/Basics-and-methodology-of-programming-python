import math
x = float(input())
if x - int(x) >= 0.5:
    print(math.ceil(x))
else:
    print(math.floor(x))
