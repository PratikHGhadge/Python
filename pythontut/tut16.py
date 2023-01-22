#list1 = [ ["harry",1],["larry",5],["boary",3],["chori",360] ]
#dict1=dict(list1)
#print(dict1)
#for item, lollypop in dict1.items():
#    print(item,"and lolly is",lollypop)
# print(item)
items=[int,float,"harry",5,6,78,34,2,64,8]
for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)