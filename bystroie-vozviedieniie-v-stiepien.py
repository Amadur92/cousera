def pow(a, n):
    if n == 1:
        return a
    if n == 0:
        return 1
    elif n % 2 == 1:
        return a * pow(a * a, (n - 1) / 2)
    elif n % 2 == 0:
        return pow(a * a, (n / 2))


print(pow(float(input()), int(input())))
