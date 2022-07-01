def Zapis_slovorya(a, b):
    a = a.split()
    for i in range(len(a)):
        b[a[i]] = a[0]
    return b


inFile = open('input.txt')
n = int(inFile.readline().split()[0])
dict = {}
for i in range(n):
    line = inFile.readline()
    Zapis_slovorya(line, dict)
m = int(inFile.readline().split()[0])
for i in range(m):
    line = inFile.readline().split()[0]
    print(dict[line])
