# Simple if-else
a=int(input("Enter a number 1: "))
b=int(input("Enter a number 2: "))

if a>b:
    print(a,"is greatest")

else:
    print(b,"is greatest")

# if-else Ladder
# program no1

age=int(input("Enter a age: "))

if age>=100:
    print("Invaid age!!")

elif age>=18:
    print("Eligible for vote!!")

else:
    print("Not eligible for vote")

# program no2

n=int(input("Enter a number: "))

if n==0:
    print("Number is zero!!")

elif n%2==0:
    print("Number is even")

else:
    print("Number is odd")

# nested if-else
# program no1

n1=int(input("Enter a number 1: "))
n2=int(input("Enter a number 2: "))
n3=int(input("Enter a number 3: "))

if n1>n2:
    if n1>n3:
        print(n1,"is greatest")

    else:
        print(n3,"is greatest")

else:
    if n2>n3:
        print(n2,"is greatest")
    else:
        print(n3,"is greatest")