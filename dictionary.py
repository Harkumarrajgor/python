# Introducition of dictionary and methods

d = {1:"hello",2:"why",3:"welcome"}
print(d)

print(d.get(2))         # get values from index
print(d.items())        # Every items shows together
print(d.keys())         # Print only the keys
print(d.values())       # print only the values

d.update({6:"python",7:"java"})
print(d)                # Extend the value in the tuple

d.pop(2)                # delete the value using the key
print(d)

d.popitem()             # delete the last value
print(d)

t = (56,24,21)          # making a tuple as a keyu
one = {}

print(one.fromkeys(t))  # taken value by defalut as none
print(one.fromkeys(t,6))  # taken value by 6