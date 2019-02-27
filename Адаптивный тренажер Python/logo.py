n = int(input())
logo = ('''[:::::[    CODE THE WORLD    ]:::::]
[:::::[www.itmathrepetitor.ru]:::::]''')
for i in range(n):
    if n < 8:
        print("ERROR")
        break
    if i == 0 or i == n-1:
        print('[[[[[[[[[[[[[[[    ]]]]]]]]]]]]]]]]]')
    elif i == n//2:
        print(logo)
    elif i <= n//4 or i >= n*3//4:
        print('[::::::::::::::    ::::::::::::::::]')
    else:
        print('[:::::[                      ]:::::]')
        
        
