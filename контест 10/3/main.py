def zapis(a, b):
    a = a.split()
    b[a[0]] = a[1]
    b[a[1]] = a[0]
    return b


inFile = open('input.txt')
n = int(inFile.readline().split()[0])
dict = {}
for i in range(n):
    zapis(inFile.readline(), dict)
sinonim = inFile.readline().split()[0]
print(dict[sinonim])
