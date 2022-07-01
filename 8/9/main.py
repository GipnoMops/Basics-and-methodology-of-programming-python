noga = int(input())
obuvVmagazine = list(map(int, input().split()))
obuvVmagazine.sort()
k = 0
for i in range(len(obuvVmagazine)):
    if noga <= obuvVmagazine[i]:
        k += 1
        noga = obuvVmagazine[i] + 3
print(k)
