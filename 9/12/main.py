inFile = open('input.txt')


def Preobrazovanie(a):
    a = a.split()
    a[0] = a[0].replace('+', '')
    a[0] = a[0].replace('-', '')
    a[0] = a[0].replace('(', '')
    a[0] = a[0].replace(')', '')
    a = str(a[0])
    if len(a) >= 10:
        if a[0] == '8':
            a = a[1:]
        elif a[0] == '7':
            a = a[1:]
    elif len(a) <= 7:
        a = '495' + a
    return a


dano = inFile.readline()
nomer1 = Preobrazovanie(dano)
for phone in inFile:
    nomer = Preobrazovanie(phone)
    if nomer == nomer1:
        print('YES')
    else:
        print('NO')
