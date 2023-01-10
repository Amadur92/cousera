def min_divisor(n):
    div = 2
    while div <= n**0.5:
        if not n % div:
            return div
        div += 1
    else:
        return n


print(min_divisor(int(input())))
