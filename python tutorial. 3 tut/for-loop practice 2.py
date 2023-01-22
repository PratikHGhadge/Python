# practice for loop
# ask a user name and count each character
# "pratik ghadge"
#  Ex p:1
#     R:1

name = input("enter your name :")
temp=""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}:{name.count(name[i])}")
        temp+=name[i]
