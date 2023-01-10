print(*list(map(lambda x: abs(x[1] - x[0]), list(zip(map(int, open('input.txt', 'r', encoding='utf8').readlines()[0].split()), map(int, open('input.txt', 'r', encoding='utf8').readlines()[1].split()))))))

def xor(link: str):
    a, b = open(link, 'r', encoding='utf8').readlines()
    a = map(int, a.split())
    b = map(int, b.split())
    return list(map(lambda x: abs(x[1] - x[0]), list(zip(a, b))))

print(*xor('input.txt'))
