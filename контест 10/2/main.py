inFile = open('input.txt')
text = inFile.readlines()
for i in range(len(text)):
    text[i] = text[i].split()
dict = {}
for i in range(len(text)):
    for j in range(len(text[i])):
        dict[text[i][j]] = dict.get(text[i][j], 0) + 1
        print(dict[text[i][j]] - 1)
