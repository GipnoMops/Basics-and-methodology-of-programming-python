max2 = 1
b = 1
max = 1
while b != 0:
    b = int(input())
    if b > max:
        max2 = max
        max = b
    elif (max2 < b):
        max2 = b
print(max2)

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
