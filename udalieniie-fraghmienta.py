def find_index(s):
    first = s.find("h")
    last = s.rfind("h")
    s = s[:first] + s[last + 1:]
    print(s)


find_index(input())
