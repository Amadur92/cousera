def is_prime(n):
    div = 2
    while div <= n**0.5:
        if n % div == 0:
            return False
        div += 1
    return True


if is_prime(int(input())):
    print("YES")
else:
    print("NO")
