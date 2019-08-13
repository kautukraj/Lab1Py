print ("Enter the date of birth")
date = int(input())
print ("Enter the month of birth")
month = input()
month = month.lower()

if month == 'december':
         if date < 22:
          sign = 'Sagittarius'
         else:
          sign ='Capricorn'
         
elif month == 'january':
        
        if date < 20:
         sign = 'Capricorn'
        else:
            sign='Aquarius'
        
elif month == 'february':
        
        if date < 19:
         sign = 'Aquarius'
        else:
            sign='Pisces'
        
elif month == 'march':
        
        if date < 21:
         sign = 'Pisces'
        else:
            sign='Aries'
        
elif month == 'april':
        
        if date < 20:
         sign = 'Aries'
        else:
            sign='Taurus'
        
elif month == 'may':
        
        if date < 21:
         sign = 'Taurus'
        else:
           sign= 'Gemini'
elif month == 'june':
        
        if date < 21:
         sign = 'Gemini'
        else:
          sign= 'Cancer'
elif month == 'july':
        
        if date < 23:
         sign = 'Cancer'
        else:
            sign='Leo'
        
elif month == 'august':
        
        if date < 23:
         sign = 'Leo'
        else:
            sign='Virgo'
        
elif month == 'september':
        
        if date < 23:
         sign = 'Virgo'
        else:
            sign='Libra'
        
elif month == 'october':
        
        if date < 23:
         sign = 'Libra'
        else:
            sign='Scorpio'
        
elif month == 'november':
        if date < 22:
         sign = 'Scorpio' 
        else:
            sign='Sagittarius'

print (sign)

        
