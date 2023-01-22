# area of trangle

a=int(input("enter valu of first side of trangal :"))
b=int(input("enter valu of second side of trangle :"))
c=int(input("enter valu of third side of trangle :"))
s=int((a+b+c)/2)
print("this are the sides of trangle ", a,b,c)
print(s)
area= (s*(s-a)*(s-b)*(s-c))**0.5
print("area of trangle is :", area)