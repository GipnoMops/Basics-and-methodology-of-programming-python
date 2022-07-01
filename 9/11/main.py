inFile = open('input.txt')
n, k = map(int, inFile.readline().split())
allday = set()
for i in range(k):
    ai, bi = map(int, inFile.readline().split())
    day = ai
    while day <= n:
        if day % 7 != 6 and day % 7 != 0:
            allday.add(day)
            day += bi
        else:
            day += bi
print(len(allday))
