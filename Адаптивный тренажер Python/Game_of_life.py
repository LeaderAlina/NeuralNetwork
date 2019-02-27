def sun(l, a, b):
    su = 0
    if a != x-1 and b != y-1:
        for q in [a-1, a, a+1]:
            for w in [b-1, b, b+1]:
                if l[q][w] == 'x':
                    su+=1
    elif a == x-1 and b !=y-1:
        for q in [a-1, a, 0]:
            for w in [b-1, b, b+1]:
                if l[q][w] == 'x':
                    su+=1
    elif a!=x-1 and b == y-1:
        for q in [a-1, a, a+1]:
            for w in [b-1, b, 0]:
                if l[q][w] == 'x':
                    su+=1
    else:
        for q in [a-1, a, 0]:
            for w in [b-1, b, 0]:
                if l[q][w] == 'x':
                    su+=1
    return su
    
x, y = input().split()
x, y = int(x), int(y)
lis = [[j for j in input()] for i in range(x)]
nextstep = [[' ' for j in range(y)] for i in range(x)]
for i in range(x):
    for j in range(y):
        if lis[i][j] == '.':
            if sun(lis, i, j) == 3:
                nextstep[i][j] = 'x'
            else:
                nextstep[i][j] = '.'
        if lis[i][j] == 'x':
            if (sun(lis, i, j)-1) == 2:
                nextstep[i][j] = 'x'
            elif sun(lis, i, j)-1 == 3:
                nextstep[i][j] = 'x'
            else:
                nextstep[i][j] = '.'
for i in range(x):
    print(' '.join(nextstep[i]))
