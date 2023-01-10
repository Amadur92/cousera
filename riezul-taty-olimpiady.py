def olympiad_sort(l):
    l.sort(key=lambda x: int(x[1]), reverse=True)
    for user in l:
        print(user[0])


n = int(input())
data = []
for _ in range(n):
    data.append(input().split())
olympiad_sort(data)
