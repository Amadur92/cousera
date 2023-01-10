def minimax_replace(l):
    min_l = l.index(min(l))
    max_l = l.index(max(l))
    l[min_l], l[max_l] = l[max_l], l[min_l]
    return l


print(*minimax_replace(list(map(int, input().split()))))
