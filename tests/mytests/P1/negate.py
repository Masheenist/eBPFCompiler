# check_negate
# output: -42
number = input()
x = -number
y = number + -number + -number
z = (not number)  + -number
# textbook p. 41 "And ... contains a list of arguments ... for P1 this list is guaranteed to have length 2"
and1 = x and y
and2 = and1 and z
print and2

