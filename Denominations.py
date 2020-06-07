#Enter a number and it will tell the most efficient way to 
#split it across denominations of the Indian Rupee.
amt = int(input("Enter a value here: "))
denom = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
i = 0
while(amt > 0):
    c = amt // denom[i]
    print("%d x %d"%(denom[i], c))
    amt = amt - denom[i] * c
    i = i + 1

   
    

