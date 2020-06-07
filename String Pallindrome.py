#Pallindrome test for strings
name = input("Enter a word here: ")
rev = name[ : : -1]

if (name == rev):
    print("This String is a pallindrome")
else:
    print("This String is not a pallindrome")
