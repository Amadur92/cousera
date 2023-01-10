def archive(size, users_count, users):
    users = sorted(users)
    memory_used = 0
    result = 0
    i = 0
    while memory_used < size and result < users_count:
        memory_used += users[i]
        if memory_used < size:
            result += 1
        i += 1
    return result


s, u = tuple(map(int, input().split()))
us = []
for _ in range(u):
    us.append(int(input()))
print(archive(s, u, us))
