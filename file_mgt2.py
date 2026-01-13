# Outsider code insert in a text file

l = []

for i in range(1,31):
    l.append(i)

print(l)

file = open("z-file.txt","a")   # Append a existing code in text file
file.write(str(l))              # For transfer a data it want to convert in a string
file.close()


# from task2 import * <= uses for package it will use to attach a code in different file
# It will also make a package automatic _pyache_