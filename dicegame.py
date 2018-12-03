#Name:Ojas Joshi
#Gr no:11810839
#roll no:23
#Division:M 
import random                              #Random function is imported
from random import randint as rt
def game(dice,faces):                      #number of dice and faces are defined withon function 'Game'
    result=0
    for roll in range(0,dice):             #roll is initialised taking values between 0 to dice input
        result+=rt(1,faces)
    return result
dice=int(input())
faces=int(input())
result=game(dice,faces)                    #Game function is called
print(result)
