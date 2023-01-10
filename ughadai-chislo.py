def guess_number(n):
    answ = ""
    variants = set(list(range(1, n + 1)))
    while answ != "HELP":
        guess = input()
        if guess == "HELP":
            print(*sorted(list(variants)))
            break
        answ = input()
        if answ == "YES":
            variants &= set(list(map(int, guess.split())))
        elif answ == "NO":
            variants -= set(list(map(int, guess.split())))

guess_number(int(input()))
