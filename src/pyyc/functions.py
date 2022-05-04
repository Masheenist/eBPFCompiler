# yea yea bad name for a file but this is what we called it in homework 5 oh well

from ast import *
import sys


def find_variables(node):

    global scope, functions

    # expand Stmt and handle renaming stuff here!
    if isinstance(node, Module):
        scope.append(dict())
        find_variables(node.node)
        # print "Module", scope
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
                # print "HERE!!!",varname, scope, tmp_scope
                if i == len(scope)-1:
                    unique_num = tmp_scope[varname]
                else:
                    unique_num = tmp_scope[varname] + 1
                break

        cur_scope[varname] = unique_num

        # if isinstance(node.expr, Lambda):
        find_variables(node.expr)

        # print node, scope


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
        find_variables(node.expr)
        find_variables(node.subs[0])


    elif isinstance(node, IfExp):
        # then and else necessarily return a value as this is an ifexp, so we want to call flatten on them first. same is not true of let
        find_variables(node.test)
        find_variables(node.then)
        find_variables(node.else_)


    elif isinstance(node, CallFunc):
        find_variables(node.node)
        args = []
        for n in node.args:
            find_variables(n)

    elif isinstance(node,Function): #for function names, use both functions for global update and scope for local updates if function redefined in same scope
        # check function name: if defined in current scope (not new_scope, but scope[-1]), don't increment counter in functions or add to scope
        #   else, if not defined, add to current scope and increment counter
        encasing_scope = scope[-1]
        # print "function", node.name, encasing_scope, scope
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


        # print "Function", node.name, scope

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

        # print "Lambda", scope, new_scope

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

    elif isinstance(node, If):
        # then and else necessarily return a value as this is an ifexp, so we want to call flatten on them first. same is not true of let
        for test in node.tests:
            find_variables(test)
        find_variables(node.else_)

    elif isinstance(node, While):
        # then and else necessarily return a value as this is an ifexp, so we want to call flatten on them first. same is not true of let
        find_variables(node.test)
        find_variables(node.body)
        find_variables(node.else_)


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
        # print node

        if node.name == 'True' or node.name == 'False':
            return node

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
        # print "FRICK", node
        # call on expr and elements in subs
        if not isinstance(node.expr, Function) and not isinstance(node.expr, Lambda):
            rename(node.expr)

        if not isinstance(node.subs[0], Function) and not isinstance(node.subs[0], Lambda):
            rename(node.subs[0])


    elif isinstance(node, IfExp):
        # then and else necessarily return a value as this is an ifexp, so we want to call flatten on them first. same is not true of let
        rename(node.test)
        if not isinstance(node.then, Function) and not isinstance(node.then, Lambda):
            rename(node.then)
        if not isinstance(node.then, Function) and not isinstance(node.then, Lambda):
            rename(node.else_)

    elif isinstance(node, CallFunc):
        # handle here, rename func separately though! (do it explicitly here)
        # old_function_name = "__func! " + node.node.name
        # if not isinstance(node.node, Name):
        #     if isinstance(node.node, CallFunc):
        #         rename(node.node)
        #         return 
        #     else:
        #         return
        # old_function_name = node.node.name
        # new_function_name = ""

        # if old_function_name in library_funcs:
        #     new_function_name = old_function_name
        # else:
        #     for i in range(len(scope)-1, -1, -1):
        #         if old_function_name in scope[i]:
        #             new_function_name = node.node.name + "_UNIQUEID" + str(scope[i][old_function_name])
        #             break

        # if new_function_name == "":
        #     print scope
        #     raise Exception("Undefined function call " + node.node.name)
        # else:
        #     node.node = Name(new_function_name)
        if not (isinstance(node.node, Name) and node.node.name in library_funcs):
            rename(node.node)

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
        # print node.name
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
                # print node
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

    elif isinstance(node, If):
        for test in node.tests:
            if not isinstance(test, Function) and not isinstance(test, Lambda):
                rename(test)
        if not isinstance(node.else_, Function) and not isinstance(node.else_, Lambda):
            rename(node.else_)

    elif isinstance(node, While):
        if not isinstance(node.test, Function) and not isinstance(node.test, Lambda):
            rename(node.test)
        if not isinstance(node.body, Function) and not isinstance(node.body, Lambda):
            rename(node.body)
        if not isinstance(node.then, Function) and not isinstance(node.then, Lambda):
            rename(node.else_)


    else:
        return


def main():
    with open(sys.argv[1], "r") as program_file:
        file_text = program_file.read()
        # print('\nTest File [{1}]\n- - - - - - - -\n{0}- - - - - - - -'.format(file_text, sys.argv[1]))
        ast = parse(file_text)#compiler.parse(file_text)
        # print("ast:[{0}]".format(ast))
        # print_python3_ast(ast)
        print(dump(ast, indent=4))
        print("~~~~~~~~")
        print(dump(ast, indent=4))

main()