oldnum = 0
counter = 1
n = int(input())
maxlen = 1
while n != 0:
    if n == oldnum:
        counter += 1
    else:
        counter = 1
    oldnum = n
    n = int(input())
    maxlen = max(maxlen, counter)

print(maxlen)
