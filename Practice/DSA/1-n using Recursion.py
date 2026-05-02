def print_numbers(i,n): # i is the current number and n is the limit

    if i>n: # base case
        return
    
    print(i,end=" \n") # print i and move to next line
    print_numbers(i+1,n)

print_numbers(1,10)