s = input()
f1 = s.find('f')
f2 = s.rfind('f')
if f1 == f2 and f1 != -1:
    print(f1)
elif f1 < f2:
    print(f1, f2)
elif f1 == -1:
    print('')
