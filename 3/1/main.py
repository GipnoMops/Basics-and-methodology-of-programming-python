n = int(input())
i = 1
while i**2 <= n:
    if i == 1:
        print(i)
        i += 1
    else:
        print(i**2)
        i += 1
