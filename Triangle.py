 #This will return if the a triangle with give 
 #specifications is Equilateral, Isoselus or Scalene
 s1 = int(input("Enter length of side #1: "))
s2 = int(input("Enter length of side #2: "))
s3 = int(input("Enter length of side #3: "))

if ((s1 + s2) > s3 and (s2 + s3) > s1 and (s1 + s3) > s2 ):
    print("invalid values")
elif (s1 == s2 and s2 == s3):
    tri = "Equilateral"
elif(s1 == s2 or s2 ==3 or s3 == s1):
    tri = "Isoselus"
else:
    tri ="Scalene"
    
print(tri)
