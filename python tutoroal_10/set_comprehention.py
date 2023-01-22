# set comprehention
s = {k**2 for k in range(1,11)}
print(s)

name = {'pratik','pravin','ravan'}
first = {names[0] for names in name}
print(first)