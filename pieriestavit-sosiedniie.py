def replace_near(l):
    for i in range(0, len(l) - 1, 2):
        l[i], l[i + 1] = l[i + 1], l[i]
    return l


print(*replace_near(list(map(int, input().split()))))
