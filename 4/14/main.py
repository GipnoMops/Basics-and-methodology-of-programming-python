s = input()
f1 = s.find('h')
f2 = s.rfind('h')
s1 = s[0:f1]
s2 = s[f2 + 1:]
print(s1, s2, sep='')
