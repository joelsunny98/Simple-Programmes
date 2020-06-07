n = int(input("Enter a number here: "))
s = 0
o = n
while(n >= 1):
    r = n % 10
    print(r)
    s = s + (r * r * r)
    n = n // 10
    
if( o == s):
    print("This is an Armstrong number")
else:
    print("This is not an Armstrong number")
