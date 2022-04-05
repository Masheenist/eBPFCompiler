import compiler
from compiler.ast import *


ast = compiler.parseFile('test.py')

print ast

variable_counter = 0
varialbes_list = []


def find_variables( node):

    global variable_counter

    # expand every Or, And, and Compare
    if isinstance(node, Module):
        find_variables(node.node)


    elif isinstance(node, Stmt):
        for n in node.nodes:
            find_variables(n)


    elif isinstance(node, Printnl):
        find_variables(node.nodes[0])

    elif isinstance(node, AssName):
        pass

    elif isinstance(node, Assign):
        varialbes_list.append({node.nodes[0].name:variable_counter}) # get names of the global variables
        variable_counter+= 1
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
    elif isinstance(node,Function):
        print "\n\n"
        varialbes_list.append({node.name:variable_counter}) # get names of the global variables
        variable_counter+= 1
        find_variables(node.code)
        tmp = []
        found = False
        for arg in node.argnames:
            for dic in varialbes_list:   #might be better to do in reverse
                for key,value in dic.items():
                    if arg == key:
                        found = True
                        tmp.append({key:value})
                        break
            if found == False:
                tmp.append({arg:variable_counter})# get names of the global variables
                variable_counter+= 1
        varialbes_list.extend(tmp)
    #could be returned as a normal
    elif isinstance(node,Return):

        if isinstance(node.value,Name):
            found = False
            tmp = []
            for dic in varialbes_list:   #might be better to do in reverse
                for key,value in dic.items():
                    if node.value.name == key:
                        found = True
                        tmp.append({key:value})
                        break
            if found == False:
                tmp.append({node.value.name:variable_counter})# get names of the global variables
                variable_counter+= 1    
            varialbes_list.extend(tmp)
       

    else:
        return

def rename( node):

    global variable_counter

    # expand every Or, And, and Compare
    if isinstance(node, Module):
        rename(node.node)


    elif isinstance(node, Stmt):
        for n in node.nodes:
            rename(n)


    elif isinstance(node, Printnl):
        rename(node.nodes[0])

    elif isinstance(node, AssName):
        pass

    elif isinstance(node, Assign):
        tmp = varialbes_list.pop(0)
        for key,value in tmp.items():
            node.nodes[0].name = key + '_' + str(value)
        rename(node.expr)
        rename(node.nodes[0])


    elif isinstance(node, Discard):
        rename(node.expr)


    elif isinstance(node, List):
        for x in node.nodes:
            rename(x)


    elif isinstance(node, Dict):
        for x in node.items:
            rename(x[0])
            rename(x[1])


    elif isinstance(node, Or):
        if len(node.nodes) > 2:
            node.nodes = [node.nodes[0], Or(node.nodes[1:])]
        rename(node.nodes[0])
        rename(node.nodes[1])


    elif isinstance(node, And):
        if len(node.nodes) > 2:
            node.nodes = [node.nodes[0], And(node.nodes[1:])]
        rename(node.nodes[0])
        rename(node.nodes[1])

    elif isinstance(node, Not):
        arg = rename(node.expr)


    elif isinstance(node, Add):
        rename(node.left)
        rename(node.right)


    elif isinstance(node, UnarySub):
        rename(node.expr)


    elif isinstance(node, Subscript):
        rename(node.subs[0])


    elif isinstance(node, IfExp):
        # then and else necessarily return a value as this is an ifexp, so we want to call flatten on them first. same is not true of let
        test = rename(node.test)
        then = rename(node.then)
        else_ = rename(node.else_)

    elif isinstance(node, CallFunc):
        args = []
        for n in node.args: 
            rename(n)
    elif isinstance(node,Function):
        print "\n\n"
        tmp = varialbes_list.pop(0)
        for key,value in tmp.items():
            node.name = key + '_' + str(value)

        rename(node.code)
        found = False
        for i  in range(len(node.argnames)):
            tmp = varialbes_list.pop(0)
            for key,value in tmp.items():
                if node.argnames[i] == key:
                    found = True
                    node.argnames[i] = key + '_' + str(value)
    
                # else:
                #     node.argnames[i] = key + '_' + str(value)


    elif isinstance(node,Return):
        
        if isinstance(node.value,Name):
            found = False
            tmp = varialbes_list.pop(0)
            for key,value in tmp.items():
                if node.value.name == key:
                    node.value.name = key + '_' + str(value)
    else:
        return


find_variables( ast)
print variable_counter
print varialbes_list
rename(ast)
print ast
        