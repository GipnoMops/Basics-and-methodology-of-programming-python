n = int(input())
startfrom = 10 ** n - 1
stopon = 10 ** (n - 1)
for i in range(startfrom, stopon - 1, -2):
    print(i)
