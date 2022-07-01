def NaborPosled(a, b):
    global i
    i = 0
    for i in range(len(b)):
        a[b[i] - 1] -= 1
    return a


n = int(input())
prochnost = list(map(int, input().split()))
k = int(input())
nagali = list(map(int, input().split()))
NaborPosled(prochnost, nagali)
for i in range(len(prochnost)):
    if prochnost[i] >= 0:
        print('NO')
    else:
        print('YES')
