#Name:Ojas Joshi
#Gr no:11810839
#roll no:23
#Division:M
n1=0                                                         #First term in the series is always 0
n2=1                                                         #Second term in the series is always one
n3=0
count=0
times=int(input('Enter number of times you want'))           #Total terms in fibonacci series
print(n2)
while count<(times-1):
    n3=n1+n2                                                 #next number is sum of previous two numbers
    print(n3)
    n1=n2
    n2=n3
    count+=1
