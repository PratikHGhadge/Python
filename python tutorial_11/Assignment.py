n = int(input("enter total no of student in the class"))
a[]

















#  THIS IS FOR MAX AND MIN MARKS
min=999
for i in range(n):
    if (a[i]!=-1 and a[i]<min):
        min=a[i]
print("Minimum =",min)

max=-1
for i in range(n):
    if(a[i]!=-1 and a[i]>max):
        max=a[i]
print("Maximum valu = ",max)