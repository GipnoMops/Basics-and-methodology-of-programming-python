inFile = open('input.txt', 'r', encoding='utf8')
danie = [0] * 8
mesta = []
rezults = []
for line in inFile:
    mesta = list(line.split())
    break
k = int(mesta[0])
for line in inFile:
    danie = list(line.split())
    exam1 = int(danie[-3])
    exam2 = int(danie[-2])
    exam3 = int(danie[-1])
    if exam1 >= 40 and exam2 >= 40 and exam3 >= 40:
        rezults.append((exam1 + exam2 + exam3))
rezults.sort()
l = -k
if len(rezults) >= k + 1 and rezults[-1] == rezults[-k]:
    print(1)
if len(rezults) <= k:
    print(0)
if len(rezults) >= k + 1 and rezults[-k] == rezults[-k - 1] and \
        rezults[-1] != rezults[-k]:
    prohodnoi = rezults[-k]
    while prohodnoi == rezults[l]:
        prhodnoi = rezults[l]
        l += 1
    print(rezults[l])
if len(rezults) >= k + 1 and rezults[-k] != rezults[-k - 1] and \
        rezults[-1] != rezults[-k]:
    l = -1 * k
    print(rezults[l])
