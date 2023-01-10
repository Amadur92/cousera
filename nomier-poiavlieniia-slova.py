def count_words(lt: list):
    d = dict([(x, 0) for x in lt])
    for word in lt:
        print(d[word], end=" ")
        d[word] += 1

with open('input.txt', 'r', encoding='utf-8') as data:
    count_words(data.read().split())
