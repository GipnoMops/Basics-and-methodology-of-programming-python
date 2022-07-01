def zapis(a, b):
    a = a.split()
    b[a[0]] = b.get(a[0], 0) + int(a[1])
    return b


inFile = open('input.txt')
dict = {}
for line in inFile:
    zapis(line, dict)
for line in sorted(dict):
    print(line, dict[line])
