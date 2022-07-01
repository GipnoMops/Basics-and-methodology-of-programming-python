def count(a, b):
    b[a] = b.get(a, 0) + 1
    return b


inFile = open('input.txt', 'r', encoding='utf8')
text1 = inFile.readlines()
text2 = []
text = []
dict = {}
tcid = {}
otvet = []
for i in range(len(text1)):
    text2.append(text1[i].split('\n'))
    text.append(text2[i][0])
for i in range(len(text)):
    count(text[i], dict)
for i in dict:
    tcid = dict[i], i
    otvet.append(tcid)
otvet = sorted(otvet, reverse=True)
if otvet[0][0] > len(text) / 2:
    print(otvet[0][1])
else:
    print(otvet[0][1])
    print(otvet[1][1])
