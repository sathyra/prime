 
num = int(input("Enter a number ( greater than 1)"))  
f = 0
i = 2
while i <= num / 2:
    if num % i == 0:
        f=1
        print("The entered number is not a PRIME number")  
        i=i+1
    
if f==0:
    print("The entered number is a PRIME number")

