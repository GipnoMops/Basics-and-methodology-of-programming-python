inFile = open('input.txt', 'r', encoding='utf8')
children = []
for line in inFile:
    fam, name, cod, ball = list(line.split())
    children.append((fam, name, int(ball)))
children.sort()
for i in range(len(children)):
    print(*children[i])
