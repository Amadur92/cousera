def make_flags(n):
    r1 = r2 = r3 = r4 = ""
    for i in range(n):
        r1 += "+___ "
        r2 += f"|{i + 1} / "
        r3 += "|__\ "
        r4 += "|    "
    print(r1)
    print(r2)
    print(r3)
    print(r4)


make_flags(int(input()))
