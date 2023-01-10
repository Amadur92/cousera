def even_elems(l):
    for i in l:
        if i % 2 == 0:
            print(i, end=' ')


even_elems(list(map(int, input().split())))
