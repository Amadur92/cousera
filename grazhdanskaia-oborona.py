n = int(input())
sd = list(map(int, input().split()))
villages = []
for i in range(n):
    villages.append((sd[i], i + 1))
villages.sort()

m = int(input())
bd = list(map(int, input().split()))
shelters = []
for i in range(m):
    shelters.append((bd[i], i + 1))
shelters.sort()

res = [0] * n
fb = 0

for i in range(0, n):
    dist = villages[i][0] + shelters[0][0]
    j = fb
    while j < m and abs(villages[i][0] - shelters[j][0]) < dist:
        if abs(villages[i][0] - shelters[j][0]) < dist:
            dist = abs(villages[i][0] - shelters[j][0])
            res[villages[i][1] - 1] = shelters[j][1]
            fb = j
        j += 1

print(*res)
