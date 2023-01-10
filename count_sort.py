def counting_sort(array):
    c = [0] * 101
    for i in range(len(array)):
        c[array[i]] += 1
    result = []
    for i in range(len(c)):
        result += [i] * c[i]
    return result


print(*counting_sort(list(map(int, input().split()))))
