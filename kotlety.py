k = int(input())
m = int(input())
n = int(input())
t = ((n + k - 1) // k) * m * 2
if n % k <= k // 2 and n > k :
    t = t - m
print(t)
