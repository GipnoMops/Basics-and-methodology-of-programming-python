s = input()
f1 = s.find('f')
f2 = s.find('f', f1 + 1)
f3 = s.rfind('f')
if f2 == f1 and f2 != -1:
    print(-1)
elif f1 == -1:
    print(-2)
else:
    print(f2)
