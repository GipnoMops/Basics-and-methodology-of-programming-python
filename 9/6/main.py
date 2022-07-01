inFile = open('input.txt', 'r', encoding='utf8')
slova = set()
for line in inFile:
    slovo = line.split()
    for i in slovo:
        slova.add(i)
print(len(slova))
