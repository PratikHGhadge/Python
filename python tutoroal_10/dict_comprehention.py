# dictionari comprehntion
# squre = {1:1,2:4,3:9}
# squre = {f"squre of {num}":num**2 for num in range(1,11)}
# for k,v in squre.items():
#     print(f"{k} : {v}")


string = "Harshit"
word_count = {char : string.count(char) for char in string}
print(word_count)