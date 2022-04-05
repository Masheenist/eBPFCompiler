import compiler
from compiler.ast import *

# Module(None, Stmt([Assign([AssName('x', 'OP_ASSIGN')], List([Const(5)])), Function(None, 'f', ['b'], [], 0, None, Stmt([Assign([AssName('y', 'OP_ASSIGN')], Const(3)), Assign([Subscript(Name('x'), 'OP_ASSIGN', [Const(0)])], Const(2)), Return(Add((Name('y'), Subscript(Name('x'), 'OP_APPLY', [Const(0)]))))]))]))
test1 = """
x = [5]
def f(b):
    y = 3
    x[0] = 2
    return y+x[0]
"""

# Module(None, Stmt([Assign([AssName('x', 'OP_ASSIGN')], Const(5)), Function(None, 'f', ['x'], [], 0, None, Stmt([Assign([AssName('y', 'OP_ASSIGN')], Const(3)), Return(Add((Name('y'), Name('x'))))]))]))
test2 = """
x = 5
def f(x):
    y = 3
    return y+x
"""

# Module(None, Stmt([Assign([AssName('x', 'OP_ASSIGN')], Const(5)), Function(None, 'f', ['b'], [], 0, None, Stmt([Printnl([Name('x')], None), Assign([AssName('y', 'OP_ASSIGN')], Const(3)), Return(Add((Name('y'), Name('x'))))]))]))
test3 = """
x = 5
def f(b):
    print x
    y = 3
    return y+x
"""

# Module(None, Stmt([Assign([AssName('x', 'OP_ASSIGN')], Const(5)), Function(None, 'f', ['b'], [], 0, None, Stmt([Printnl([Name('x')], None), Assign([AssName('x', 'OP_ASSIGN')], Const(5)), Assign([AssName('y', 'OP_ASSIGN')], Const(3)), Return(Add((Name('y'), Name('x'))))]))]))
test4 = """
x = 4
def f(b):
    print x
    x = 5
    y = 3
    return y+x
"""

# Module(None, Stmt([Assign([AssName('x', 'OP_ASSIGN')], Const(4)), Function(None, 'f', ['b'], [], 0, None, Stmt([Printnl([Name('x')], None), Assign([AssName('x', 'OP_ASSIGN')], Const(5)), Function(None, 'g', ['x'], [], 0, None, Stmt([Assign([AssName('g', 'OP_ASSIGN')], Const(3)), Assign([AssName('x', 'OP_ASSIGN')], Const(2)), Printnl([Name('x')], None)]))]))]))
test5 = """
x = 4
def f(b):
    print x
    x = 5
    def g(x):
        g = 3
        x = 2
        print x
"""

# Module(None, Stmt([Assign([AssName('x', 'OP_ASSIGN')], Const(4)), Function(None, 'f', ['b'], [], 0, None, Stmt([Printnl([Name('x')], None), Assign([AssName('y', 'OP_ASSIGN')], Const(5)), Function(None, 'g', ['x'], [], 0, None, Stmt([Assign([AssName('g', 'OP_ASSIGN')], Const(3)), Assign([AssName('x', 'OP_ASSIGN')], Lambda(['x'], [], 0, Add((Name('x'), Name('g'))))), Assign([AssName('c', 'OP_ASSIGN')], Lambda(['y'], [], 0, Add((Name('g'), Name('y'))))), Return(Lambda(['y'], [], 0, Add((CallFunc(Name('x'), [Const(1)], None, None), Name('y')))))]))]))]))
test6 = """
x = 4 #x1
def f(b): #f1(b1)
    print x #x1
    y = 5 #y1
    def g(x): #g1, x2
        g = 3 #g2
        x = lambda x: x+g #x2 = x3+g2
        c = lambda y: g + y #c1 = y2+g2
        return lambda y: x + y #y2+x2
"""

test7 = """
x = 4 #x1
def f(b): #f1, b1
    print x #x1
    y = 5 #y1
    def g(x): #g1, x2
        g = 3 #g2
        x = lambda x: lambda q: x+q #x3,q0: x2 = x3 + q1
        c = lambda y: g + y #c0 = y2+g2
        return lambda y: x + y #y2+x2
"""

test7_tmp = "lambda x: lambda q: x+q"
test7_tmp2 = "x=lambda x: lambda q: x+q"

test8 = """
def f(b): #f1, b1
    def g(x): #overwrites outer; g1, x1
        return 1
    def h(y): #h1, y1
        return y #y1
    return g(1) + h(4) #g1, h1

def g(y): #g2, y1
    return 3
"""

test9 = """
def g(y): #g1
    return 3

def f(b): #f1, b1
    def g(x): #overwrites outer; g2, x1
        return 1
    def h(y): #h1, y1
        return y #y1
    return g(1) + h(4) #g2, h1
"""

test10 = """
def f(b): #f1, b1
    def g(x): #g1, x1
        return 1
    def h(y): #h1, y1
        return y
    return g(1) + h(1) #g1, h1

def p(y): #p1, y1
    def g(x): #g2, x1
        return 2
    def h(y): #h2, y2
        return y+1
    return g(1) + h(1) #g2, h2
"""

test11 = """
def f(b): #f1, b1
    def g(x): #g1, x1
        return 1
    def g(y): #g1, y1
        return y
    def g(x, y): #overwrites the above, g1, x1, y1
        return x+y
    return g(3) #g1
"""

test12 = """
def g(x): #g1, x1
    def g(x): #g2, x2
        return x #x2
    return g #g2
"""

test13 = """
l = [lambda x: x+10, lambda y: y+11]
def a(x):
    return x
a(1)(2)
"""

# variable_counter = 0
# varialbes_list = []
scope = [] # a stack! append to the end and pop from the end
functions = dict() # for unique func names. just a global counter across all scopes


def find_variables(node):

    global scope, functions

    # expand Stmt and handle renaming stuff here!
    if isinstance(node, Module):
        scope.append(dict())
        find_variables(node.node)
        print "Module", scope
        rename(node.node)

    # call on each statement. just a wrapper
    elif isinstance(node, Stmt):
        for n in node.nodes:
            find_variables(n)

    # # call on stuff inside, to rename
    elif isinstance(node, Printnl):
        find_variables(node.nodes[0])

    # elif isinstance(node, AssName):
    #     pass

    elif isinstance(node, Assign):
        # varialbes_list.append({node.nodes[0].name:variable_counter}) # get names of the global variables
        # variable_counter+= 1
        # find_variables(node.expr)
        # find_variables(node.nodes[0])
        # if across all scopes a variable with a name matching the value of arg is never defined, then unique_num is 0

        # only if making a new name.
        if not isinstance(node.nodes[0],AssName):
            return

        varname = node.nodes[0].name

        cur_scope = scope[-1]

        # so if varname is 'x', and there is no 'x' in any previous scopes, its number should be 'x0'. if is defined in a previous scope, and its last
        #   valid name was like 'x1', then this should be 'x2'.
        unique_num = 0

        # check if this argument name shows up in any of the old scopes, so iterate backwards through the stack of scopes; this is how you get the index
        for i in range(len(scope)-1, -1, -1):
            tmp_scope = scope[i]
            if varname in tmp_scope:
                print "HERE!!!",varname, scope, tmp_scope
                if i == len(scope)-1:
                    unique_num = tmp_scope[varname]
                else:
                    unique_num = tmp_scope[varname] + 1
                break

        cur_scope[varname] = unique_num

        # if isinstance(node.expr, Lambda):
        find_variables(node.expr)

        print node, scope


    elif isinstance(node, Discard):
        find_variables(node.expr)


    elif isinstance(node, List):
        for x in node.nodes:
            find_variables(x)


    elif isinstance(node, Dict):
        for x in node.items:
            find_variables(x[0])
            find_variables(x[1])


    elif isinstance(node, Or):
        # if len(node.nodes) > 2:
        #     node.nodes = [node.nodes[0], Or(node.nodes[1:])]
        find_variables(node.nodes[0])
        find_variables(node.nodes[1])


    elif isinstance(node, And):
        # if len(node.nodes) > 2:
        #     node.nodes = [node.nodes[0], And(node.nodes[1:])]
        find_variables(node.nodes[0])
        find_variables(node.nodes[1])

    elif isinstance(node, Not):
        arg = find_variables(node.expr)


    elif isinstance(node, Add):
        find_variables(node.left)
        find_variables(node.right)


    elif isinstance(node, UnarySub):
        find_variables(node.expr)


    elif isinstance(node, Subscript):
        find_variables(node.subs[0])


    elif isinstance(node, IfExp):
        # then and else necessarily return a value as this is an ifexp, so we want to call flatten on them first. same is not true of let
        test = find_variables(node.test)
        then = find_variables(node.then)
        else_ = find_variables(node.else_)


    elif isinstance(node, CallFunc):
        find_variables(node.node)
        args = []
        for n in node.args:
            find_variables(n)

    elif isinstance(node,Function): #for function names, use both functions for global update and scope for local updates if function redefined in same scope
        # check function name: if defined in current scope (not new_scope, but scope[-1]), don't increment counter in functions or add to scope
        #   else, if not defined, add to current scope and increment counter
        encasing_scope = scope[-1]
        print "function", node.name, encasing_scope, scope
        #if "__func! " + node.name not in encasing_scope:
        if node.name not in encasing_scope:
            # add function name to encasing/current scope
            if node.name in functions:
                # encasing_scope["__func! " + node.name] = functions[node.name]
                functions[node.name] += 1
                encasing_scope[node.name] = functions[node.name]
            else:
                # encasing_scope["__func! " + node.name] = 0
                encasing_scope[node.name] = 0
                functions[node.name] = 0


        # handle variables
        new_scope = dict()

        # append to scope, all new argnames
        for arg in node.argnames:
            # if across all scopes a variable with a name matching the value of arg is never defined, then unique_num is 0
            # so if varname is 'x', and there is no 'x' in any previous scopes, its number should be 'x0'. if is defined in a previous scope, and its last
            #   valid name was like 'x1', then this should be 'x2'.
            unique_num = 0

            # check if this argument name shows up in any of the old scopes, so iterate backwards through the stack of scopes; this is how you get the index
            for i in range(len(scope)-1, -1, -1):
                cur_scope = scope[i]
                if arg in cur_scope:
                    unique_num = cur_scope[arg] + 1
                    break

            new_scope[arg] = unique_num

        scope.append(new_scope)

        # call this method recursively
        find_variables(node.code)

        # rename
        rename(node)
        rename(node.code)


        print "Function", node.name, scope

        # pop from stack/scope
        scope = scope[0:len(scope)-1]


        # print "\n\n"
        # varialbes_list.append({node.name:variable_counter}) # get names of the global variables
        # variable_counter+= 1
        # find_variables(node.code)
        # tmp = []
        # found = False
        # for arg in node.argnames:
        #     for dic in varialbes_list:   #might be better to do in reverse
        #         for key,value in dic.items():
        #             if arg == key:
        #                 found = True
        #                 tmp.append({key:value})
        #                 break
        #     if found == False:
        #         tmp.append({arg:variable_counter})# get names of the global variables
        #         variable_counter+= 1
        # varialbes_list.extend(tmp)

    elif isinstance(node, Lambda):
        new_scope = dict()

        # append to scope, all new argnames
        for arg in node.argnames:
            # if across all scopes a variable with a name matching the value of arg is never defined, then unique_num is 0
            # so if varname is 'x', and there is no 'x' in any previous scopes, its number should be 'x0'. if is defined in a previous scope, and its last
            #   valid name was like 'x1', then this should be 'x2'.
            unique_num = 0

            # check if this argument name shows up in any of the old scopes, so iterate backwards through the stack of scopes; this is how you get the index
            for i in range(len(scope)-1, -1, -1):
                cur_scope = scope[i]
                if arg in cur_scope:
                    unique_num = cur_scope[arg] + 1
                    break

            new_scope[arg] = unique_num

        scope.append(new_scope)

        # call this method recursively
        find_variables(node.code)

        # rename
        rename(node)
        if not isinstance(node.code, Lambda):
            rename(node.code)

        print "Lambda", scope, new_scope

        # pop from stack/scope
        scope = scope[0:len(scope)-1]

    #could be returned as a normal
    elif isinstance(node,Return):
        find_variables(node.value)

    #     if isinstance(node.value,Name):
    #         found = False
    #         tmp = []
    #         for dic in varialbes_list:   #might be better to do in reverse
    #             for key,value in dic.items():
    #                 if node.value.name == key:
    #                     found = True
    #                     tmp.append({key:value})
    #                     break
    #         if found == False:
    #             tmp.append({node.value.name:variable_counter})# get names of the global variables
    #             variable_counter+= 1
    #         varialbes_list.extend(tmp)


    else:
        return

def rename( node):

    global scope

    # expand every Or, And, and Compare
    # if isinstance(node, Module):
    #     rename(node.node)


    # elif isinstance(node, Stmt):
    if isinstance(node, Stmt):
        for n in node.nodes:
            if not isinstance(n, Function) and not isinstance(n, Lambda):
                rename(n)


    elif isinstance(node, Printnl):
        if not isinstance(node.nodes[0], Function) and not isinstance(node.nodes[0], Lambda):
            rename(node.nodes[0])

    elif isinstance(node, Const):
        pass

    elif isinstance(node, AssName):
        # behavior here
        unique_num = -1

        for i in range(len(scope)-1, -1, -1):
            cur_scope = scope[i]
            if node.name in cur_scope:
                unique_num = cur_scope[node.name]
                break

        if unique_num == -1:
            raise Exception("Variable Undefined!!!! " + node.name + " " + str(scope))
        else:
            node.name = node.name + "_UNIQUEID" + str(unique_num)


    elif isinstance(node, Name):
        # behavior here
        unique_num = -1

        for i in range(len(scope)-1, -1, -1):
            cur_scope = scope[i]
            if node.name in cur_scope:
                unique_num = cur_scope[node.name]
                break

        if unique_num == -1:
            raise Exception("Variable Undefined!!!! " + node.name)
        else:
            node.name = node.name + "_UNIQUEID" + str(unique_num)


    elif isinstance(node, Assign):
        for x in node.nodes:
            if not isinstance(x, Function) and not isinstance(x, Lambda): #impossible
                rename(x)

        #dont want to repeat work!
        if not isinstance(node.expr, Function) and not isinstance(node.expr, Lambda):
            rename(node.expr)


    elif isinstance(node, Discard):
        if not isinstance(node.expr, Function) and not isinstance(node.expr, Lambda):
            rename(node.expr)


    elif isinstance(node, List):
        for x in node.nodes:
            if not isinstance(x, Function) and not isinstance(x, Lambda):
                rename(x)


    elif isinstance(node, Dict):
        for x in node.items:
            if not isinstance(x, Function) and not isinstance(x, Lambda):
                rename(x[0])
                rename(x[1])


    elif isinstance(node, Or):
        #if len(node.nodes) > 2:
        #    node.nodes = [node.nodes[0], Or(node.nodes[1:])]
        #rename(node.nodes[0])
        #rename(node.nodes[1])
        for arg in node.nodes:
            if not isinstance(arg, Function) and not isinstance(arg, Lambda):
                rename(arg)


    elif isinstance(node, And):
        # if len(node.nodes) > 2:
        #     node.nodes = [node.nodes[0], And(node.nodes[1:])]
        # rename(node.nodes[0])
        # rename(node.nodes[1])
        for arg in node.nodes:
            if not isinstance(arg, Function) and not isinstance(arg, Lambda):
                rename(arg)

    elif isinstance(node, Not):
        if not isinstance(node.expr, Function) and not isinstance(node.expr, Lambda):
            rename(node.expr)


    elif isinstance(node, Compare):
        if not isinstance(node.expr, Function) and not isinstance(node.expr, Lambda):
            expr = rename(node.expr)
        for x in node.ops:    
            if not isinstance(x, Function) and not isinstance(x, Lambda):
                rename(x)


    elif isinstance(node, Add):
        if not isinstance(node.left, Function) and not isinstance(node.left, Lambda):
            rename(node.left)
        if not isinstance(node.right, Function) and not isinstance(node.right, Lambda):
            rename(node.right)


    elif isinstance(node, UnarySub):
        if not isinstance(node.expr, Function) and not isinstance(node.expr, Lambda):
            rename(node.expr)


    elif isinstance(node, Subscript):
        # call on expr and elements in subs
        if not isinstance(node.expr, Function) and not isinstance(node.expr, Lambda):
            rename(node.expr)

        if not isinstance(node.subs[0], Function) and not isinstance(node.subs[0], Lambda):
            rename(node.subs[0])


    elif isinstance(node, IfExp):
        # then and else necessarily return a value as this is an ifexp, so we want to call flatten on them first. same is not true of let
        test = rename(node.test)
        if not isinstance(node.then, Function) and not isinstance(node.then, Lambda):
            then = rename(node.then)
        if not isinstance(node.then, Function) and not isinstance(node.then, Lambda):
            else_ = rename(node.else_)

    elif isinstance(node, CallFunc):
        # handle here, rename func separately though! (do it explicitly here)
        # old_function_name = "__func! " + node.node.name
        if not isinstance(node.node, Name):
            if isinstance(node.node, CallFunc):
                rename(node.node)
                return 
            else:
                return
        old_function_name = node.node.name
        new_function_name = ""

        for i in range(len(scope)-1, -1, -1):
            if old_function_name in scope[i]:
                new_function_name = node.node.name + "_UNIQUEID" + str(scope[i][old_function_name])
                break

        if new_function_name == "":
            print scope
            raise Exception("Undefined function call " + node.node.name)
        else:
            node.node = Name(new_function_name)

        args = []
        for n in node.args:
            if not isinstance(n, Function) and not isinstance(n, Lambda):
                rename(n)

    elif isinstance(node,Function):
        # handle here, rename func separately though! (do it explicitly here)
        # rename func
        # call on argnames
        # call on func body


        # prevent case where we are in the outer scope and don't need to rename functions again
        function_outer_scope = scope[-2]
        print node.name
        # if "__func! " + node.name in function_outer_scope:
        #     node.name = node.name + "_UNIQUEID" + str(function_outer_scope["__func! " + node.name])
        if node.name in function_outer_scope:
            node.name = node.name + "_UNIQUEID" + str(function_outer_scope[node.name])
        else:
            raise Exception("Rename in uniquify, error when defining function " + node.name + " " + str(scope))

        for i in range(0, len(node.argnames)):
            arg = node.argnames[i]
            unique_num = -1

            for j in range(len(scope)-1, -1, -1):
                cur_scope = scope[j]
                if arg in cur_scope:
                    unique_num = cur_scope[arg]
                    break

            if unique_num == -1:
                raise Exception("Variable Undefined!!!! " + arg)
            else:
                node.argnames[i] = arg + "_UNIQUEID" + str(unique_num)

        #rename(node.code)

        # print "\n\n"
        # tmp = varialbes_list.pop(0)
        # for key,value in tmp.items():
        #     node.name = key + '_' + str(value)

        # rename(node.code)
        # found = False
        # for i  in range(len(node.argnames)):
        #     tmp = varialbes_list.pop(0)
        #     for key,value in tmp.items():
        #         if node.argnames[i] == key:
        #             found = True
        #             node.argnames[i] = key + '_' + str(value)

        #         # else:
        #         #     node.argnames[i] = key + '_' + str(value)


    elif isinstance(node, Lambda):
        # call on argnames
        # for arg in node.argnames:
        #     rename(arg)
        for i in range(0, len(node.argnames)):
            arg = node.argnames[i]
            unique_num = -1

            for j in range(len(scope)-1, -1, -1):
                cur_scope = scope[j]
                if arg in cur_scope:
                    unique_num = cur_scope[arg]
                    break

            if unique_num == -1:
                print node
                raise Exception("Variable Undefined!!!! " + arg)
            else:
                node.argnames[i] = arg + "_UNIQUEID" + str(unique_num)

        # call on func body
        #rename(node.code)


    elif isinstance(node,Return):
        if not isinstance(node.value, Function) and not isinstance(node.value, Lambda):
            rename(node.value)

        # if isinstance(node.value,Name):
        #     found = False
        #     tmp = varialbes_list.pop(0)
        #     for key,value in tmp.items():
        #         if node.value.name == key:
        #             node.value.name = key + '_' + str(value)
    else:
        return


# SHOULD GIVE EVERYTHING A NAME!!!!
class LambdaUnifier():
    def __init__(self):
        # if appending new lines, need to append them to the right scope, so this tracks the most recent new scope opening
        self.tree = Module(None, Stmt([]))
        self.append_point = self.tree.node
        self.lambda_ctr = 0

    def lambdaUnify(self, node):
        if isinstance(node, Module):
            self.lambdaUnify(node.node)


        elif isinstance(node, Stmt):
            nodes = [self.lambdaUnify(n) for n in node.nodes]
            return Stmt([nodes])
        
        elif isinstance(node, Printnl):
            t = self.lambdaUnify(node.nodes[0])
            # self.tree.node.nodes.append(Printnl([t], None))
            self.append_point.nodes.append(Printnl([t], None))
        
        elif isinstance(node, Assign):
            t = self.lambdaUnify(node.expr)
            n = [self.lambdaUnify(x) for x in node.nodes]
            # self.tree.node.nodes.append(Assign([n], t))
            self.append_point.nodes.append(Assign(n, t))

        elif isinstance(node, Discard):
            t = self.lambdaUnify(node.expr)
            # self.tree.node.nodes.append(Discard(t))
            self.append_point.nodes.append(Discard(t))

        elif isinstance(node, Const):
            return node

        elif isinstance(node, Name):
            return node

        elif isinstance(node, AssName):
            return node

        elif isinstance(node, List):
            l = [self.lambdaUnify(x) for x in node.nodes]
            return List(l)

        elif isinstance(node, Dict):
            i = [(self.lambdaUnify(x[0]), self.lambdaUnify(x[1])) for x in node.items]
            return Dict(i)

        elif isinstance(node, Or):
            i = [self.lambdaUnify(x) for x in node.nodes]
            return Or(i)


        elif isinstance(node, And):
            i = [self.lambdaUnify(x) for x in node.nodes]
            return And(i)

        elif isinstance(node, Not):
            i = self.lambdaUnify(node.expr)
            return Not(i)

        elif isinstance(node, Compare):
            expr = self.lambdaUnify(node.expr)
            ops = [self.lambdaUnify(x) for x in node.ops]
            return Compare(expr, ops)


        elif isinstance(node, Add):
            left = self.lambdaUnify(node.left)
            right = self.lambdaUnify(node.right)
            return Add((left, right))


        elif isinstance(node, UnarySub):
            expr = self.lambdaUnify(node.expr)
            return UnarySub(expr)


        elif isinstance(node, Subscript):
            # call on expr and elements in subs
            expr = self.lambdaUnify(node.expr)
            subs = [self.lambdaUnify(x) for x in node.subs]
            return Subscript(expr, node.flags, subs)


        elif isinstance(node, IfExp):
            # then and else necessarily return a value as this is an ifexp, so we want to call flatten on them first. same is not true of let
            test = self.lambdaUnify(node.test)
            then = self.lambdaUnify(node.then)
            else_ = self.lambdaUnify(node.else_)
            return IfExp(test, then, else_)


        elif isinstance(node, CallFunc):
            # handle here, rename func separately though! (do it explicitly here)
            args = [self.lambdaUnify(x) for x in node.args]
            return CallFunc(node.node, args, None, None)
            

        elif isinstance(node,Function): #-> appends
            # append an assign to a lambda
            # print node, self.append_point, self.tree
            node.defaults = 'lambda_' + str(self.lambda_ctr)
            self.lambda_ctr += 1
            old_append_point = self.append_point
            self.append_point = Stmt([])
            self.lambdaUnify(node.code)
            body = self.append_point
            self.append_point = old_append_point
            self.append_point.nodes.append(Assign([AssName(node.name, 'OP_ASSIGN')], Lambda(node.argnames, node.defaults, node.flags, body)))


        elif isinstance(node, Lambda):
            node.defaults = 'lambda_' + str(self.lambda_ctr)
            self.lambda_ctr += 1
            body = self.lambdaUnify(node.code)
            return Lambda(node.argnames, node.defaults, node.flags, Stmt([Return(body)]))


        elif isinstance(node,Return): #-> appends
            value = self.lambdaUnify(node.value)
            self.append_point.nodes.append(Return(value))

            # if isinstance(node.value,Name):
            #     found = False
            #     tmp = varialbes_list.pop(0)
            #     for key,value in tmp.items():
            #         if node.value.name == key:
            #             node.value.name = key + '_' + str(value)
        else:
            return


# ast = compiler.parse(test1)

# print ast
# find_variables(ast)
# #print variable_counter
# #print varialbes_list
# #rename(ast)
# print "\n\n\n"
# print ast
# print "\n\n\n"

# lf = LambdaUnifier()
# lf.lambdaUnify(ast)

# print lf.tree
