# # set data type
# # unorderd collection of unique items
# s = {1,2,3,4,4,4,4}
# s.add(5)
# s.add(6)
# s.remove(1)
# s.discard(4)
# # s.clear()
# s1 = s.copy()
# print(s1)
#
# l = [1,2,3,3,2,2,5,4,6,7,8,8,6]
# #remove dupliciat
# s2 = list(set(l))
# print(s2)
#
# s3 = {1,1.1,1.0,'str'}
# print(s3)

# more about set
# in keywords in set and for loop
s = {'a','b','c'}
# in key words to chek item is present in set or not
if 'a' in set(s):
    print("present")
else:
    print("absent")


# for loop
for item in s:
    print(item)

# set maths
a1 = {1,2,3,4}
a2 = {3,4,5,6}

union_set = a1|a2 # union
print(union_set)
print(a1 & a2)# intersection