num2 = int(input())
num1 = num2
counter1, counter2, max1, max2 = 1, 1, 1, 1
while num2 != 0:
    num2 = int(input())
    if num2 > num1:
        counter1 = 1
        counter2 += 1
        if counter2 > max2:
            max2 = counter2
    if num2 < num1 and num2 != 0:
        counter2 = 1
        counter1 += 1
        if counter1 > max1:
            max1 = counter1
    if num1 == num2:
        counter1, counter2 = 1, 1
    num1 = num2
if max1 > max2:
    print(max1)
else:
    print(max2)
