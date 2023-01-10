def make_dicts():
    n = int(input())
    d = {}
    for _ in range(n):
        k, v = input().split()
        d[k], d[v] = v, k
    print(d[input()])

make_dicts()
