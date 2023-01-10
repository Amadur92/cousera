def lowest_positive(l):
    min_elem = max(l)
    for i in range(len(l)):
        if 0 < l[i] <= min_elem:
            min_elem = l[i]
    print(min_elem)


lowest_positive(list(map(int, input().split())))
