def diference(a):
    a1, a2, a3, a4 = a//1000, a//100%10, a%100//10, a%10
    if a1!=a2 and a2!=a3 and a3!=a4 and a1!=a4 and a1!=a3 and a2!= a4:
        return a
l = []
for i in range(1000, 9999):
    if diference(i)!=None:
        l.append(i)
print(l)
