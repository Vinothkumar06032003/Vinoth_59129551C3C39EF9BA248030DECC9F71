def isLeap(year):                                               
	if(year % 4 ==0 and year % 100 != 0) or year % 400 == 0:    
		return(True)
	else :
		return(False)



year=int(input("Enter a year : "))                          
if isLeap(year):                                               
	print("the year {} is a leap year.".format(year))           
else :
	print("the year {} is not a leap year.".format(year))       

