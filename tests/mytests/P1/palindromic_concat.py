# palindromic concatenation
# Should print "[1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1]"
a = [1, 2, 3]
b = [4, 5, 6]
bprime = [b[2]] + [b[1]] + [b[0]]
aprime = [a[2]] + [a[1]] + [a[0]]
a = a + b + bprime + aprime
print a
