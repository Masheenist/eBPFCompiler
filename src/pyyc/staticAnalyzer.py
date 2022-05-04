from compiler.ast import *
from compiler.consts import OP_ASSIGN
import compiler
import sys


ast_tree = compiler.parseFile("/home/jovyan/eBPFCompiler/tests/preliminary_ebpf_tests/basic_test1.py")
print "\n_____________AST____________\n"
print ast_tree

all_variables = {}
all_functions = {}
all_returns = {}

def get_function_info(func):
    all_functions[func.name] = func.argnames

def check_data_structure(array):
    
    isInt = False
    isBool = False
    isString = False

    if isinstance(array, List) or isinstance(array, Set):
        for arr in array:
            if isinstance(arr, Const):
                if type(arr.value) == int:
                    isInt = True
                elif type(arr.value) == str:
                    isString = True
                else:
                    raise Exception("No AST match: " + str(array))
            elif isinstance(arr, Name):
                if type(arr.name) == str and (arr.name == 'True' or arr.name == 'False'):
                    isBool = True
                else:
                    raise Exception("No AST match: " + str(array))
    elif isinstance(array, Dict):
        # keyInt = False
        # keyBool = False
        # keyStr = False

        # valueInt = False
        # valueBool = False
        # valueStr = False

        # for arr in array.items:
        #     #check the keys
        #     if isinstance(arr[0], Const):
        #         if type(arr[0].value) == int:
        #             keyInt = True
        #         elif type(arr[0].value) == str:
        #             keyStr = True
        #         else:
        #             raise Exception("No AST match: " + str(array))
        #     elif isinstance(arr[0], Name):
        #         if type(arr[0].name) == str and (arr[0].name == 'True' or arr[0].name == 'False'):
        #             keyBool = True
        #         else:
        #             raise Exception("No AST match: " + str(array)) 
            
        #     #check the values
        #     if isinstance(arr[1], Const):
        #         if type(arr[1].value) == int:
        #             keyInt = True
        #         elif type(arr[1].value) == str:
        #             keyStr = True
        #         else:
        #             raise Exception("No AST match: " + str(array))
        #     elif isinstance(arr[1], Name):
        #         if type(arr[1].name) == str and (arr[1].name == 'True' or arr[1].name == 'False'):
        #             keyBool = True
        #         else:
        #             raise Exception("No AST match: " + str(array))
            
        #     if keyInt and not keyBool and not keyStr:
        pass
    
    if isInt and not isBool and not isString:
        return int
    elif not isInt and isBool and not isString:
        return bool
    elif not isInt and not isBool and isString:
        return str
    else:
        raise Exception("The data structure needs to have the same type of variables")


def check_type(name, expr):
    name = name[0].name  #get name of variable
    if isinstance(expr, Const):        
        if type(expr.value) == int:
            all_variables[name] = int   #int
        elif type(expr.value) == str:
            all_variables[name] = str   #string
        else:
            raise Exception("No AST match: " + str(expr))
    elif isinstance(expr, Name):
        if type(expr.name) == str and (expr.name == 'True' or expr.name == 'False'):
            all_variables[name] = bool
        else:
            funcFound = False
            temp = None
            for dic in all_functions:
                if dic == expr.name:
                    def foo(x): #quick to enter function type
                        print x
                    all_variables[name] = type(foo)
                    temp = dic
                    funcFound = True

            if funcFound == False:
                raise Exception("No AST match: " + str(expr))
            else:
                all_functions[name] = all_functions[temp]
    elif isinstance(expr, List):
        dataType = check_data_structure(expr)
        all_variables[name] = {list:dataType}
    elif isinstance(expr,Set):
        dataType = check_data_structure(expr)
        all_variables[name] = {list:dataType}
    elif isinstance(expr, Dict):
        dataType = check_data_structure(expr)
        all_variables[name] = {list:dataType}
    elif isinstance(expr, CallFunc):
        # def foo(x): #quick to enter function type
        #     print x
        # all_variables[name] = type(foo)
        # for arg in expr.args:
        #     if isinstance(expr, Const):        
        #         if type(expr.value) == int:
        #             all_variables[name] = int   #int
        #         elif type(expr.value) == str:
        #             all_variables[name] = str   #string
        #         else:
        #             raise Exception("No AST match: " + str(expr))
        #     elif isinstance(expr, Name):
        #         if type(expr.name) == str and (expr.name == 'True' or expr.name == 'False'):
        #             all_variables[name] = bool
        #         else:
        #             raise Exception("No AST match: " + str(expr))
        tmpName  = None
        if isinstance(expr.node, Name):
            tmpName = expr.node.name
        else:
            raise Exception("No AST match: " + str(expr))
        zip_obj = zip(expr.args,all_functions[tmpName])
        for callType, paramVariable in zip_obj:
            if isinstance(callType, Const):        
                if type(callType.value) == int:
                    all_variables[paramVariable] = int   #int
                elif type(callType.value) == str:
                    all_variables[paramVariable] = str   #string
                else:
                    raise Exception("No AST match: " + str(callType))
            elif isinstance(callType, Name):
                if type(callType.name) == str and (callType.name == 'True' or callType.name == 'False'):
                    all_variables[paramVariable] = bool
                else:
                    funcFound = False
                    for dic in all_functions:
                        if dic == callType.name:
                            def foo(x): #quick to enter function type
                                print x
                            all_variables[paramVariable] = type(foo)
                            funcFound = True
                    if funcFound == False:
                        raise Exception("No AST match: " + str(callType))
            elif isinstance(callType, List):
                dataType = check_data_structure(callType)
                all_variables[paramVariable] = {list:dataType}
            elif isinstance(callType,Set):
                dataType = check_data_structure(callType)
                all_variables[paramVariable] = {list:dataType}
            elif isinstance(callType, Dict):
                dataType = check_data_structure(callType)
                all_variables[paramVariable] = {list:dataType}
            else:
                raise Exception("No AST match: " + str(callType))

    else:
        raise Exception("No AST match: " + str(expr))

def ast_print(ast)  :
    if isinstance(ast, Module):
        ast_print(ast.node)
    elif isinstance(ast, Stmt):
        for node in ast.nodes:
            if isinstance(node, Function):
                get_function_info(node)
        ast_print(ast.nodes)
    elif isinstance(ast, Printnl):
        ast_print(ast.nodes)
    elif isinstance(ast, Assign):
        check_type(ast.nodes, ast.expr)
        ast_print(ast.nodes)
        ast_print(ast.expr)
    elif isinstance(ast, AssName):
        pass
        # ast_print(ast.name)
        # ast_print(ast.flags)
    elif isinstance(ast, Discard):
        ast_print(ast.expr)
    elif isinstance(ast, Const):
        pass
    # elif isinstance(ast, Bool):
    #     print "bool"
    elif isinstance(ast, Name):
        pass
    elif isinstance(ast, Add):
        ast_print(ast.left)
        ast_print(ast.right)
    elif isinstance(ast, Compare):
        ast_print(ast.expr)
        ast_print(ast.ops)
    elif isinstance(ast, UnarySub):
        ast_print(ast.expr)
    elif isinstance(ast, Not):
        ast_print(ast.expr)
    elif isinstance(ast, CallFunc):
        ast_print(ast.node)
        ast_print(ast.args)
    elif isinstance(ast, List):
        ast_print(ast.nodes)
    elif isinstance(ast, list):
        for node in ast:
            ast_print(node)
    elif isinstance(ast, Set):
        for node in ast:
            ast_print(node)
    elif isinstance(ast, Dict):
        ast_print(ast.items)
    elif isinstance(ast, tuple):
        for node in ast:
            ast_print(node)
    elif isinstance(ast, dict):
        for key in ast:
            ast_print(ast[key])
    elif isinstance(ast, IfExp):
        ast_print(ast.test)
        ast_print(ast.then)
        ast_print(ast.else_)
    # elif isinstance(ast, Let):
    #     ast_print(ast.var)
    #     ast_print(ast.rhs)
    #     ast_print(ast.body)
    # elif isinstance(ast, InjectFrom):
    #     ast_print(ast.typ)
    #     ast_print(ast.arg)
    # elif isinstance(ast, ProjectTo):
    #     ast_print(ast.typ)
    #     ast_print(ast.arg)
    # elif isinstance(ast, GetTag):
    #     ast_print(ast.arg)
    # elif isinstance(ast, Lambda):
    #     ast_print(ast.argnames)
    #     ast_print(ast.code)
    elif isinstance(ast, Function):
        #ast_print(ast.name)
        #ast_print(ast.argnames)
        print ast.code
        ast_print(ast.code)
        def foo(x): #quick to enter function type
            print x
        all_variables[ast.name] = type(foo)
    elif isinstance(ast, CallFunc):
        ast_print(ast.node)
        ast_print(ast.args)
    # elif isinstance(ast, GlobalFuncName):
    #     ast_print(ast.name)
    elif isinstance(ast, Return):
        ast_print(ast.value)
    # elif isinstance(ast, str):
    #     print ast
    else:
        raise Exception("No AST match: " + str(ast))


ast_print(ast_tree)
print "\n_____________TYPES____________\n"
print all_variables