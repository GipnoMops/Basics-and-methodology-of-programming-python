print(min(filter(lambda x: x % 2 != 0, map(int, open('input.txt').read().replace('\n', ' ').split()))))
