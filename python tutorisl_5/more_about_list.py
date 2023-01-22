#generate list with the help of range fuction
#somthing more about pop method
#index method
#pass list to a function

# number = list(range(1,11))
number = [1,3,4,5,6,76,8,88,66,5,43,55]
# poped_item=number.pop()
# print(number)
# print(number.index(8))

def negativ_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative

print(negativ_list(number))