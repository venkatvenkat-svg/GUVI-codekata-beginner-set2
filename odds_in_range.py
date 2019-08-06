start, end = map(int, input().split())#using map function
  
for num in range(start+1, end): 
      
    if num % 2 != 0: 
        print(num, end = " ") 
