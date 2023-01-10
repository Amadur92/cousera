def sort_names():
    with open('input.txt', 'r', encoding='utf8') as f:
        data = f.readlines()
        data.sort()
    with open('output.txt', 'w', encoding='utf8') as f:
        for name in data:
            name = name.split()
            name = name[0] + " " + name[1] + " " + name[3] + "\n"
            f.write(name)


sort_names()
