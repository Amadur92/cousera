a = int(input())
b = int(input())
x = max(a,b)
def nok (a, b):
    global x
    if x%a==0 and x%b == 0:
        return x
    else:
        x+=1
        return nok(a,b)

#print(nok(a,b))

d = 2
def delit(c):
    global d

    if c%d ==0:
        print(d)
        return delit(c/d)
    elif c == 1:
        print("end")
    else:

        d+=1
        return delit(c)

delit(a)