print(*map(lambda x: int(x == (1, 0) or x == (0, 1)), zip(map(int, input().split()), map(int, input().split()))))
