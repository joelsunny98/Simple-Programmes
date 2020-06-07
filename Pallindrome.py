#Test if the given number is a Pallindrome
n = int(input("Enter a number here: "))
o = n
result = 0
while(n >= 1):
    r = n % 10
    result = result*10 + r
    n = n // 10
if(result == o):
    print("It is a Pallindrom")
else:
    print("It is not a Pallindrom")
    
