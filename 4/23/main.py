s = input()
k = 0
while k < len(s):
    if k < len(s) - 1:
        print(s[k], '*', sep='', end='')
        k += 1
    else:
        print(s[k])
        k += 1
