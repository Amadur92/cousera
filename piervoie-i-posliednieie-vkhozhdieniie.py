def find_index(s):
    first = s.find("f")
    last = s.rfind("f")
    if first == last != -1:
        print(first)
    elif first != last:
        print(first, last)


find_index(input())
