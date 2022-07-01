inFile = open('input.txt', 'r', encoding='utf8')
n, m = map(int, inFile.readline().split())
anya = set()
borya = set()
k = 1
for line in inFile:
    if n < k <= n + m:
        k += 1
        borya.add(int(line))
    if k <= n:
        k += 1
        anya.add(int(line))
print(len(anya & borya))
print(*sorted(anya & borya))
print(len(anya - (anya & borya)))
print(*sorted(anya - (anya & borya)))
print(len(borya - (anya & borya)))
print(*sorted(borya - (anya & borya)))
