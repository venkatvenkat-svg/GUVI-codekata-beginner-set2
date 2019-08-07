import math
start, end=map(int,input().split())
for n in range(start,end):
    temp=n
    dc=0
    sum=0
    while(n!=0):
        n=n//10
        dc+=1
    n=temp
    while(n!=0):
        rem=n%10
        sum=sum+pow(rem,dc)
        n//=10
    if(sum==temp):
        print(temp,end=" ")
    

