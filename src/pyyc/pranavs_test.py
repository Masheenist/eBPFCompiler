# # a = 3#[3,5,7] 
# # def f(b):
# #     d = a
# #     return 21
# # print f(7)

# a = [lambda x: 10]
# print a[0](3)


# a = b if True else c
# if a:
#     print p
# else:
#     print d

# Module(None, 
#        Stmt([
#            Assign([AssName('a', 'OP_ASSIGN')], 
#            IfExp(Name('True'), Name('b'), Name('c'))), 
#            If([
#                (Name('a'), 
#                Stmt([Printnl([Name('p')], 
#                      None)])
#                 )
#               ], 
#               Stmt([Printnl([Name('d')], None)])
#             )]
#         )
#     )

# # THE BELOW TEST WORKS!!!
# b = 3
# c = 4
# d = 5
# a = b+c #a = 7 -> Variable(3)
# # c = -a 
# b = a + -d #b = 2 -> Variable(0)
# c = b+c #c = 6 -> Variable(1)
# d = a + -d #d = 2 -> Variable(2)

# a = b + c
# b = b + c #fails, does b + a...
# b = 3
# c=3

# def f(b):
#     print b
# f(1) <- test to see how calls to custom functions were. it'll be a node like (call, Variable(7), None, Set()), so no need to handle pointers and stuff like that as constants when looking at movs and such. so only if you have an integer as the first arg do you have a const and you can fold

# a = True <- true evaluates to "True", so (movl, True, Variable(0), Set())
# b = False <- false evaluates to "False", so (movl, False, Variable(0), Set())

# ifexp works with optimization
# c = 0
# b = c
# a = 1 if b else 4
# b = 6
# print a

# def f(p):
#     c = 0
#     if c:
#         a = 2 + 3
#         b = 2 + 3
#     else:
#         a = 3 + 4
#         b = 3 + 4
#     print a
#     return b


c = 0
if c:
    a = 2 + 3
    b = 4
    b = 2 + 3
else:
    a = 3 + 4
    b = 3 + 4
print a
print b


# a = 1
# if a:
#     print 3
#     if 0:
#         print 25
#     else:
#         c = 7
# else:
#     print 7
# print 26

# a = 1
# while a != 4:
#     print a
#     a = a+1
# print a

# CHECK THIS ONE, goal is to make sure that eax persists or is destroyed as needed.
# p = 4
# y = 3
# x = 1 #if y else 2
# z = x + y
# g = p(z)
# p(g)

# a = b+c #a = 7 -> Variable(3)
# # c = -a 
# b = a + -d #b = 2 -> Variable(0)
# c = b+c #c = 6 -> Variable(1)
# d = a + -d #d = 2 -> Variable(2)

# b = 10
# print 10