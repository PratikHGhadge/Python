# if elif else statment
#
#     show ticket pricing
# 1 to 3 (free)
# 4 to 10 (150)
# 11 to 69 (200)

age = int(input("please input your age "))
if 0<age<=3 :
    print("ticket is free : ")
elif 3<age<=10 :
    print("ticket price : 150 ")
elif 10<age<=60 :
    print("ticket price is : 250")
else:
    print("ticket price : 200")