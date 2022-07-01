from itertools import permutations
set(map(lambda x: print(*x, sep=''), permutations(range(1, int(input()) + 1))))
