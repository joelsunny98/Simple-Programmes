#Counts the number of words in a statement 
para = input("Enter your statement here: ")
x = len(para)- 1
word = 0
for i in range(0, len(para)):
    if (para[x] == " " and para[x-1] != " "):
        word = word + 1
    x = x - 1
print(word + 1)
    
