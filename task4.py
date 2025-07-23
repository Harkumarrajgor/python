#2) W.A.P to find length of string using simple for loop list1(apple,banana,mango)
one=["apple","banana","mango"]
for i in one:
    print(i,' ',(len(i)))

#3) W.A.P to find particular string using simple for loopm list1(apple,banana,mango)
one=["apple","banana","mango"]
for i in one:
    if(i=="apple"):
        print(i)

#4) print a pattern using nested for loop
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()