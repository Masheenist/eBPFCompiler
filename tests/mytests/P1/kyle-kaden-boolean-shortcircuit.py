t = True
f = False

# input() should not be called since first part is false
print f and input() == 1
# input() should be called since first part is true
print t and input() == 1

# input() should not be called since first part is true
print t or input() == 1
# input() should be called since first part is false
print f or input() == 1