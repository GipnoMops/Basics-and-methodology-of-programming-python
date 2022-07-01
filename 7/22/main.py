x = []
y = []
otvet = 0
for i in range(8):
    koordinati = list(map(int, input().split()))
    x.append(koordinati[0])
    y.append(koordinati[1])
for i in range(8):
    if x.count(x[i]) != 1 or y.count(y[i]) != 1:
        otvet += 1
        break
    for j in range(i + 1, 8):
        if (x[i] - x[j]) ** 2 == (y[i] - y[j]) ** 2:
            otvet += 1
            break
if otvet == 0:
    print('NO')
else:
    print('YES')
