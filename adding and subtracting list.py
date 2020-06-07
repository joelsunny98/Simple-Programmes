

    
mat1= []
mat2 = []
r = int(input("enter"))
c = int(input("enter Second" ))

print("Enter elements for mat1")

for i in range(0, r):
    elements = []
    for j in range(0, c):
        elements.append(int(input("enter the element")))
    mat1.append(elements)
print("enter elements for mat2")
for i in range(0, r):
    elements=[]
    for j in range(0, c):
        elements.append(int(input("enter the element")))
    mat2.append(elements)
sum = []
dif = []
for i in range(0,r):
    sumel= []
    difel= []
    for j in range(0,c):
        sumel.append(mat1[i][j] + mat2[i][j])
        difel.append(mat1[i][j] - mat2[i][j])
        sum.append(sumel)
        dif.append(difel)
print(sum)
print(dif)
    
