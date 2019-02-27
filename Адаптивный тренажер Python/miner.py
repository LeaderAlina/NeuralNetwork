def neib(li, a, b):
    su = 0
    for q in [a-1, a, a+1]:
        for w in [b-1, b, b+1]:
            if li[q][w] == "*":
                su+=1
    return su
x, y = input().split() 
x, y = int(x), int(y)
l = [[j for j in input()] for i in range(x)]
l1 = [[',' for j in range(y+2)] for i in range(x+2)]
for i in range(x):
    for j in range(y):
        l1[i+1][j+1] = l[i][j]
for i in range(1, x+1):
    for j in range(1, y+1):
        if l1[i][j] == '.':
            l1[i][j] = neib(l1, i, j)
for i in range(1, x+1):
    for j in range(1, y+1):
        l[i-1][j-1] = l1[i][j]
for i in range(x):
    print(' '.join(str(j) for j in l[i]))
