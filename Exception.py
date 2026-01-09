# This is used for the handling of the user side error

# 1) This code is for the wrong input from user side
try:
    n = int(input("Enter a number 1: "))    # The code which has chances to make a error from user side
    n1 = int(input("Enter a number 2: "))

    print(n+n1)
    print("Try executed!!")

except ValueError as e:             # This is a value error if the user can give a wrong input
    print(e)

else:
    print("Else executed!!")        # It was a extra block if there is a try run then it was run

finally:
    print("Finally executed!!")     # It was a extra block and run complusary if try run or not

# 2) This is a wrong input for division
try:
    n = int(input("Enter a number 1:"))
    n1 = int(input("Enter a number 2:"))

    print(n/n1)
    print("Try exectued!!")

except ValueError as e:
    print(e)

except ZeroDivisionError as e:
    print(e)

# 3) This is a used in the wrong index 
try:
    l = [15,25,30]
    n = int(input("Enter a index number: "))
    
    print("The value is: ",l[n])

except ValueError as e:
    print(e)

except IndexError as e:
    print(e)

# 4) For all type of error (in real world this is a used)
try:
    l = [15,20,35]
    n = int(input("Enter a index number: "))

    print("The value is: ",l[n])

except:
    print("Invalid input!!")