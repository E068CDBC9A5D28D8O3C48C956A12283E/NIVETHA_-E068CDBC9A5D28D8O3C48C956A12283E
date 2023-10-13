def checkleap (year):

  if((year % 400 == 0) or
     (year % 100 != 0) and
     (year % 4 == 0)):
    print("Given year is a keep year");

  else: 
    print("Given year is not a leap year")

year = int(input("Enter the number:"))

checkleap(year)
    
