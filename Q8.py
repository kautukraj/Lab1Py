import sys

print ("Select the type of computation -\n" \
        "1. Add\n" \
        "2. Multiply\n" \
        "3. Average\n")
      
ch = input("Select one of 1,2,3 ") 
if ch=='1' or ch=='2' or ch=='3' :
    n1 = float(input("Enter first number: ")) 
    n2 = float(input("Enter second number: ")) 
  
    if ch == '1': 
      print(n1 ,"+" ,n2 ,"=" ,(n1+n2))
      sys.exit(0)
  
    elif ch == '2': 
      print(n1 ,"x", n2 ,"=" ,(n1*n2))
      sys.exit(0)
  
    elif ch == '3': 
      print("Average of", n1, "and", n2, "is", (n1+n2)/2 )
      sys.exit(0)
  
else: 
    print("Invalid input") 

