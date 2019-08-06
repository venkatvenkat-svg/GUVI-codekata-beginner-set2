N=int(input())
if(N<=1000):
   count=0
   for fact in range(1,N+1):
      if(N%fact==0):
         count=count+1
   if (count==2):
      print("yes")
   else:
      print("no")
else:
   print("no")
