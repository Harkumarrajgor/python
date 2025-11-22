# The program show for loop
# 1) This is use to print number

for i in range(1,11,1):
    print(i)
print(" ")

# 2) This is use to print number in reverse 

for i in range(10,0,-1):
    print(i)

# 3) This is use to print number dynamically

n = int(input("Enter a number: "))

for i in range(1,n+1):
    print(i)

# 4) This is use to print number reverse dynamically

n = int(input("Enter a number: "))

for i in range(n,0,-1):
    print(i)