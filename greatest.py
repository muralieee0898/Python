a,b,c=map(int,input().split(" "))
if a>b and a>c:
    print(a + "is greater")
elif b>c and b>a:
    print(b,"is greater")
else: 
    print(c,"is greater")
