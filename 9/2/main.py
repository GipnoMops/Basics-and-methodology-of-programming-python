inFile = open('input.txt', 'r', encoding='utf8')
line1 = set(map(int, inFile.readline().split()))
line2 = set(map(int, inFile.readline().split()))
chisla = line1 & line2
print(len(chisla))
