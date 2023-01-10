def elections():
    with open('input.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
    d = {}
    total = len(data)
    for name in data:
        name = name.strip()
        if name in d:
            d[name] += 1
        else:
            d[name] = 1
    sorted_list = (sorted(d, key=lambda x: d[x], reverse=True))
    with open('output.txt', 'w', encoding='utf-8') as f:
        if d[sorted_list[0]] > total / 2:
            f.write(sorted_list[0])
        else:
            f.write(sorted_list[0] + "\n" + sorted_list[1])

elections()
