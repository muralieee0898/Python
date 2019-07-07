N,A,D=map(int,input().split(" "))
sum=0
for i in range(1,N+1):
    sum=sum+A
    A=A+D
print(sum)
