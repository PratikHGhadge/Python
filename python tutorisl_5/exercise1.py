#define a function which will take list of numbers as input
#and returns list of squre of that list



def squre_list(l):
    squre=[]
    for i in l:
        squre.append(i**2)
    return squre
numbers=[1,2,3,4,5,6,7,8,0,9,8,7,6,5,4]
print(squre_list(numbers))