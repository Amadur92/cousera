def reduce(n, m):
    div = 2
    if n == m:
        return 1, 1
    while div <= n**0.5 or div <= m**0.5:
        if n % div == 0 and m % div == 0:
            n, m = n // div, m // div
        else:
            div += 1
    return n, m


print(*reduce(int(input()), int(input())))
