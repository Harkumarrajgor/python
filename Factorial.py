# This sum is for factorial

fact=1
i=1

n=int(input("Enter a number: "))

while i<=n:
    fact=fact*i

    i=i+1
print("Factorial is: ",fact)

# This is factorial for using for loop
a=int(input("Enter a number: "))

fact=1
for i in range(1,a+1,1):
    fact=fact*i

print(fact)