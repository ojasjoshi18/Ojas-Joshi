l=[]                                                    #All entries of list are saved in open list l 
while 1:
    name=input('Enter your name: ')                     #input name
    l.append(name)
    gr_no=int(input('Enter your GR no.: '))             #input gr_no
    l.append(gr_no)
    roll_no=int(input('Enter your Roll no.: '))         #input roll_no       
    l.append(roll_no)
    Eng=int(input('Enter your English marks: '))        #Input English marks
    l.append(Eng)
    Math=int(input('Enter your Math marks: '))          #Input Math marks
    l.append(Math)
    Science=int(input('Enter your Science marks: '))    #Input Science marks
    l.append(Science)
    break
d={}                                                    #All entries of list are save in open dictionary d
while 1:
    d['name']=input('Enter your name: ')
    d['gr_no']=int(input('Enter your gr_no:' ))
    d['roll_no']=int(input('Enter your roll number: '))
    d['Eng']=int(input('Enter your Eng marks: '))
    d['Math']=int(input('Enter your Math marks: '))
    d['Science']=int(input('Enter your Science marks: '))
    break
print(d)
print(l)
