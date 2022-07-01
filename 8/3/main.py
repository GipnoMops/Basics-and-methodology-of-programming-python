n = int(input())
a = list(map(int, input().split()))
x = int(input())
otvet = [a[0], abs(a[0] - x)]
for i in range(len(a)):
    if abs(a[i] - x) < otvet[1]:
        otvet[1] = abs(a[i] - x)
        otvet[0] = a[i]
print(otvet[0])
