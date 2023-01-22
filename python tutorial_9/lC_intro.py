# List comprehension
# with the help of list comprehention we can creat list in one line

# creat a list of squre frome 1 to 10

# squres = []   # by basic way
# for i in range(1,11):
#     squres.append(i**2)
# print(squres)
#
# squres2 = [i**2 for i in range(1,int(input("enter number up to which you "
#                                            "whant to print squres :"))+1)]  # by list comprehention way
# print(squres2)

# print numbers from -1 to -10

# negative = []
# for i in range(1,11):
#     negative.append(-i)
# print(negative)
#
# negative1 = [-i for i in range(1,11)]
# print(negative1)

names = ['pratik','pravin','mayur']
# new_list = ['p','p','m']
new_list = []
for name in names:
    new_list.append(name[0])
print(new_list)

new_list1 = [name[0] for name in names]
print(new_list1)






# x, y, z, n = (int(input("enter number :")) for i in range(1,5)) # use this for taking multiple inputs in one line
# print("multiplecation of all num is",x*y*z*n)