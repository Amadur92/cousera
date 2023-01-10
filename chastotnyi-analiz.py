from collections import Counter
from itertools import groupby


def frequency_analysis():
    with open('input.txt', 'r', encoding='utf-8') as f:
        data = f.read().split()
    s = (Counter(data).most_common())
    s = groupby(s, lambda x: x[1])
    for num, words in s:
        words = sorted(words, key=lambda x: x[0])
        for word in words:
            print(word[0])

frequency_analysis()
