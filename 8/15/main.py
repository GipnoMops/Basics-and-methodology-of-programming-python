def average(a):
    global summ, i
    summ = 0
    i = 0
    for i in range(len(nines)):
        summ += nines[i]
    return summ / len(nines)


inFile = open('input.txt', 'r', encoding='utf8')
elevens = []
nines = []
tens = []
for line in inFile:
    fam, name, klass, ball = list(line.split())
    if klass == '9':
        nines.append(int(ball))
    elif klass == '10':
        tens.append(int(ball))
    elif klass == '11':
        elevens.append(int(ball))
print(average(nines), average(tens), average(elevens))
