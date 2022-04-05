a = {}

a[1] = True
b = a
print b is a
print b[1]

a[0] = False
print b[0]
print b is a