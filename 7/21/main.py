dano = list(map(int, input().split()))
n = dano[0]
k = dano[1]
b = []
for i in range(n):
    b.append('I')
for i in range(k):
    diapozon = list(map(int, input().split()))
    x1 = diapozon[0]
    x2 = diapozon[1]
    for j in range(x1 - 1, x2):
        b[j] = '.'
for i in range(n):
    print(b[i], sep='', end='')

