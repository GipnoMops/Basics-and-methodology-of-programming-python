def maxx(a):
    max = 0
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
    return max


def maxx2(a):
    max1 = maxx(a)
    max2 = 0
    for i in range(len(a)):
        if a[i] > max2 and a[i] < max1:
            max2 = a[i]
    return max2


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
print(maxx2(nines), maxx2(tens), maxx2(elevens))
