

# def cube_finder(n):
#     cubes = {}
#     for i in range(1,n+1):
#         cubes[i] = i**3
#     return cubes
# print(cube_finder(int(input("enter a number up to which you whant to print cubes :"))))


# word counter

def wordcounter(word):
    count = {}
    for char in word:
        count[char] = word.count(char)
    return count

print(wordcounter('pratikharidasghadge'))
