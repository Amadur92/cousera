a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a == 0:
    if b == 0:
        print("INF")
    else:
        print('NO')
else:
    if a * d == b * c:
        print('NO')
    else:
        if (-b / a) % 1 == 0:
            print(-b // a)
        else:
            print('NO')
