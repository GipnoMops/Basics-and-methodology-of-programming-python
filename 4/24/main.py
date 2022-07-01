s = input()
k = 0
while k < len(s):
    if k % 3 != 0:
        print(s[k], sep='', end='')
        k += 1
    else:
        k += 1
