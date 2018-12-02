#Name:Ojas Joshi
#Gr no:11810839
#roll no:23
#Division:M
def armstrong(n):                                #function to define armstrong number
    sum=0
    t=n
    while t>0:
        d=t%10                                   #Separating out the number into indiviual digits
        sum=t**3                                 #cube of the digits is found out
        t=t//10
    return sum
n=int(input("Enter a number"))                   #user input number is taken    
y=armstrong(n)                                   #function is called        
print(y)              
