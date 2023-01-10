def shoes_shop(size, available):
    available = filter(lambda x: x >= size, sorted(available))
    on_leg = size - 3
    count = 0
    for shoe in available:
        if shoe >= on_leg + 3:
            count += 1
            on_leg = shoe
    return count


print(shoes_shop(int(input()), list(map(int, input().split()))))
