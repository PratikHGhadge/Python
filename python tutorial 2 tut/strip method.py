name = "    pratik     "
dots = "..............."
# 1strip()method
# print(name+dots)
# print(name.lstrip()+dots) #for remove left speace
# print(name.rstrip()+dots) # for remove right space
# print(name.lstrip().rstrip()+dots)# for remove left and right space
# # # if we have to remove space form sentence
# print(name.replace(" ","")+dots) # for replacing something

#replace() method
#find() method
string= "she is very beautiful and she is good dancer "
# print(string.replace(" ","_"))
# print(string.replace("is","was",1))

is_pos1=string.find("is") #is_pos1    number
print(is_pos1)
is_pos2=string.find("is",is_pos1+1)
print(is_pos2)
