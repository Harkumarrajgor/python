# This is a armstorng number
# Ex:- 153 is a armstrong number 

n=int(input("Enter a number: "))
arm=0
rem=0
n1=n
while(n!=0):
    rem=n%10
    arm=arm+rem*rem*rem
    n=n//10     # Two slash(//) are compulsary

if n1==arm:
    print("Number is armstrong")
else:
    print("Number is not armstrong")