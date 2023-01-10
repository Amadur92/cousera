def pow(a, n):
    if n == 1:
        return a
    if n == 0:
        return 1
    return a * pow(a, n - 1)


print(pow(float(input()), int(input())))
