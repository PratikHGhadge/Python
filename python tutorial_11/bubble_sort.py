def Buble():
    for i in range(n):
        for j in range(n-1):
            if(a[j]>a[j+1]):
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
    print("Sorted array :")
    for i in range(n):
        print(a[i])

a = []
n = int(input("Enter how many student are :"))
for i in range(n):
    ele = int(input("Enter percentage of student :"))
    a.append(ele)
print("Student along with their percentage marks :")
for i in range(n):
    print(a[i])
Buble()