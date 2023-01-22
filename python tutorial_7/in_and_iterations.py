# chek if any key exist in dictionari
user = {'name':'pratik','age':'18'}
# if 'name' in user:
#     print("present")
# else:
#     print("absent")
#
#
# if '18' in user.values():
#     print("present")
# else:
#     print("absent")
#
# # loops in dictionaries
# for i in user:
#     print(i)

# # loops in dictionaries
# for i in user.values():
#     print(i)

#
# # values method
# user_values = user.values()
# print(type(user_values))


# keys method
# user_keys = user.keys()
# print(user_keys)

# loops in dictionaries
# for i in user :
#     print(user[i])

# items method
# user_items = user.items()
# print(user_items)

for key,valu in user.items():
    print(f"key is {key} and valu is {valu}")