a = list(map(int, input().split()))
x = int(input())
mestopeti = 0
for i in range(len(a)):
    if i == 0:
        if a[0] < x:
            mestopeti = 1
            break
    if a[-1] >= x:
        mestopeti = len(a) + 1
        break
    if a[i] >= x > a[i + 1]:
        mestopeti = i + 2
        break
print(mestopeti)
