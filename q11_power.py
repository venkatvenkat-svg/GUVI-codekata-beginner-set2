#general method 
n,e =input().split()
n=int(n)
e=int(e)
if (n>0):
    power=n**e
    print(power)
else:
     print("invalid")
#alternate method using math lib
"""
import math
n,e =input().split()
n=int(n)
e=int(e)
p=math.pow(n,e)
print(p)
"""
