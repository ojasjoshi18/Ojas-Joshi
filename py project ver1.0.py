# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 20:02:00 2018

@author: Ojas
"""

#Ojas Joshi
#Division-M
#Roll no:23
#Gr no:11810839
from easygui import *                                                          #All functions of easygui are imported
import sys
while 1:
  l=[]                                                                        #Emplty list declared for billing
  while 1:                                                                  #While loop introduced to allow multiple products to be selected
    msg="What do you want to buy?"
    title="A1 SUPERMARKET"
    choices=["CHOCOLATES","BISCUITS","SOAPS","CLOTHS"]                        #List of comodities available for purchase
    choice=choicebox(msg,title,choices)
    while str(choice)=="CHOCOLATES":                                             #Item selection
      msg1="Which chocolates do you want?"
      msg2="Which vendor would you like?"
      title1="CHOCOLATES"
      choice1=["DairyMilk","Hersheys","Nutella","Kitkat","Gems"]             #Various chocolates
      choicev=["Fastship","ekart","quickdelivery"]
      choice2=choicebox(msg1,title1,choice1)
      choice3=choicebox(msg2,title1,choicev)
      if choice2=="Kitkat":
            if choice3=="Fastship=5":
               a=5                                                                 #This denotes the price of above selected commodity(a-t)
            elif choice3=="ekart=7":
                 a=7
            else:
                 a=8
            l.append(a)                                                         #Price is appended to the empty list which is used for billing
      elif choice2=="DairyMilk":
             if choice3=="Fastship":
                b=10
             elif choice3=="ekart":
                  b=15
             else:
                  b=13
             l.append(b)
      elif choice2=="Hersheys":
             if choice3=="Fastship":
                c=50
             elif choice3=="ekart":
                  c=72
             else:
                  c=52
             l.append(c) 
      elif choice2=="Nutella":
             if choice3=="Fastship":
                d=100
             elif choice3=="ekart":
                  d=109
             else:
                  d=119
             l.append(d) 
      else:
             if choice3=="Fastship":
                e=25
             elif choice3=="ekart":
                  e=11
             else:
                  e=19
             l.append(e) 
      break
     
    while str(choice)=="BISCUITS":
           msg2="Which biscuits do you want?"
           title2="BISCUITS"
           choice3=["ParleG","Hide and Seek","Bourbon","Monaco","Marie"]
           choicev=["Fastship","ekart","quickdelivery"]
           choice4=choicebox(msg2,title2,choice3)
           choice5=choicebox(msg,title2,choicev)
           if choice4=="ParleG":
               if choice5=="Fastship":
                f=25
               elif choice5=="ekart":
                  f=19
               else:
                  f=15
               l.append(f)
           elif choice4=="Hide and Seek":
               if choice5=="Fastship":
                 g=25
               elif choice5=="ekart":
                  g=30
               else:
                  g=20
               l.append(g)
           elif choice4=="Bourbon":
             if choice5=="Fastship":
                  h=30
             elif choice5=="ekart":
                  h=40
             else:
                  h=29
             l.append(h) 
           elif choice4=="Monaco":
             if choice5=="Fastship":
                i=25
             elif choice5=="ekart":
                  i=20
             else:
                  i=19
             
             l.append(i) 
           else:
             if choice5=="Fastship":
                j=5
             elif choice5=="ekart":
                  j=10
             else:
                  j=8
             l.append(j) 
           break
    
    while str(choice)=="SOAPS":
          msg3="Which soaps do you want?"
          title3="SOAPS"
          choice5=["Lux","Dettol","Lifeboy","Pears","Moti"]
          choicev=["Fastship","ekart","quickdelivery"]
          choice6=choicebox(msg3,title3,choice5)
          choice7=choicebox(msg3,title3,choicev)
          if choice6=="Lux":
             if choice7=="Fastship":
                k=50
             elif choice7=="ekart":
                  k=46
             else:
                  k=48
             l.append(k)
          elif choice6=="Dettol":
             if choice7=="Fastship":
                lo=60
             elif choice7=="ekart":
                  lo=53
             else:
                  lo=60
             l.append(lo)
          elif choice6=="Lifeboy":
             if choice7=="Fastship":
                m=30
             elif choice7=="ekart":
                  m=25
             else:
                  m=25
             l.append(m) 
          elif choice6=="Pears":
               if choice7=="Fastship":
                n=49
               elif choice7=="ekart":
                  n=59
               else:
                  n=60
               l.append(n) 
          else:
             if choice7=="Fastship":
                o=80
             elif choice7=="ekart":
                  o=76
             else:
                  o=78
             l.append(o) 
          break
    
    while str(choice)=="CLOTHS":
          msg4="Which brand do you want?"
          title4="CLOTHS"
          choice7=["US POLO","CottonKing","Blackberry","Levis","Peter England"]
          choicev=["Fastship","ekart","quickdelivery"]
          choice3=choicebox(msg4,title4,choice7)
          choice8=choicebox(msg4,title4,choicev)
          if choice3=="US POLO":
             if choice8=="Fastship":
                p=2500
             elif choice8=="ekart":
                  p=2110
             else:
                  p=1999
             l.append(p)
          elif choice3=="Cottonking":
             if choice8=="Fastship":
                q=799
             elif choice8=="ekart":
                  q=776
             else:
                  q=767   
             l.append(q)
          elif choice3=="Blackberry":
             if choice8=="Fastship":
                r=2499
             elif choice8=="ekart":
                  r=2299
             else:
                  r=2799
             l.append(r) 
          elif choice3=="Levis":
             if choice8=="Fastship":
                s=3999
             elif choice8=="ekart":
                  s=3699
             else:
                  s=4299
             l.append(s) 
          else:
             if choice8=="Fastship":
                t=2499
             elif choice8=="ekart":
                  t=2799
             else:
                  t=2699
             l.append(t)
          break
    else:
        pass
        msg="Do you want to continue?"                                                        #Confirmation is asked whether to exit shopping
        title="Please Confirm"
        if ccbox(msg,title):
          pass
        else:
          break
    break
  break
a3=0
i=0                                                                                    #Billing to the above selected commodities
sum=0
for i in l:
 sum+=i
 a2=sum
y=[]
a1=0
if ccbox("Would you like to participate in a quiz?","*DISCOUNT ALERT*"):
      msgbox(msg="The following quiz will give you an opprtunity of grab exciting discounts*",title="Quiz")
      msg1="Who is the speaker of RajyaSabha?"
      title1=""
      choice1=("Sumitra Mahajan","PJ Kurien","Narendra Modi","V Naidu")
      Assa=buttonbox(msg1,title1,choices=choice1)
      if Assa=="Sumitra Mahajan":
         a1+=1
         y.append(a1)
      else: 
           pass
      msg2="With which country has the Rafael deal been signed?"
      title2=""
      choice2=("France","Italy","Russia","Germany")
      Asaa=buttonbox(msg2,title2,choices=choice2)
      if Asaa=="France":
        a1+=1
        y.append(a1)
      else: 
         pass
      msg3="Which movie won the Academy Award in 2018?"
      title3=""
      choice3=("Dunkirk","The Shape of Water","La La Land","The Silent Child")
      Asa=buttonbox(msg3,title3,choices=choice3)
      if Asa=="The Shape of Water":
        a1+=1
        y.append(a1)
      else: 
          pass
      msg5="Who was the first person to reach North Pole?"
      title5=""
      choice5=("Charles Hilary","Johan Don","Robert Peary","Rajesh Sharma")
      As=buttonbox(msg5,title5,choices=choice5)
      if As=="Robert Peary":
        a1+=1
        y.append(a1)
      else: 
       pass
      if a1==4:
       msgbox(msg="Congratulations!! You have got all answers Correct!! You get a discount of 5% on your total purchase",title="")
       a3=(a2*0.05)
      else:
        msgbox("Sorry you have lost the quiz","")
from Tkinter import *
import random
def roll():    
    r = random.randint(1, 6)
    s=str(r)
    e.delete(0, END)
    e.insert(0, s)    
root = Tk()
root.geometry("100x100")
label = Label(root, text="Dice Roller")
e = Entry(root, width=10)
button1 = Button(root, text="Click to roll the dice", fg="blue", command=roll)
label.grid(row=0)
e.grid(row=1)
button1.grid(row=2)
root.mainloop()
a4=0
if s=="6":
    a4=(a2*0.05)
A=a2-(a3+a4)
print("Total Cost is:",A,"Discount from Quiz:",a3,"Discount from Luckdraw:",a4)                                                 #Total cost is shown
                        