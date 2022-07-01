inFile = open('input.txt', 'r', encoding='utf8')
n = int(inFile.readline())
ostalis = set(range(1, n + 1))
line = inFile.readline()
while line != 'HELP':
    da = ostalis & set(map(int, line.split()))
    net = ostalis - set(map(int, line.split()))
    if len(da) > len(net):
        ostalis = da
        print('YES')
    elif len(da) <= len(net):
        ostalis = net
        print('NO')
    line = inFile.readline()
print(*sorted(ostalis))
