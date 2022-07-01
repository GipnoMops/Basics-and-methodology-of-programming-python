inFile = open('input.txt', 'r', encoding='utf8')
n = int(inFile.readline())
ostalis = set(range(1, n + 1))
for line in inFile:
    if line == 'HELP\n':
        break
    else:
        line2 = inFile.readline()
        if line2 == 'YES\n':
            line = set(map(int, line.split()))
            ostalis &= line
        elif line2 == 'NO\n':
            ostalis -= set(map(int, line.split()))
print(*sorted(ostalis))
