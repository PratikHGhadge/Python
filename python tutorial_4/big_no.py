# take two number input and find out which number is big

a=int(input("enter a first number :"))
b=int(input("enter a second number :"))

def big_no(a,b):
    if a>b:
        return f"{a} is big"
    return f"{b} is big"

print(big_no(a,b))