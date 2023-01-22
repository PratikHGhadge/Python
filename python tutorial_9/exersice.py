# difine a function that takes list of strings
# list contaning reverse of every string
# use list comprehention
# example
# l = ['abc','pqr','xyz']
# revers_l = ['cba','rqp','zyx']

# l = ['abc','pqr','xyz']
# revers_l = [i[::-1] for i in l]
# print(revers_l)

def reverse_string(l):
    return [name[::-1] for name in l]
print(reverse_string(['abc','pqr','xyz']))