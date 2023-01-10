def sort_students(l: list) -> list:
    k = int(l[0])
    res = []
    for student in l[1:]:
        name = " "
        student = student.split()
        name = name.join(student[:-3])
        res.append([name, *list(map(int, student[-3:])),
                    sum(list(map(int, student[-3:])))])
    res.sort(key=lambda x: x[-1], reverse=True)
    res = list(filter(lambda x: x[-4] >= 40 and
                      x[-2] >= 40 and x[-3] >= 40, res))
    if k >= len(res):
        print(0)
    elif res[0][-1] == res[k][-1]:
        print(1)
    else:
        for s in res[k - 1:: - 1]:
            if s[-1] == res[k][-1]:
                continue
            print(s[-1])
            break


def main():
    with open('input.txt', 'r', encoding="utf-8") as f:
        data = f.readlines()
    sort_students(data)


main()
