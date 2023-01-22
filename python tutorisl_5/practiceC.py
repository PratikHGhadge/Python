num = [2,5,9,7,33,66,44,55]
print(min(num))
print(max(num))

def greatest_diff(l):
    return max(l)-min(l)

print(greatest_diff(num))