# next fibonacci number
fib = [0, 1]
fib_len = 2

# third fibonacci number
fib = fib + [fib[fib_len + -1] + fib[fib_len + -2]]
fib_len = fib_len + 1

# fourth fibonacci number
fib = fib + [fib[fib_len + -1] + fib[fib_len + -2]]
fib_len = fib_len + 1

# fifth fibonacci number
fib = fib + [fib[fib_len + -1] + fib[fib_len + -2]]
fib_len = fib_len + 1

# sixth fibonacci number
fib = fib + [fib[fib_len + -1] + fib[fib_len + -2]]
fib_len = fib_len + 1

# Print all six
print fib

# Print last fibonacci number
print fib[fib_len + -1]

# Print 2nd fibonacci number
print fib[1]
