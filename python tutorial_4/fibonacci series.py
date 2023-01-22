#  fibonacci series
# 0 1 1 2 3 5 8 13 21 ...


# for i in range(1,11):
#    print(i, end=",")

def fibonachi_seq(n):
    a=0   # first no
    b=1   # second no
    if n == 1:
        print(a)
    elif n == 2:
        print(a,b)
    else:
        print(a,b, end=" ")
        for i in range(n-2):
            c = a+b
            a=b
            b=c
            print(b,end=" ")

fibonachi_seq(int(input("enter a number up to print fibonachi series :")))

# second way
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

print(fibonacci(10)) # prints [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
