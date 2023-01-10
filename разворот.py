def rec():
    n = int(input())
    if n == 0:
        return print(n)
    rec()
    return print(n)

rec()