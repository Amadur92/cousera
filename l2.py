x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if 0 < x1 < 9 and 0 < x2 < 9 and 0 < y1 < 9 and 0 < y2 < 9:
    if (x1 + y1) % 2 != (x2 + y2) % 2:
        print('NO')
    elif x2 + y2 < x1 + x2:
        print('NO')
    elif x2 - y2 > x1 - y1:
        print('NO')
    else:
        print('YES')
else:
    print('NO')
