den =[200,50,10,5,2,1]
amt = int(input("Enter the amount "))

for i in range (6) :
    count = int(amt / den[i]);
    if count!=0 :
        print(den[i], "x", count, "=" , den[i]*count)
    amt = amt % den[i]    
