from functools import reduce
print(reduce(lambda x, y: x * y,
    map(
      int,
      open('input.txt').read().replace('\n', ' ').split()
      )
)**5
)
