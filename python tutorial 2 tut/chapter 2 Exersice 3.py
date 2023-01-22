# take two comma sepreated inputs from user
# 1) users name
# 2)a singal charecter ,

# output - 2 pdrint lines
# 1) users name lenth
# 2) count the character that usre input (bonus : case insensitive count )

name,character=input("enter your full name and one character ").split(",")

a=print(len(name))
print(a)
print(f"charecter count :{name.lower().count(character.lower())}")


