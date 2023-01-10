def intersection(list_a, list_b):
    res = list(set(list_a) & set(list_b))
    res.sort()
    return res


l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
print(*intersection(l1, l2))
