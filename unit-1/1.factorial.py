def fact(num):                      
	if(num ==0 or num ==1):
		return(1)
	else :
		return(num*fact(num-1))     

num=int(input("Enter number : "))  

result=fact(num)                    
print("factorial of number {} is {} .".format(num,result))  
