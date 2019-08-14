# program to find hypotenuse
import math
a = float(input("Enter the first side "))
b = float(input("Enter the second side "))
if a>0 and b>0:
 c = math.sqrt(a*a + b*b)
 print("The hypotenuse is",c )

else:
    print ("Invalid input")

