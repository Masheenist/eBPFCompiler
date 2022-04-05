import compiler
from compiler.ast import *


ast = compiler.parseFile('test.py')

print ast
print "\n"

scope_counter = 0
variables_list = []


def find_variables( node):

    global scope_counter

    # expand every Or, And, and Compare
    if isinstance(node, Module):
        find_variables(node.node)


    elif isinstance(node, Stmt):
        for n in node.nodes:
            find_variables(n)

    elif isinstance(node, Printnl):
        find_variables(node.nodes[0])

    elif isinstance(node, AssName):
        if any(node.name in key for key in variables_list):
            for dic in variables_list:
                for key in dic.keys():
                    if node.name == key:
                        dic[key].add(scope_counter)
        else:
            variables_list.append({node.name:{scope_counter}})

    elif isinstance(node, Name):
        if any(node.name in key for key in variables_list):
            for dic in variables_list:
                for key in dic.keys():
                    if node.name == key:
                        dic[key].add(scope_counter)
        else:
            variables_list.append({node.name: {scope_counter}})

    elif isinstance(node, Assign):

        find_variables(node.expr)
        find_variables(node.nodes[0])


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
        if len(node.nodes) > 2:
            node.nodes = [node.nodes[0], Or(node.nodes[1:])]
        find_variables(node.nodes[0])
        find_variables(node.nodes[1])


    elif isinstance(node, And):
        if len(node.nodes) > 2:
            node.nodes = [node.nodes[0], And(node.nodes[1:])]
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
        args = []
        for n in node.args: 
            find_variables(n)
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
        find_variables(node.code)
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
        find_variables(node.code)
        scope_counter-= 1

    #could be returned as a normal
    elif isinstance(node,Return):
        find_variables(node.value)

    else:
        print "Have not encountered node"
        print "************"
        print node
        print "************\n"
        return
    

def heapify( node):

    global scope_counter

    # expand every Or, And, and Compare
    if isinstance(node, Module):
        node.node = heapify(node.node)


    elif isinstance(node, Stmt):

        newStmt = []
        for n in node.nodes:
            newStmt.append(heapify(n))
        node.nodes = newStmt


    elif isinstance(node, Printnl):
        node.nodes[0] = heapify(node.nodes[0])

    elif isinstance(node, AssName):
        if any(node.name in key for key in variables_list):
            name = node.name
            for dic in variables_list:
                for key in dic.keys():
                    if len(dic[key]) > 1 and name == key:
                        node = Subscript(Name(name), 'OP_APPLY', [Const(0)])
        
                        
    elif isinstance(node, Name):
        if any(node.name in key for key in variables_list):
            name = node.name
            for dic in variables_list:
                for key in dic.keys():
                    if len(dic[key]) > 1 and name == key:
                        node = Subscript(Name(name), 'OP_APPLY', [Const(0)])

    #two possible assigments a = 3 or a = b
    elif isinstance(node, Assign):
        node.expr = heapify(node.expr)
        node.nodes[0] = heapify(node.nodes[0])
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
        node.expr = heapify(node.expr)


    elif isinstance(node, List):
        newList = []
        for x in node.nodes:
            newList.append(heapify(x))
        node.nodes = newList

    elif isinstance(node, Dict):
        tmp = {}
        for x in node.items:
            key = find_variables(x[0])
            value = find_variables(x[1])
            tmp[key] = value
        node.items = tmp

    elif isinstance(node, Or):
        if len(node.nodes) > 2:
            node.nodes = [node.nodes[0], Or(node.nodes[1:])]
        node.nodes[0] = heapify(node.nodes[0])
        node.nodes[1] = heapify(node.nodes[1])


    elif isinstance(node, And):
        if len(node.nodes) > 2:
            node.nodes = [node.nodes[0], And(node.nodes[1:])]
        node.nodes[0] = heapify(node.nodes[0])
        node.nodes[1] = heapify(node.nodes[1])

    elif isinstance(node, Not):
        node.expr = heapify(node.expr)


    elif isinstance(node, Add):
        node.left = heapify(node.left)
        node.right = heapify(node.right)


    elif isinstance(node, UnarySub):
        node.expr = heapify(node.expr)


    elif isinstance(node, Subscript):
        node.subs[0] = heapify(node.subs[0])


    elif isinstance(node, IfExp):
        # then and else necessarily return a value as this is an ifexp, so we want to call flatten on them first. same is not true of let
        test = heapify(node.test)
        then = heapify(node.then)
        else_ = heapify(node.else_)

    elif isinstance(node, CallFunc):
        tmpArgs = []
        for n in node.args: 
            tmpArgs.append(heapify(n))
        node.args = tmpArgs

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
                        if len(dic[key]) > 1 and arg == key:
                            tmp.append(Assign([AssName(key, 'OP_ASSIGN')], List([])))
                        elif arg == key:
                            tmp.append(arg)
        node.argnames = tmp
        node.code = heapify(node.code)
        scope_counter-= 1
        
    elif isinstance(node,Lambda):
        scope_counter+= 1
        
        tmp = []
        found = False
        for arg in node.argnames:
            if any(arg in key for key in variables_list):
                for dic in variables_list:
                    for key in dic.keys():
                        if len(dic[key]) > 1 and arg == key:
                            tmp.append(Assign([AssName(key, 'OP_ASSIGN')], List([])))
                        elif arg == key:
                            tmp.append(arg)
        node.argnames = tmp
        node.code = heapify(node.code)
        scope_counter-= 1

    #could be returned as a normal
    elif isinstance(node,Return):
        node.value = heapify(node.value)

    else:
        print "Have not encountered node"
        print "*****PANIC*******"
        print node
        print "************\n"
    return node


find_variables(ast)
print variables_list
print "\n"
print heapify(ast)

    
            