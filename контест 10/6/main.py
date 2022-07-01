def count(a, b):
    b[a] = b.get(a, 0) + 1
    return b


inFile = open('input.txt')
text1 = inFile.readlines()
text = []
text2 = []
dict = {}
tcid = ()
otvet = []
for i in range(len(text1)):
    text2.append(text1[i].split())
    for j in range(len(text2[i])):
        text.append(text2[i][j])
for i in range(len(text)):
    count(text[i], dict)
for i in dict:
    tcid = -1 * dict[i], i
    otvet.append(tcid)
otvet = sorted(otvet)
for i in range(len(otvet)):
    print(otvet[i][1])
