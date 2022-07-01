s = input()
f1 = s.find('h')
f2 = s.rfind('h')
s1 = s[0:f1 + 1]
s2 = s[f2:]
s3 = s[f1 + 1:f2]
print(s1, s3, s3, s2, sep='')
