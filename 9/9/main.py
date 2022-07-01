inFile = open('input.txt', 'r', encoding='utf8')
n = int(inFile.readline())
knowall = set()
knowone = set()
for i in range(n):
    znaet = int(inFile.readline())
    ai = set()
    for j in range(znaet):
        ai |= set(inFile.readline().split())
    if i != 0:
        knowone |= ai
        knowall &= ai
    else:
        knowone |= ai
        knowall = ai
print(len(knowall))
if len(knowall) != 0:
    print(*knowall, sep='\n')
print(len(knowone))
print(*knowone, sep='\n')
