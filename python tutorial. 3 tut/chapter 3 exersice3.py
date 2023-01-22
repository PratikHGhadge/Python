# problem
# ask user to input a number containing more than one digit
# example - 1256
# calculate 1+2+5+6 and print

num=input("enter a number containing more than one digit:")

total=0
i=0
while i<len(num):
    total+=int(num[i])
    i+=1
    print(total)