# Introduction and methods of tuple

t = (1,2,1,1,"Hello","why",True,16.88)

print(type(t))          # type is tuple

print(t.count(1))       # find the value how much times in tuple
print(t.index(2))       # finding index using value

z = list(t)             # changing type as list
print(type(z))