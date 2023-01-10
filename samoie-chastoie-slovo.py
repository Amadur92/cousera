from collections import Counter


def most_common_word():
    with open('input.txt', 'r', encoding='utf-8') as f:
        data = f.read().split()
    s = (Counter(data).most_common())
    s = list(filter(lambda x: x[1] == s[0][1], s))
    s.sort(key=lambda x: x[0])
    print(s[0][0])

most_common_word()
