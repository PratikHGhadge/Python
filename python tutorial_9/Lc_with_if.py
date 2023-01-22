# List comprention with if statment

# numbers = list(range(1,11)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_nums = []
# odd_nums = []
# for i in numbers:
#     if i%2 == 0:
#         even_nums.append(i)
#     elif i%2 != 0:
#         odd_nums.append(i)
# print(even_nums)
# print(odd_nums)

# comprehention method
even_nums = [i for i in range(1,11) if i%2 == 0]
odd_nums = [i for i in range(1,11) if i%2 != 0]
print(even_nums)
print(odd_nums)

