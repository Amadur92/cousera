def even_index(l):
    for i in range(0, len(l), 2):
        print(l[i], end=' ')


even_index(list(map(int, input().split())))
