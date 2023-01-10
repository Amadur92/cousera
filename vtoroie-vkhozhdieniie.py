def second_find(s):
    i = s.find('f')
    s = s[i + 1:]
    j = s.find('f')
    if j == -1:
        if i == j:
            print(-2)
        else:
            print(-1)
    else:
        print(i + j + 1)


second_find(input())
