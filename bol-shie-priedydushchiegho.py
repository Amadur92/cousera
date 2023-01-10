def bigger_than_previous(l):
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            print(l[i], end=' ')


bigger_than_previous(list(map(int, input().split())))
