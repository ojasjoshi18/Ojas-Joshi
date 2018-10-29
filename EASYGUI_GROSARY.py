#Ojas Joshi
#Division-M
#Roll no:23
#Gr no:11810839
from easygui import *                                                          #All functions of easygui are imported
import sys
while 1:
   msgbox("Hello,welcome to the supermarket!!")                                #Welcome 
   l=[]                                                                        #Emplty list declared for billing
   while 1:                                                                    #While loop introduced to allow multiple products to be selected
     msg="What do you want to buy?"
     title="A1 SUPERMARKET"
     choices=["CHOCOLATES","BISCUITS","SOAPS","CLOTHS"]                        #List of comodities available for purchase
     
     choice=choicebox(msg,title,choices)
     if str(choice)=="CHOCOLATES":                                             #Item selection
        msg1="Which chocolates do you want?"
        msg2="Which vendor would you like?"
        title1="CHOCOLATES"
        choice1=["DairyMilk","Hersheys","Nutella","Kitkat","Gems"]             #Various chocolates
        choicev=["Fastship","ekart","quickdelivery"]
        choice2=choicebox(msg1,title1,choice1)
        choice3=choicebox(msg2,title1,choice2)
         
        if choice2=="Kitkat":
            if choice3=="Fastship":
               a=5                                                                 #This denotes the price of above selected commodity(a-t)
            elif choice3=="ekart":
                 a=7
            else:
                 a=8
            msgbox(msg=str(a),title="Price of Kitkat")
            l.append(a)                                                         #Price is appended to the empty list which is used for billing
                 
        elif choice2=="DairyMilk":
             if choice3=="Fastship":
                b=10
             elif choice3=="ekart":
                  b=15
             else:
                  b=13
             msgbox(msg=str(b),title="price of DairyMilk")
             l.append(b)
        elif choice2=="Hersheys":
             if choice3=="Fastship":
                c=50
             elif choice3=="ekart":
                  c=72
             else:
                  c=52
             msgbox(msg=str(c),title="price of Hersheys")
             l.append(c) 
        elif choice2=="Nutella":
             if choice3=="Fastship":
                d=100
             elif choice3=="ekart":
                  d=109
             else:
                  d=119
             msgbox(msg=str(d),title="price of Nutella")
             l.append(d) 
        else:
             if choice3=="Fastship":
                e=25
             elif choice3=="ekart":
                  e=11
             else:
                  e=19
             msgbox(msg=str(e),title="price of Gems")
             l.append(e) 
 
     elif str(choice)=="BISCUITS":
          msg2="Which biscuits do you want?"
          title2="BISCUITS"
          choice3=["ParleG","Hide and Seek","Bourbon","Monaco","Marie"]
          choice4=choicebox(msg2,title2,choice3)
          if choice4=="ParleG":
               if choice3=="Fastship":
                f=25
               elif choice3=="ekart":
                  f=19
               else:
                  f=15
               msgbox(msg=str(f),title="Price of ParleG")
               l.append(f)
          elif choice4=="Hide and Seek":
               if choice3=="Fastship":
                 g=25
               elif choice3=="ekart":
                  g=30
               else:
                  g=20
               msgbox(msg=str(g),title="price of Hide and Seek")
               l.append(g)
          elif choice4=="Bourbon":
               if choice3=="Fastship":
                  h=30
               elif choice3=="ekart":
                  h=40
               else:
                  h=29
               msgbox(msg=str(h),title="price of Bourbon")
               l.append(h) 
          elif choice4=="Monaco":
               if choice3=="Fastship":
                i=25
               elif choice3=="ekart":
                  i=20
               else:
                  i=19
               msgbox(msg=str(i),title="price of Monaco")
               l.append(i) 
          else:
               if choice3=="Fastship":
                j=5
               elif choice3=="ekart":
                  j=10
               else:
                  j=8
               msgbox(msg=str(j),title="price of Marie")
               l.append(j) 
 


     elif str(choice)=="SOAPS":
         msg3="Which soaps do you want?"
         title3="SOAPS"
         choice5=["Lux","Dettol","Lifeboy","Pears","Moti"]
         choice6=choicebox(msg3,title3,choice5) 
         if choice6=="Lux":
             if choice3=="Fastship":
                k=50
             elif choice3=="ekart":
                  k=46
             else:
                  k=48
           
             msgbox(msg=str(k),title="Price of Lux")
             l.append(k)
         elif choice6=="Dettol":
             if choice3=="Fastship":
                lo=60
             elif choice3=="ekart":
                  lo=53
             else:
                  lo=60
             
             msgbox(msg=str(lo),title="price of Dettol")
             l.append(lo)
         elif choice6=="Lifeboy":
             if choice3=="Fastship":
                m=30
             elif choice3=="ekart":
                  m=25
             else:
                  m=25
             
             msgbox(msg=str(m),title="price of Lifeboy")
             l.append(m) 
         elif choice6=="Pears":
               if choice3=="Fastship":
                n=49
               elif choice3=="ekart":
                  n=59
               else:
                  n=60
             
               msgbox(msg=str(n),title="price of Pears")
               l.append(n) 
         else:
             if choice3=="Fastship":
                o=80
             elif choice3=="ekart":
                  o=76
             else:
                  o=78
             
             msgbox(msg=str(o),title="price of Moti")
             l.append(o) 

     elif str(choice)=="CLOTHS":
         msg4="Which brand do you want?"
         title4="CLOTHS"
         choice7=["US POLO","CottonKing","Blackberry","Levis","Peter England"]
         choice8=choicebox(msg4,title4,choice7)
         if choice8=="US POLO":
             if choice3=="Fastship":
                p=2500
             elif choice3=="ekart":
                  p=2110
             else:
                  p=1999
           
             msgbox(msg=str(p),title="Price of US POLO")
             l.append(p)
         elif choice6=="Cottonking":
             if choice3=="Fastship":
                q=799
             elif choice3=="ekart":
                  q=776
             else:
                  q=767
             
             msgbox(msg=str(q),title="price of Cottonking")
             l.append(q)
         elif choice6=="Blackberry":
             if choice3=="Fastship":
                r=2499
             elif choice3=="ekart":
                  r=2299
             else:
                  r=2799
             
             msgbox(msg=str(r),title="price of Blackberry")
             l.append(r) 
         elif choice6=="Levis":
             if choice3=="Fastship":
                s=3999
             elif choice3=="ekart":
                  s=3699
             else:
                  s=4299
             
             msgbox(msg=str(s),title="price of Levis")
             l.append(s) 
         else:
             if choice3=="Fastship":
                t=2499
             elif choice3=="ekart":
                  t=2799
             else:
                  t=2699
             
             msgbox(msg=str(t),title="price of Peter England")
             l.append(t) 

     msg="Do you want to continue?"                                                        #Confirmation is asked whether to exit shopping
     title="Please Confirm"
     if ccbox(msg,title):
        pass
     else:
          break
   i=0                                                                                    #Billing to the above selected commodities
   sum=0
   for i in l:
      sum+=i
      
      
   msgbox(str(sum),"Total Cost","Result")                                                 #Total cost is shown
   msg="Do you want to shop again?"                                                       #Conformation for exit
   title="Please Confirm"
   if ccbox(msg,title):
        pass
   else:
          sys.exit()                                                                      #Exit
