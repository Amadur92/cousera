def second_max(l):
    l.remove(max(l))
    return max(l)


lst = []
n = int(input())
while n != 0:
    lst.append(n)
    n = int(input())
print(second_max(lst))
