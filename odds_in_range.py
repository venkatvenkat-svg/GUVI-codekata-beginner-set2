start, end = map(int, input().split())
  
# iterating each number in list 
for num in range(start+1, end): 
      
    # checking condition 
    if num % 2 != 0: 
        print(num, end = " ") 
