a = 1
b = 0
c = []
for n in range(1, 1000):
    while a<n/2:
        a+=1
        if n%a==0 and a%2==0:
            c.append(a)
            b+=1
            print(a)
        else:
            if b == 6:
                print(c, n)

            else:
                b = 0
                c = []
print(c)