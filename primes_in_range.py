lower, upper = map(int, input().split())#using map function

for num in range(lower+1,upper):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num,end=" ")
