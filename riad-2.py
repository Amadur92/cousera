def range2(n1, n2):
    if n1 < n2:
        for i in range(n1, n2 + 1):
            print(i, end=" ")
    else:
        for i in range(n1, n2 - 1, -1):
            print(i, end=" ")


range2(int(input()), int(input()))
