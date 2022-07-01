from math import sqrt, ceil
print(*filter(lambda x: all(map(lambda y: (x % y != 0), range(2, int(sqrt(x)) + 1))), range(2, int(open('input.txt').readline().split()[0]) + 1)))

print(
    *filter(
        lambda x: all(x % y != 0 for y in range(2, round(sqrt(x)) + 1)),
        range(2, int(input()) + 1)
    )
)



