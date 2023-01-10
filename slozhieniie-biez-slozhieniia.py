def no_sum(a, b):
    if b == 0:
        return a
    if b >= 0:
        return no_sum(a + 1, b - 1)
    else:
        return no_sum(a - 1, b + 1)


print(no_sum(int(input()), int(input())))
