def Lsearch():
    flag = 0
    key = int(input("Enter Roll No to search :"))
    for i in range(n):
        if(key == a[i]):
            flag = 1
            break
    if (flag == 0):
        print("Roll No is absent")
    else:
        print("Roll no is Present")


a = []
n = int(input("Enter how many student attended training program :"))
for i in range(n):
    ele = int(input("Enter Roll No :"))
    a.append(ele)
print("Student who attended training program :")
for i in range(n):
    print(a[i])
Lsearch()

