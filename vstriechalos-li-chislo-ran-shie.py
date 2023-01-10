def is_num_in_list(l):
    s = set()
    for num in l:
        if num in s:
            print('YES')
        else:
            print('NO')
        s.add(num)


def main():
    l = list(map(int, input().split()))
    is_num_in_list(l)


main()
