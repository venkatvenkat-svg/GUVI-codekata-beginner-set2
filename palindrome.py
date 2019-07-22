num=input()
num=int(num)
rev=0
temp=num
if(num<=1000):
    while(num!=0):
        rem=num%10
        rev=(rev*10)+rem
        num=num//10
    if(temp==rev):
        print("yes")
    else:
        print("no")
else:
    print("invalid number")
