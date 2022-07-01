def Perevernutaya():
    n = int(input())
    if n == 0:
        print(0)
        return 0
    Perevernutaya()
    if n != 0:
        print(n)


Perevernutaya()
