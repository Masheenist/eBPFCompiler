import compiler
from compiler.ast import *
from NewDataTypes import *
from heapify import find_frees

def add_variable(variable_list):
	ret = variable_list[0]
	variable_list[0] += 1
	return Name("l" + str(ret))

def add_function(function_list):
	return "f" + str(len(function_list))

def closure(ast):
	function_list = {}
	variable_list = [0]
	closure_recursive(ast, function_list, variable_list)
	return function_list

def closure_recursive(ast, function_list, variable_list):
	if isinstance(ast, Module):
		main = Lambda([], [], 0, closure_recursive(ast.node, function_list, variable_list))
		function_list["main"] = main
		return None
	elif isinstance(ast, Stmt):
		newStmts = []
		for node in ast.nodes:
			newStmts.append(closure_recursive(node, function_list, variable_list))
		return Stmt(newStmts)
	elif isinstance(ast, Assign):
		return Assign(ast.nodes, closure_recursive(ast.expr, function_list, variable_list))
	elif isinstance(ast, Discard):
		return Discard(closure_recursive(ast.expr, function_list, variable_list))
	elif isinstance(ast, Const):
		return ast
	elif isinstance(ast, Bool):
		return ast
	elif isinstance(ast, Name):
		return ast
	elif isinstance(ast, String):
		return ast
	elif isinstance(ast, Add):
		return Add((closure_recursive(ast.left, function_list, variable_list), closure_recursive(ast.right, function_list, variable_list)))
	elif isinstance(ast, Compare):
		return Compare(closure_recursive(ast.expr, function_list, variable_list),[(ast.ops[0][0], closure_recursive(ast.ops[0][1], function_list, variable_list))])
	elif isinstance(ast, UnarySub):
		return UnarySub(closure_recursive(ast.expr, function_list, variable_list))
	elif isinstance(ast, Not):
		return Not(closure_recursive(ast.expr, function_list, variable_list))
	elif isinstance(ast, CallFunc):
		if isinstance(ast.node, GlobalFuncName):
			newArgs = []
			for arg in ast.args:
				newArgs.append(closure_recursive(arg, function_list, variable_list))
			return CallFunc(ast.node, newArgs)
		else:
			new_var = add_variable(variable_list)
			newArgs = [CallFunc(GlobalFuncName('get_free_vars'), [new_var])]
			for arg in ast.args:
				newArgs.append(closure_recursive(arg, function_list, variable_list))
			return Let(new_var, closure_recursive(ast.node, function_list, variable_list), CallFunc(CallFunc(GlobalFuncName('get_fun_ptr'), [new_var]), newArgs))
	elif isinstance(ast, IfExp):
		return IfExp(closure_recursive(ast.test, function_list, variable_list), closure_recursive(ast.then, function_list, variable_list), closure_recursive(ast.else_, function_list, variable_list))
	elif isinstance(ast, Let):
		return Let(closure_recursive(ast.var, function_list, variable_list), closure_recursive(ast.rhs, function_list, variable_list), closure_recursive(ast.body, function_list, variable_list))
	elif isinstance(ast, InjectFrom):
		return InjectFrom(ast.typ, closure_recursive(ast.arg, function_list, variable_list))
	elif isinstance(ast, ProjectTo):
		return ProjectTo(ast.typ, closure_recursive(ast.arg, function_list, variable_list))
	elif isinstance(ast, GetTag):
		return GetTag(closure_recursive(ast.arg, function_list, variable_list))
	elif isinstance(ast, Lambda):
		new_code = closure_recursive(ast.code, function_list, variable_list)
		freeVars = find_frees(new_code, set([])) - set(ast.argnames)
		newStmts = []
		new_var = add_variable(variable_list)
		i = 0
		for var in freeVars:
			newStmts.append(Assign([AssName(var, 'OP_ASSIGN')], CallFunc(GlobalFuncName('get_subscript'),[new_var, Const(i)])))
			i += 1
		for stmt in new_code.nodes:
			newStmts.append(stmt)
		newargs = [new_var.name] + ast.argnames
		func_name = add_function(function_list)
		function_list[func_name] = Lambda(newargs, ast.defaults, ast.flags, Stmt(newStmts))
		free_var_names = []
		for var in freeVars:
			free_var_names.append(Name(var))
		return InjectFrom(Const(3), CallFunc(GlobalFuncName('create_closure_recursive'),[GlobalFuncName(func_name), List(free_var_names)]))
	elif isinstance(ast, GlobalFuncName):
		return ast
	elif isinstance(ast, Return):
		return Return(closure_recursive(ast.value, function_list, variable_list))
	elif isinstance(ast, List):
		newElem = []
		for elem in ast.nodes:
			newElem.append(closure_recursive(elem, function_list, variable_list))
		return List(newElem)
	elif isinstance(ast, Dict):
		newItems = []
		for item in ast.items:
			newItems.append((closure_recursive(item[0], function_list, variable_list), closure_recursive(item[1], function_list, variable_list)))
		return Dict(newItems)
	elif isinstance(ast, If):
		return If([(closure_recursive(ast.tests[0][0], function_list, variable_list), closure_recursive(ast.tests[0][1], function_list, variable_list))], closure_recursive(ast.else_, function_list, variable_list))
	elif isinstance(ast, While):
		return While(closure_recursive(ast.test, function_list, variable_list), closure_recursive(ast.body, function_list, variable_list), None)
	else:
		raise Exception("No AST match: " + str(ast))