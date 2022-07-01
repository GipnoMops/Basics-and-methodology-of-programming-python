def maxx(a):
    global max, i
    i = 0
    max = 0
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
    return max


def num_of_win(a):
    global k
    win = maxx(a)
    k = 0
    for i in range(len(a)):
        if a[i] == win:
            k += 1
    return k


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
print(num_of_win(nines), num_of_win(tens), num_of_win(elevens))
