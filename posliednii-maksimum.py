def last_max(l):
    max_ind = 0
    max_elem = l[0]
    for i in range(len(l)):
        if l[i] >= max_elem:
            max_elem = l[i]
            max_ind = i
    return max_elem, max_ind


print(*last_max(list(map(int, input().split()))))
