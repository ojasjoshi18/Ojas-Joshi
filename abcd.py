from easygui import *                                                          #All functions of easygui are imported
import sys
choicev=[]
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
        choice3=choicebox(msg2,title1,choicev)
         
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
          msg3="Which biscuits do you want?"
          msg4="Which vendor would you like?"
          title2="BISCUITS"
          choice4=["ParleG","Hide and Seek","Bourbon","Monaco","Marie"]
          choicev=["Fastship","ekart","quickdelivery"]          
          choice5=choicebox(msg3,title2,choice4)
          choice6=choicebox(msg4,title2,choicev)
          if choice5=="ParleG":
               if choice6=="Fastship":
                f=25
               elif choice6=="ekart":
                  f=19
               else:
                  f=15
               msgbox(msg=str(f),title="Price of ParleG")
               l.append(f)
          elif choice5=="Hide and Seek":
               if choice6=="Fastship":
                 g=25
               elif choice6=="ekart":
                  g=30
               else:
                  g=20
               msgbox(msg=str(g),title="price of Hide and Seek")
               l.append(g)
          elif choice5=="Bourbon":
               if choice6=="Fastship":
                  h=30
               elif choice6=="ekart":
                  h=40
               else:
                  h=29
               msgbox(msg=str(h),title="price of Bourbon")
               l.append(h) 
          elif choice5=="Monaco":
               if choice6=="Fastship":
                i=25
               elif choice6=="ekart":
                  i=20
               else:
                  i=19
               msgbox(msg=str(i),title="price of Monaco")
               l.append(i) 
          else:
               if choice6=="Fastship":
                 j=5
               elif choice6=="ekart":
                  j=10
               else:
                  j=8
               l.append(j)
               msgbox(msg=str(j),title="price of Marie")
                
 


     elif str(choice)=="SOAPS":
         msg5="Which soaps do you want?"
         msg6="Which vendor would you like?"
         choicev=["Fastship","ekart","quickdelivery"]
         title3="SOAPS"
         choice7=["Lux","Dettol","Lifeboy","Pears","Moti"]
         choice8=choicebox(msg5,title3,choice7)
         choice9 =choicebox(msg6,title3,choicev)
         if choice8=="Lux":
             if choice9=="Fastship":
                k=50
             elif choice9=="ekart":
                  k=46
             else:
                  k=48
           
             msgbox(msg=str(k),title="Price of Lux")
             l.append(k)
         elif choice8=="Dettol":
             if choice9=="Fastship":
                lo=60
             elif choice9=="ekart":
                  lo=53
             else:
                  lo=60
             
             msgbox(msg=str(lo),title="price of Dettol")
             l.append(lo)
         elif choice8=="Lifeboy":
             if choice9=="Fastship":
                m=30
             elif choice9=="ekart":
                  m=25
             else:
                  m=25
             
             msgbox(msg=str(m),title="price of Lifeboy")
             l.append(m) 
         elif choice8=="Pears":
               if choice9=="Fastship":
                n=49
               elif choice9=="ekart":
                  n=59
               else:
                  n=60
             
               msgbox(msg=str(n),title="price of Pears")
               l.append(n) 
         else:
             if choice9=="Fastship":
                o=80
             elif choice9=="ekart":
                  o=76
             else:
                  o=78
             
             msgbox(msg=str(o),title="price of Moti")
             l.append(o) 

     else:
         msg7="Which brand do you want?"
         msg8="Which vendor would you like?"
         title4="CLOTHS"
         choice10=["US POLO","CottonKing","Blackberry","Levis","Peter England"]
         choicev=["Fastship","ekart","quickdelivery"]
         choice11=choicebox(msg7,title4,choice10)
         choice12=choicebox(msg8,title4,choicev)
         if choice11=="US POLO":
             if choice12=="Fastship":
                p=2500
             elif choice12=="ekart":
                  p=2110
             else:
                  p=1999
           
             msgbox(msg=str(p),title="Price of US POLO")
             l.append(p)
         elif choice11=="Cottonking":
             if choice12=="Fastship":
                q=799
             elif choice12=="ekart":
                  q=776
             else:
                  q=767
             
             msgbox(msg=str(q),title="price of Cottonking")
             l.append(q)
         elif choice11=="Blackberry":
             if choice12=="Fastship":
                r=2499
             elif choice12=="ekart":
                  r=2299
             else:
                  r=2799
             
             msgbox(msg=str(r),title="price of Blackberry")
             l.append(r) 
         elif choice11=="Levis":
             if choice12=="Fastship":
                s=3999
             elif choice12=="ekart":
                  s=3699
             else:
                  s=4299
             
             msgbox(msg=str(s),title="price of Levis")
             l.append(s) 
         else:
             if choice12=="Fastship":
                t=2499
             elif choice12=="ekart":
                  t=2799
             else:
                  t=2699
             
             msgbox(msg=str(t),title="price of Peter England")
             l.append(t)
     if ccbox("Do you want to continue?",""):
        pass
     else:
        break 
     msg=""                                                        #Confirmation is asked whether to exit shopping
     title="Your bill is"
     msgbox(msg=str(a2),title) 
     i=0                                                                                    #Billing to the above selected commodities
     sum=0
     for i in l:
       sum+=i
       a2=sum
    
     msgbox(msg="We have a surprise for you!!",title="SURPRISE")
 
    if ccbox("Would you like to participate in a quiz?","*DISCOUNT ALERT*"):
        msgbox(msg="The following quiz will give you an opprtunity of grab exciting discounts*",title="Quiz")
      y=[]
      a1=0
      msg1="Who is the speaker of RajyaSabha?"
      title1=""
      choice1=("Sumitra Mahajan","PJ Kurien","Narendra Modi","V Naidu")
      buttonbox(msg1,title1,choices=choice1)
      if choices=="Sumitra Mahajan":
         a1+=1
         y.append(a1)
      else: 
           pass
      msg2="With which country has the Rafael deal been signed?"
      title2=""
      choice2=("France","Italy","Russia","Germany")
      buttonbox(msg1,title1,choices=choice2)
      if choices=="France":
        a1+=1
        y.append(a1)
      else: 
          pass
      msg3="Which movie won the Academy Award in 2018?"
      title3=""
      choice3=("Dunkirk","The Shape of Water","La La Land","The Silent Child")
      buttonbox(msg1,title1,choices=choice3)
      if choices=="The Shape of Water":
        a1+=1
        y.append(a1)
      else: 
          pass
      msg5="Who was the first person to reach North Pole?"
      title5=""
      choice5=("Charles Hilary","Johan Don","Robert Peary","Rajesh Sharma")
      buttonbox(msg1,title1,choices=choice5)
      if choices=="":
        a1+=1
        y.append(a1)
      else: 
           pass
    z1=len(y)
    if z1==5:
       msgbox(msg="Congratulations!! You have got all answers Correct!! You get a discount of 5% on your total purchase",title="")
       a2=a2-(a2*0.05)
    else:
       sys.exit()


    msgbox(str(a2),"Total Cost","Result")                                                 #Total cost is shown
    msg="Do you want to shop again?"                                                       #Conformation for exit
    title="Please Confirm"
    if ccbox(msg,title):
         pass
    else:
       sys.exit() 
