def closest_num(l, i):
    dist = abs(l[0] - i)
    memo = l[0]
    for j in l:
        if dist > abs(j - i):
            dist = abs(j - i)
            memo = j
    return memo


k = int(input())
m = list(map(int, input().split()))
n = int(input())
print(closest_num(m, n))
