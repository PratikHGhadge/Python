def Bsearch():
    key = int(input("Enter Roll No to search "))
    L = 0
    H = n-1
    while(L <= H):
        M = int((L+H)/2)
        if(key == a[M]):
            print("Roll No is present")
            break
        elif(key > a[M]):
            L = M+1
        else:
            H = M-1
    if(L > H):
        print("Roll NO is absent")


a = []
n = int(input("Enter how many student attended training program :"))
for i in range(n):
    ele = int(input("Enter Roll No :"))
    a.append(ele)
print("Student who attended training program :")
for i in range(n):
    print(a[i])
Bsearch()
