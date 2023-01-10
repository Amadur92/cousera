def count_pisitive_nums(l):
    l = list(filter(lambda x: x > 0, l))
    return len(l)


print(count_pisitive_nums(list(map(int, input().split()))))
