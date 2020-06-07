#This code is an example on how to use flags in python
flag = True
n = int(input("Enter"))

for i in range (2, n//2 + 1):
    if(n % i == 0):
        flag = False
        break

if(flag == False):
    print("not Prime")
else:
    print("prime")
