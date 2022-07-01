dano = list(map(int, input().split()))
s = dano[0]
n = dano[1]
dannie = [0] * n
for i in range(n):
    dannie[i] = int(input())
dannie.sort()
zanyato = 0
k = 0
while zanyato <= s and k != n:
    zanyato += dannie[k]
    k += 1
if zanyato > s:
    k -= 1
print(k)
