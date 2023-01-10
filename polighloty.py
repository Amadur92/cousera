def polygloty():
    n = int(input())
    all_langs = set()
    all_students = set()
    for i in range(n):
        k = int(input())
        languages = set()
        for j in range(k):
            lang = input()
            languages.add(lang)
        all_langs |= languages
        if i == 0:
            all_students = languages
        all_students &= languages
    print(len(all_students))
    for i in all_students:
        print(i)
    print(len(all_langs))
    for j in all_langs:
        print(j)

polygloty()
