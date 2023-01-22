# list compretion with if else
nums = [1,2,3,4,5,6,7,8,9,10]
# if number is odd make it -ve and if num is even multiply it by 2
new_list = [i*2 if (i%2 == 0) else (-i) for i in nums]
print(new_list)
