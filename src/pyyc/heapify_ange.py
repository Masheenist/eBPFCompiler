import compiler
from compiler.ast import *
from functions import *

scope_counter = 0
variables_list = []


def find_frees(node):

    global scope_counter

    # expand every Or, And, and Compare
    if isinstance(node, Module):
        find_frees(node.node)


    elif isinstance(node, Stmt):
        for n in node.nodes:
            find_frees(n)


    elif isinstance(node, Printnl):
        find_frees(node.nodes[0])

    elif isinstance(node, AssName):
        if any(node.name in key for key in variables_list):
            for dic in variables_list:
                for key in dic.keys():
                    if node.name == key:
                        dic[key].add(scope_counter)
        else:
            variables_list.append({node.name:{scope_counter}})
        pass

    elif isinstance(node, Name):
        if any(node.name in key for key in variables_list):
            for dic in variables_list:
                for key in dic.keys():
                    if node.name == key:
                        dic[key].add(scope_counter)
        else:
            variables_list.append({node.name: {scope_counter}})
        return

    elif isinstance(node, Assign):

        find_frees(node.expr)
        find_frees(node.nodes[0])


    elif isinstance(node, Discard):
        find_frees(node.expr)


    elif isinstance(node, List):
        for x in node.nodes:
            find_frees(x)


    elif isinstance(node, Dict):
        for x in node.items:
            find_frees(x[0])
            find_frees(x[1])


    elif isinstance(node, Or):
        if len(node.nodes) > 2:
            node.nodes = [node.nodes[0], Or(node.nodes[1:])]
        find_frees(node.nodes[0])
        find_frees(node.nodes[1])


    elif isinstance(node, And):
        if len(node.nodes) > 2:
            node.nodes = [node.nodes[0], And(node.nodes[1:])]
        find_frees(node.nodes[0])
        find_frees(node.nodes[1])

    elif isinstance(node, Not):
        find_frees(node.expr)


    elif isinstance(node, Add):
        find_frees(node.left)
        find_frees(node.right)


    elif isinstance(node, UnarySub):
        find_frees(node.expr)


    elif isinstance(node, Subscript):
        find_frees(node.expr)
        for sub in node.subs:
            find_frees(sub)


    elif isinstance(node, IfExp):
        # then and else necessarily return a value as this is an ifexp, so we want to call flatten on them first. same is not true of let
        test = find_frees(node.test)
        then = find_frees(node.then)
        else_ = find_frees(node.else_)

    elif isinstance(node, CallFunc):
        args = []
        for n in node.args:
            find_frees(n)
        # find_frees(node.node)

    elif isinstance(node, Const):
        pass


    elif isinstance(node,Function):
        scope_counter+= 1
        tmp = []
        found = False
        for arg in node.argnames:
            if any(arg in key for key in variables_list):
                for dic in variables_list:
                    for key in dic.keys():
                        if arg == key:
                            dic[key].add(scope_counter)
            else:
                variables_list.append({arg:{scope_counter}})
        find_frees(node.code)
        scope_counter-= 1


    elif isinstance(node,Lambda):
        scope_counter+= 1

        tmp = []
        found = False
        for arg in node.argnames:
            if any(arg in key for key in variables_list):
                for dic in variables_list:
                    for key in dic.keys():
                        if arg == key:
                            dic[key].add(scope_counter)
            else:
                variables_list.append({arg:{scope_counter}})
        find_frees(node.code)
        scope_counter-= 1


    #could be returned as a normal
    elif isinstance(node,Return):
        find_frees(node.value)


    else:
        print "Have not encountered node"
        print "************"
        print node
        print "************\n"
        return


class Heapifier():
    def __init__(self):
        print variables_list
        self.tree = Module(None, Stmt([]))
        self.append_point = self.tree.node
        self.has_been_declared = []
        self.curr_scope = '!!BASE!!'
        self.frees_for_each_func = {self.curr_scope: set()}
        # self.scope_counter = 0


    def heapify(self, node):

        # expand every Or, And, and Compare
        if isinstance(node, Module):
            # node.node = self.heapify(node.node)
            self.tree.node = self.heapify(node.node)
            for key in self.frees_for_each_func:
                self.frees_for_each_func[key] = list(self.frees_for_each_func[key])


        elif isinstance(node, Stmt):
            # newStmt = []
            # for n in node.nodes:
            #     newStmt.append(self.heapify(n))
            # node.nodes = newStmt
            nodes = [self.heapify(n) for n in node.nodes]
            # print "STMT!!!", nodes
            return Stmt(nodes)



        elif isinstance(node, Printnl):
            # node.nodes[0] = self.heapify(node.nodes[0])
            t = self.heapify(node.nodes[0])
            # self.append_point.nodes.append(Printnl([t], None))
            return Printnl([t], None)

        # elif isinstance(node, AssName):
        #     # if any(node.name in key for key in variables_list):
        #     #     name = node.name
        #     #     for dic in variables_list:
        #     #         for key in dic.keys():
        #     #             if len(dic[key]) > 1 and node.name == key:
        #     #                 #node = Subscript(Name(name), 'OP_APPLY', [Const(0)])
        #     #                 return Subscript(Name(name), 'OP_APPLY', [Const(0)])
        #     # won't ever have an assname that you need to convert to a subscript, as it'll just be a new variable in the scope
        #     # a = 3
        #     # def f(x):
        #     #    x = a
        #     #    a = 7 -> a is not free, will be renamed, so this literally isn't possible. can only have accesses of free vars!!! which means assigns only in original scope
        #     return node

        elif isinstance(node, Const):
            return node

        elif isinstance(node, Name):
            print node.name
            was_added = False
            if any(node.name in key for key in variables_list):
                name = node.name
                for dic in variables_list:
                    for key in dic.keys():
                        if len(dic[key]) > 1 and node.name == key:
                            #node = Subscript(Name(name), 'OP_APPLY', [Const(0)])
                            print self.curr_scope, self.frees_for_each_func, name
                            if self.curr_scope in self.frees_for_each_func:
                                self.frees_for_each_func[self.curr_scope].add(name)
                            else:
                                self.frees_for_each_func[self.curr_scope] = {name}
                            was_added = True
                            return Subscript(Name(name), 'OP_APPLY', [Const(0)])
            if not was_added:
                return node

        #two possible assigments a = 3 or a = b
        elif isinstance(node, Assign):
            # if it WAS declared, then a[0] = VALUE. else, a = [VALUE] on declaration the first time, if its free.
            was_added = False
            if any(node.nodes[0].name in key for key in variables_list):
                name = node.nodes[0].name
                for dic in variables_list:
                    for key in dic.keys():
                        if len(dic[key]) > 1 and name == key:
                            if name in self.has_been_declared:
                                # self.append_point.nodes.append(Assign([Subscript(Name(name), 'OP_ASSIGN', [Const(0)])], self.heapify(node.expr)))
                                was_added = True
                                if self.curr_scope in self.frees_for_each_func:
                                    self.frees_for_each_func[self.curr_scope].add(name)
                                else:
                                    self.frees_for_each_func[self.curr_scope] = {name}
                                return Assign([Subscript(Name(name), 'OP_ASSIGN', [Const(0)])], self.heapify(node.expr))
                            else:
                                self.has_been_declared.append(name)
                                was_added = True

                                if self.curr_scope in self.frees_for_each_func:
                                    self.frees_for_each_func[self.curr_scope].add(name)
                                else:
                                    self.frees_for_each_func[self.curr_scope] = {name}
                                # self.append_point.nodes.append(Assign([AssName(name, 'OP_ASSIGN')], List([self.heapify(node.expr)])))
                                return Assign([AssName(name, 'OP_ASSIGN')], List([self.heapify(node.expr)]))
            if not was_added:
                # self.append_point.nodes.append(Assign([AssName(node.nodes[0].name, 'OP_ASSIGN')], self.heapify(node.expr)))
                return Assign([AssName(node.nodes[0].name, 'OP_ASSIGN')], self.heapify(node.expr))


            # if isinstance(node.expr, Lambda):
            #     # create the function
            #     print "TODO"
            # else:
            # node.expr = self.heapify(node.expr)
            # # if free and this is the first assignment of it
            # node = Assign([AssName(node.nodes[0].name)], List([node.expr]))
            # node.nodes[0] = self.heapify(node.nodes[0])
            # print 'node.expr ', node.expr
            # #a = 3
            # if isinstance(node.expr, Const) and any(node.nodes[0].name in key for key in variables_list):
            #     value = node.expr.value
            #     for dic in variables_list:
            #         for key in dic.keys():
            #             if len(dic[key]) > 1 and node.nodes[0].name == key:
            #                 node = Assign([AssName(key, 'OP_ASSIGN')], List([Const(value)]))
            # #a = b
            # elif isinstance(node.expr, Name) and any(node.nodes[0].name in key for key in variables_list):
            #     value = node.expr.name
            #     for dic in variables_list:
            #         for key in dic.keys():
            #             if len(dic[key]) > 1 and node.nodes[0].name == key:
            #                 node = Assign([AssName(key, 'OP_ASSIGN')], List([Name(value)]))



        elif isinstance(node, Discard):
            # if isinstance(node.expr, Lambda):
            #     action
            # else:
            #     node.expr = self.heapify(node.expr)
            t = self.heapify(node.expr)
            # self.append_point.nodes.append(Discard(t))
            return Discard(t)


        elif isinstance(node, List):
            # newList = []
            # for x in node.nodes:
            #     newList.append(self.heapify(x))
            # node.nodes = newList
            l = [self.heapify(x) for x in node.nodes]
            return List(l)

        elif isinstance(node, Dict):
            # tmp = {}
            # for x in node.items:
            #     key = find_frees(x[0])
            #     value = find_frees(x[1])
            #     tmp[key] = value
            # node.items = tmp
            i = [(self.heapify(x[0]), self.heapify(x[1])) for x in node.items]
            return Dict(i)

        elif isinstance(node, Or):
            # if len(node.nodes) > 2:
            #     node.nodes = [node.nodes[0], Or(node.nodes[1:])]
            # node.nodes[0] = self.heapify(node.nodes[0])
            # node.nodes[1] = self.heapify(node.nodes[1])
            i = [self.heapify(x) for x in node.nodes]
            return Or(i)


        elif isinstance(node, And):
            # if len(node.nodes) > 2:
            #     node.nodes = [node.nodes[0], And(node.nodes[1:])]
            # node.nodes[0] = self.heapify(node.nodes[0])
            # node.nodes[1] = self.heapify(node.nodes[1])
            i = [self.heapify(x) for x in node.nodes]
            return And(i)

        elif isinstance(node, Not):
            # node.expr = self.heapify(node.expr)
            i = self.heapify(node.expr)
            return Not(i)

        elif isinstance(node, Compare):
            expr = self.heapify(node.expr)
            ops = [self.heapify(x) for x in node.ops]
            return Compare(expr, ops)

        elif isinstance(node, Add):
            # node.left = self.heapify(node.left)
            # node.right = self.heapify(node.right)
            left = self.heapify(node.left)
            right = self.heapify(node.right)
            return Add((left, right))


        elif isinstance(node, UnarySub):
            # node.expr = self.heapify(node.expr)
            expr = self.heapify(node.expr)
            return UnarySub(expr)


        elif isinstance(node, Subscript):
            # node.subs[0] = self.heapify(node.subs[0])
            # call on expr and elements in subs
            expr = self.heapify(node.expr)
            subs = [self.heapify(x) for x in node.subs]
            return Subscript(expr, node.flags, subs)


        elif isinstance(node, IfExp):
            # then and else necessarily return a value as this is an ifexp, so we want to call flatten on them first. same is not true of let
            # test = self.heapify(node.test)
            # then = self.heapify(node.then)
            # else_ = self.heapify(node.else_)
            test = self.heapify(node.test)
            then = self.heapify(node.then)
            else_ = self.heapify(node.else_)
            return IfExp(test, then, else_)

        elif isinstance(node, CallFunc):
            # tmpArgs = []
            # for n in node.args:
            #     tmpArgs.append(self.heapify(n))
            # node.args = tmpArgs
            args = [self.heapify(x) for x in node.args]
            n = self.heapify(node.node)
            return CallFunc(n, args, None, None)

        # elif isinstance(node, Const):
        #     pass

        # elif isinstance(node,Function):
        #     self.scope_counter+= 1
        #     tmp = []
        #     found = False
        #     for arg in node.argnames:
        #         if any(arg in key for key in variables_list):
        #             for dic in variables_list:
        #                 for key in dic.keys():
        #                     if len(dic[key]) > 1 and arg == key:
        #                         tmp.append(Assign([AssName(key, 'OP_ASSIGN')], List([])))
        #     node.argnames = tmp
        #     node.code = self.heapify(node.code)
        #     self.scope_counter-= 1

        elif isinstance(node,Lambda):
            # self.scope_counter+= 1
            # old_append_point = self.append_point
            # new_append_point = Stmt([])
            # self.append_point = new_append_point
            old_scope = self.curr_scope
            self.curr_scope = node.defaults
            tmp = []
            found = False
            for arg in node.argnames:
                if any(arg in key for key in variables_list):
                    for dic in variables_list:
                        for key in dic.keys():
                            if len(dic[key]) > 1 and arg == key:
                                tmp.append(Assign([AssName(key, 'OP_ASSIGN')], List([Name(arg)])))
                                # self.append_point.nodes.append(Assign([AssName(key, 'OP_ASSIGN')], List([Name(arg)])))
            # node.argnames = tmp
            body = self.heapify(node.code)
            self.curr_scope = old_scope
            body.nodes = tmp + body.nodes
            return Lambda(node.argnames, node.defaults, node.flags, body)
            # self.scope_counter-= 1

        #could be returned as a normal
        elif isinstance(node,Return):
            # node.value = self.heapify(node.value)
            return Return(self.heapify(node.value))

        else:
            print "Have not encountered node"
            print "*****PANIC*******"
            print node
            print "************\n"
        return node

ast = compiler.parse("""
a = 3
def f(x):
    b = 3
    def p(c):
        return c
    return lambda y: a + x + b + p(y)
""")

# print ast
# print "\n\n"

# lf = LambdaUnifier()
# lf.lambdaUnify(ast)
# ast = lf.tree
# print ast
# print "\n\n"

# find_frees(ast)
# print variables_list
# print "\n\n"

# hpfy = Heapifier()
# hpfy.heapify(ast)
# print hpfy.tree