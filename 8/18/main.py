def top_schools(a):
    global otvet
    otvet = []
    maxx = 0
    for i in range(len(a)):
        if a.count(a[i]) > maxx:
            otvet = []
            maxx = a.count(a[i])
            otvet.append(a[i])
        if a.count(a[i]) == maxx:
            for j in range(len(otvet)):
                if a[i] == otvet[j]:
                    break
                if a[i] == otvet[-1]:
                    break
                if a[i] < otvet[0]:
                    otvet.insert(0, a[i])
                    break
                if j + 1 < len(otvet) - 1 and otvet[j] > a[i] > otvet[j + 1]:
                    otvet.insert(j + 1, a[i])
                    break
                if a[i] > otvet[-1]:
                    otvet.append(a[i])
                    break
    return otvet


inFile = open('input.txt', 'r', encoding='utf8')
schools = []
for line in inFile:
    fam, name, sch, ball = list(line.split())
    schools.append(int(sch))
a = top_schools(schools)

print(*a)
