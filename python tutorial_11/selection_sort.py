def Selection():
    for i in range(n-1):
        for j in range(i+1,n):
            if(a[i]>a[j]):
                t=a[i]
                a[i]=a[j]
                a[j]=t
    print("percentage marks in ascending order :")
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
Selection()