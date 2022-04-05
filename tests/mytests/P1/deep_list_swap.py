# deep list swap
# output:
# [1, 2, 3]
# [4, 5, 6]
# [4, 5, 6]
# [1, 2, 3]
a = [1, 2, 3]
b = [4, 5, 6]
print a
print b
tmp = a[0]
a[0] = b[0]
b[0] = tmp
tmp = a[1]
a[1] = b[1]
b[1] = tmp
tmp = a[2]
a[2] = b[2]
b[2] = tmp
print a 
print b
