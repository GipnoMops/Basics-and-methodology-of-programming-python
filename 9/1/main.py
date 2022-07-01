inFile = open('input.txt', 'r', encoding='utf8')
chisla = []
for line in inFile:
    chisla = map(int, line.split())
print(len(set(chisla)))
