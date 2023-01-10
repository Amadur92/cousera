def summa(n, sum=0):
    if n != 0:
        sum += n
        return summa(int(input()), sum)
    else:
        return sum


print(summa(int(input())))
