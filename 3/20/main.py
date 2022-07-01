k = int(input())
i = 0
K = 0
while i < k:
    perevernutoe = 0
    perrazr = 0
    i += 1
    l = i
    while l > 0:
        perevernutoe = (10 * perevernutoe) + (l % 10)
        l = l // 10
        if perevernutoe == i:
            K += 1
print(K)
