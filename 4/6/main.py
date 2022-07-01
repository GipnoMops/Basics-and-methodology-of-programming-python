n = int(input())
sum = 0
k = 1
while k <= n:
    sum += 1 / k ** 2
    k += 1
print(sum)
