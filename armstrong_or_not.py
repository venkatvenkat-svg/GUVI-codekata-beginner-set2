import math
n=int(input())
if(n<=100000):#setiing the limit of the input to 1 lakh
    {
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
        print("yes")
    else:
        print("no")
    }
else:
    print(no)
