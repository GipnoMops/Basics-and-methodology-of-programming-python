inFile = open('input.txt', 'r', encoding='utf8')
line1 = tuple(map(int, inFile.readline().split()))
chisla = set()
for i in line1:
    if i in chisla:
        print('YES')
    else:
        print ('NO')
        chisla.add(i)
