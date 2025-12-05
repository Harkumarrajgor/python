#   Create a function and do a reverse number

# Type 1- function without parameters without reutrn type

def fun1():          # define a function
    n=int(input("Enter a number: "))

    rev=0
    rem=0

    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n//=10

    print(rev)

fun1()              # calling a function

# Type 2- function with paramters without return type

# static function
def add(a,b):       # parameter
    print(a+b)

add(10,20)          # arguments

# dynamic function
def add(a,b):       # parameter
    print(a+b)

a1=int(input("Enter a number: "))
b1=int(input("Enter a number: "))
add(a1,b1)          # arguments

# Type 3-  function without parameters with reutrn type

def fun():
    n = int(input("Enter a number: "))
    n1 = int(input("Enter a number: "))

    return n+n1

print(fun())

def fac():
    n = int(input("Enter a number: "))
    fact=1

    for i in range(1,n+1):
        fact = fact*i

    return fact

print(fac())

# Type 4-  function with paramaters and with return type

def fun(a,b):

    return a+b

n=10
m=20
print(fun(n,m)) 