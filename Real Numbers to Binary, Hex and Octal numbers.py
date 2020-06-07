desire = input("Into which number system do you want the number converted to? Binary/octal/Hexadeimcal")
l1 = []
if(desire == "binary"):
    n = int(input("Enter the number here: "))
    
    while (n >= 1):
        remainder =int( n % 2 )
        l1.append(remainder)
        n = n / 2
    l1 = l1[ : :-1]
    print(l1)
    
elif(desire == "octal"):
    num = int(input("Enter the number here: "))
    while (num >= 1):
        remainder =int( num % 8 )
        l1.append(remainder)
        num = num / 8
    l1 = l1[ : :-1]

    print("Your Octal Number is", l1)

elif(desire == "hexadecimal"):
    num1 = int(input("Enter the number here: "))
    while(num1 >= 1):
        remainder = int( num1 % 16)
        if (remainder <= 1 and remainder >= 9 ):
            l1.append( remainder )
        elif(remainder == 10):
            l1.append("A")
        elif(remainder == 11):
            l1.append("B")
        elif(remainder == 12):
            l1.append("C")
        elif(remainder == 13):
            l1.append("D")
        elif(remainder == 14):
            l1.append("E")
        elif(remainder == 15):
            l1.append("F")
    
            
        num1 = num1 / 16
    l1 = l1[ : :-1]
    print("Your Hexadecimal number is: ", l1)

else:
    print("You have not entered a valid option")







