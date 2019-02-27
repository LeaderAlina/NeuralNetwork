200dic = {1:'I', 2:"II", 3: "III", 4:"VI", 5:"V", 6:"IV", 7:"IIV", 8:"IIIV", 9:"XI",
       10:"X", 20:"XX", 30:"XXX",40:"LX",50:'L', 60:"XL", 70:"XXL",80:"XXXL",90:"CX",
       100:"C",200:"CC",300:"CCC",400:"DC",500:"D", 600:'CD',700:'CCD', 800:'CCCD', 900:'MC',
       1000:'M', 2000:'MM', 3000:'MMM', 0:''}
n = int(input())
l = len(str(n))
s = ''
for i in range(l):
    w = n%(10**(i+1))//(10**i)*10**i
    s = s+dic[w]
print(s[::-1])
