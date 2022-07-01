def count(a, b):
    b[a[0]] = {a[1]: a[2]}
    return b


inFile = open('input.txt', 'r', encoding='utf8')
pokupateli = {}
for line in inFile:
    count(line.split(), pokupateli)
print(pokupateli)
