i =0
"""while(True):
    if i+1<5:
        i=i+1
        continue
    print(i+1, end="     ")
    if(i==44):
        break #stop the loop
    i=i+1"""


while(True):
    inp=int(input("enter the number\n"))
    if inp>100:
        print("congrats you enterd a number greater than 100\n")
        break
    else:
        print("try again\n")
        continue