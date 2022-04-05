# closure conversion
# handles converting any lambda into a call to create closure with argument [free_vars - arguments] -> DONE
# handles converting usage for free variables to indexing the free variables from a free_vars argument -> DONE
# handles moving all function definitions to the root level -> DONE
# handles converting callfunc for everything except input into CallFunc of get_fun_ptr with arg Name, and then that is called on get_free_vars name, 1

import compiler
from compiler.ast import *
from dataTypes import *

from functions import *

class ClosureConverter():
    def __init__(self, free_vars):
        self.tree = Module(None, Stmt([Stmt([])])) # inside first Stmt([]) is where function definitions go
        self.append_point = self.tree.node.nodes[0]
        self.curr_scope = '' #this will be a function name, so you know where to check for free vars
        self.free_vars = free_vars

    def closureConversion(self, node):
        if isinstance(node, Module):
            self.closureConversion(node.node)


        elif isinstance(node, Stmt):
            nodes = [self.closureConversion(n) for n in node.nodes]
            return Stmt([nodes])
        
        elif isinstance(node, Printnl):
            t = self.closureConversion(node.nodes[0])
            # self.tree.node.nodes.append(Printnl([t], None))
            self.append_point.nodes.append(Printnl([t], None))
        
        elif isinstance(node, Assign):
            t = self.closureConversion(node.expr)
            n = [self.closureConversion(x) for x in node.nodes]
            # self.tree.node.nodes.append(Assign([n], t))
            self.append_point.nodes.append(Assign(n, t))

        elif isinstance(node, Discard):
            t = self.closureConversion(node.expr)
            # self.tree.node.nodes.append(Discard(t))
            self.append_point.nodes.append(Discard(t))

        elif isinstance(node, Const):
            return node

        elif isinstance(node, Name):
            return node

        elif isinstance(node, AssName):
            return node

        elif isinstance(node, List):
            l = [self.closureConversion(x) for x in node.nodes]
            return List(l)

        elif isinstance(node, Dict):
            i = [(self.closureConversion(x[0]), self.closureConversion(x[1])) for x in node.items]
            return Dict(i)

        elif isinstance(node, Or):
            i = [self.closureConversion(x) for x in node.nodes]
            return Or(i)


        elif isinstance(node, And):
            i = [self.closureConversion(x) for x in node.nodes]
            return And(i)

        elif isinstance(node, Not):
            i = self.closureConversion(node.expr)
            return Not(i)

        elif isinstance(node, Compare):
            expr = self.closureConversion(node.expr)
            ops = [self.closureConversion(x) for x in node.ops]
            return Compare(expr, ops)


        elif isinstance(node, Add):
            left = self.closureConversion(node.left)
            right = self.closureConversion(node.right)
            return Add((left, right))


        elif isinstance(node, UnarySub):
            expr = self.closureConversion(node.expr)
            return UnarySub(expr)


        elif isinstance(node, Subscript):
            # call on expr and elements in subs
            expr = self.closureConversion(node.expr)
            subs = [self.closureConversion(x) for x in node.subs]
            return Subscript(expr, node.flags, subs)


        elif isinstance(node, IfExp):
            # then and else necessarily return a value as this is an ifexp, so we want to call flatten on them first. same is not true of let
            test = self.closureConversion(node.test)
            then = self.closureConversion(node.then)
            else_ = self.closureConversion(node.else_)
            return IfExp(test, then, else_)


        elif isinstance(node, CallFunc):
            # CallFunc(Name('f'), [Const(1)], None, None)
            # CallFunc(CallFunc(Name('get_fun_ptr'), [Name('f')], None, None), [CallFunc(Name('get_free_vars'), [Name('f')], None, None), Const(1)])
            return CallFunc(
                    CallFunc(Name('get_fun_ptr'), [node.node], None, None),
                    [CallFunc(Name('get_free_vars'), [node.node], None, None)] + node.args)
            

        elif isinstance(node,Lambda): #-> appends
            # append an assign to a lambda
            # print node, self.append_point, self.tree
            old_append_point = self.append_point

            # needed a func name so we put it in Lambda.defaults
            new_scope = node.defaults
            old_scope = self.curr_scope
            self.curr_scope = new_scope

            self.append_point = Stmt([])
            # declare all the free vars
            free_vars_name = 'free_vars_' + new_scope[new_scope.index('lambda_')+7:]
            for i in range(0, len(self.free_vars[new_scope])):
                name = self.free_vars[new_scope][i]
                self.append_point.nodes.append(Assign([AssName(name, 'OP_ASSIGN')], Subscript(Name(free_vars_name), 'OP_APPLY', [Const(i)])))

            self.closureConversion(node.code)
            body = self.append_point

            self.append_point = old_append_point
            self.curr_scope = old_scope

            self.tree.node.nodes.append(Lambda([free_vars_name] + node.argnames, node.defaults, node.flags, body))

            # second list is an access of the free vars, and we pass as the first parameter the name of the lambda. 
            # if you call a function and it has a FunctionLabel in its arguments, its necessarily a call to create_closure. you convert a FunctionLabel to just node.defaults in x86_IR, right after explicate i think
            return CallFunc(Name('create_closure'), [FunctionLabel(node.defaults), List([Name(x) for x in self.free_vars[new_scope]])], None, None)
            #self.append_point.nodes.append(Assign([AssName(node.name, 'OP_ASSIGN')], Lambda(node.argnames, node.defaults, node.flags, body)))


        elif isinstance(node,Return): #-> appends
            value = self.closureConversion(node.value)
            self.append_point.nodes.append(Return(value))

            # if isinstance(node.value,Name):
            #     found = False
            #     tmp = varialbes_list.pop(0)
            #     for key,value in tmp.items():
            #         if node.value.name == key:
            #             node.value.name = key + '_' + str(value)
        else:
            return


test0 = """
a = [3]
def f(b):
    c = [a[0] + b]
    return lambda x: c[0] + x

q = f(0)
q(1)
"""

ast = compiler.parse(test0)

print ast

find_variables(ast)
#print variable_counter
#print varialbes_list
#rename(ast)
print "\n\n\n"
print ast
print "\n\n\n"

lf = LambdaUnifier()
lf.lambdaUnify(ast)

print lf.tree

print "\n\n\n"

cc = ClosureConverter({'lambda_0': ['a'], 'lambda_1': ['c']})
cc.closureConversion(lf.tree)

for node in cc.tree.node.nodes:
    print node
for node in cc.tree.node.nodes[0].nodes:
    print node


print "\n\n\n"

