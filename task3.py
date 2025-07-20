#7) W.A.P to find the grade according the percentage using if_else ladder
a=int(input("Enter your percentage"))
if(a>=80):
    print("You have distinction")
elif(a<=79 and a>=70):
    print("You have first class")
elif(a<=69 and a>=50):
    print("You have second class")
elif(a<=49 and a>=40):
    print("You have third class")
else:
    print("You are fail !")

#8) W.A.P to find that who can donate the blood using nested if
a=int(input("Enter a weight"))
if(a>50):
    b=int(input("Enter a age"))
if(b>=18):
    print("You are eligible")
else:
    print("You are not eligible for blood dontaion")

# Level 1 questions:-

#1) W.A.P to print in list using simple for loop. List(apple,banana,mango)
one=["apple","banana","mango"]
for i in one:
    print(i)