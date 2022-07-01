A = int(input())
B = int(input())
for i in range(A, B + 1):
    perevernutor = 0
    dublikat = i
    while dublikat != 0:
        perevernutor = (perevernutor + dublikat % 10) * 10
        dublikat //= 10
    if i == (perevernutor // 10):
        print(i)
