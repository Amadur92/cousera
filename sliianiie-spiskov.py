def merge(list_a, list_b):
    result = []
    cur_a = cur_b = 0
    for _ in range(len(list_a) + len(list_b)):
        if list_a[cur_a] >= list_b[cur_b]:
            result.append(list_b[cur_b])
            cur_b += 1
        else:
            result.append(list_a[cur_a])
            cur_a += 1
        if cur_a == len(list_a):
            result.extend(list_b[cur_b:])
            break
        if cur_b == len(list_b):
            result.extend(list_a[cur_a:])
            break
    return result


l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
print(*merge(l1, l2))
