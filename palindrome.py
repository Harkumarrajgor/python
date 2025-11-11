# palindrome a number 

n=int(input("Enter a number: "))
rev=0
rem=0
n1=n
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10     # Two slash(//) are compulsary

print(rev)

if n1==rev:
    print("Number is palindrome")
else:
    print("Numeber is not palindrome")