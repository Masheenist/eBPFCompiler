d = {1: 2, 3: 4}
a = True
d[1 if a else 3] = input() if a else 25
print d