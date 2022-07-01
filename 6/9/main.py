for i in range(10, 100):
    a1 = i % 10
    a2 = i // 10
    if i == 2 * a1 * a2:
        print(i)
