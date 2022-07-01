inFile = open('input.txt')
n = map(int, inFile.readline().split())
m = map(int, inFile.readline().split())
print(*n, *m)
