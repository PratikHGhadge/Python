# define afunction that will take a list of argument as input
# and return list with reverse of every element in that list

def reverse_elements(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements

words = ['abc','xyz','pqr']
print(reverse_elements(words))