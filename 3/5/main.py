n = int(input())
i = 1
while i <= n:
    if i == n or n == 1:
        print("YES")
        i *= 2
    elif i > n:
        print("NO")
    elif i <= n:
        i *= 2
if (i > n) and (n != 1) and (n * 2 != i):
    print('NO')
