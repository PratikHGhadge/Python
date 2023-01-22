# exercise wath coco movie
#ask users name and age
#if users name start with a or A and age is above 10 then
#print"you canwatch movie
#else print 'YOU CAN NOT WATCH COCO

name=input("enter your name")
age=int(input("enter your age "))

if age>=10 and (name[0]=="a" or name[0]=="A") :
    print("you can watch coco movie ")
else :
    print("you can not watch coco")