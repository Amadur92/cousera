ashop = list(map(int, input().split(" " )))
bshop = list(map(int, input().split(" " )))
cshop = list(map(int, input().split(" " )))
m = min(ashop[0],bshop[0],cshop[0])
h = min(ashop[1],bshop[1],cshop[1])
k = min(ashop[2],bshop[2],cshop[2])
print("Мин.цена на молоко",m,"Мин.цена на хлеб",h,"Мин. цена на колбасу",k)








"""a = {"а":"._","б":"_...","в":".__","г":"__.","д":"_..","е":".","ж":"..._","з":"__..","и":"..","й":".___"}
for letter in b:
    c+=a[letter]
print(c)



















a = {"Russia":"Moscow","USA":"Washington","France":"Paris"}
print (a.keys())
print(a.values())
"""