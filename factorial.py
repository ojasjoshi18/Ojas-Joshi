#Name:Ojas Joshi
#Gr no:11810839
#roll no:23
#Division:M
num=int(input())                #The number whose factorial is to be found is taken as input
total=1                         
if num<0:                       #If number is <0 then its factorial does not exist
     print('Please enter a positive number')
elif num==0:                    #If number is zero then its factorial is 1
     print('factorial is 1')
else:
 while num>0:                   #till number is greater than 0 the while loop keeps multipying it with previous number
        total=num*total     
        num=num-1
print("factorial is",total)
    
