import compiler
from compiler.ast import *
from dataTypes import *
from NewDataTypes import *

protected_names = ["True", "False", "input"]

def add_variable(name, variable_list, assignment):
	if name in protected_names:
		return name
	if assignment:
		if name in variable_list[-1]:
			return variable_list[-1][name]
	else:
		for i in range(len(variable_list) - 1, 0, -1):
			if name in variable_list[i]:
				return variable_list[i][name]
	new_var = "u" + str(variable_list[0])
	variable_list[len(variable_list) - 1][name] = new_var
	variable_list[0] += 1
	return new_var

def uniquify_wrapper(ast):
	variable_list = [0, {}]
	return uniquify(ast, variable_list)

def uniquify_search(ast, variable_list):
	if isinstance(ast, Module):
		uniquify_search(ast.node, variable_list)
	elif isinstance(ast, Stmt):
		for statement in ast.nodes:
			uniquify_search(statement, variable_list)
	elif isinstance(ast, Printnl):
		uniquify_search(ast.nodes[0], variable_list)
	elif isinstance(ast, Assign):
		uniquify_search(ast.nodes[0], variable_list)
		uniquify_search(ast.expr, variable_list)
	elif isinstance(ast, AssName):
		add_variable(ast.name, variable_list, True)
	elif isinstance(ast, Discard):
		uniquify_search(ast.expr, variable_list)
	elif isinstance(ast, Const):
		pass
	elif isinstance(ast, String):
		pass
	elif isinstance(ast, Name):
		pass
	elif isinstance(ast, Add):
		uniquify_search(ast.left, variable_list)
		uniquify_search(ast.right, variable_list)
	elif isinstance(ast, Compare):
		uniquify_search(ast.expr, variable_list)
		uniquify_search(ast.ops[0][1], variable_list)
	elif isinstance(ast, And):
		uniquify_search(ast.nodes[0], variable_list)
		uniquify_search(ast.nodes[1], variable_list)
	elif isinstance(ast, Or):
		uniquify_search(ast.nodes[0], variable_list)
		uniquify_search(ast.nodes[1], variable_list)
	elif isinstance(ast, UnarySub):
		uniquify_search(ast.expr, variable_list)
	elif isinstance(ast, Not):
		uniquify_search(ast.expr, variable_list)
	elif isinstance(ast, CallFunc):
		for arg in ast.args:
			uniquify_search(arg, variable_list)
		uniquify_search(ast.node, variable_list)
	elif isinstance(ast, List):
		for node in ast.nodes:
			uniquify_search(node, variable_list)
	elif isinstance(ast, Dict):
		for item in ast.items:
			uniquify_search(item[0],variable_list)
			uniquify_search(item[1],variable_list)
	elif isinstance(ast, Subscript):
		uniquify_search(ast.expr, variable_list)
		uniquify_search(ast.subs[0], variable_list)
	elif isinstance(ast, IfExp):
		uniquify_search(ast.test, variable_list)
		uniquify_search(ast.then, variable_list)
		uniquify_search(ast.else_, variable_list)
	elif isinstance(ast, Return):
		uniquify_search(ast.value, variable_list)
	elif isinstance(ast, Function):
		func_name = add_variable(ast.name, variable_list, True)
	elif isinstance(ast, Lambda):
		pass
	elif isinstance(ast, If):
		uniquify_search(ast.tests[0][0], variable_list)
		uniquify_search(ast.tests[0][1], variable_list)
		uniquify_search(ast.else_, variable_list)
	elif isinstance(ast, While):
		uniquify_search(ast.test, variable_list)
		uniquify_search(ast.body, variable_list)
	elif isinstance(ast, Let):
		uniquify_search(ast.var, variable_list)
		uniquify_search(ast.rhs, variable_list)
		uniquify_search(ast.body, variable_list)
	elif isinstance(ast, GlobalFuncName):
		pass
	else:
		raise Exception("No AST match: " + str(ast))


def uniquify(ast, variable_list):
	if isinstance(ast, Module):
		uniquify_search(ast.node, variable_list)
		return Module(None, uniquify(ast.node, variable_list))
	elif isinstance(ast, Stmt):
		newStmts = []
		for statement in ast.nodes:
			newStmts.append(uniquify(statement, variable_list))
		return Stmt(newStmts)
	elif isinstance(ast, Printnl):
		return Printnl([uniquify(ast.nodes[0], variable_list)], ast.dest)
	elif isinstance(ast, Assign):
		return Assign([uniquify(ast.nodes[0], variable_list)], uniquify(ast.expr, variable_list))
	elif isinstance(ast, AssName):
		return AssName(add_variable(ast.name, variable_list, False), ast.flags)
	elif isinstance(ast, Discard):
		return Discard(uniquify(ast.expr, variable_list))
	elif isinstance(ast, Const):
		return ast
	elif isinstance(ast, String):
		return ast
	elif isinstance(ast, Name):
		return Name(add_variable(ast.name, variable_list, False))
	elif isinstance(ast, Add):
		return Add((uniquify(ast.left, variable_list), uniquify(ast.right, variable_list)))
	elif isinstance(ast, Compare):
		return Compare(uniquify(ast.expr, variable_list),[(ast.ops[0][0],uniquify(ast.ops[0][1], variable_list))])
	elif isinstance(ast, And):
		return And([uniquify(ast.nodes[0], variable_list),uniquify(ast.nodes[1], variable_list)])
	elif isinstance(ast, Or):
		return Or([uniquify(ast.nodes[0], variable_list),uniquify(ast.nodes[1], variable_list)])
	elif isinstance(ast, UnarySub):
		return UnarySub(uniquify(ast.expr, variable_list))
	elif isinstance(ast, Not):
		return Not(uniquify(ast.expr, variable_list))
	elif isinstance(ast, CallFunc):
		uniqArgs = []
		for arg in ast.args:
			uniqArgs.append(uniquify(arg, variable_list))
		return CallFunc(uniquify(ast.node, variable_list), uniqArgs)
	elif isinstance(ast, List):
		newNodes = []
		for node in ast.nodes:
			newNodes.append(uniquify(node, variable_list))
		return List(newNodes)
	elif isinstance(ast, Dict):
		newItems = []
		for item in ast.items:
			newItems.append((uniquify(item[0],variable_list),uniquify(item[1],variable_list)))
		return Dict(newItems)
	elif isinstance(ast, Subscript):
		return Subscript(uniquify(ast.expr, variable_list), ast.flags, [uniquify(ast.subs[0], variable_list)])
	elif isinstance(ast, IfExp):
		return IfExp(uniquify(ast.test, variable_list), uniquify(ast.then, variable_list), uniquify(ast.else_, variable_list))
	elif isinstance(ast, Return):
		return Return(uniquify(ast.value, variable_list))
	elif isinstance(ast, Function):
		func_name = add_variable(ast.name, variable_list, False)
		variable_list.append({})
		new_argNames = []
		for arg in ast.argnames:
			new_argNames.append(add_variable(arg, variable_list, True))
		uniquify_search(ast.code, variable_list)
		ret = Function(None, func_name, new_argNames, [], 0, None, uniquify(ast.code, variable_list))
		del variable_list[-1]
		return ret
	elif isinstance(ast, Lambda):
		variable_list.append({})
		new_argNames = []
		for arg in ast.argnames:
			new_argNames.append(add_variable(arg, variable_list, True))
		uniquify_search(ast.code, variable_list)
		ret = Lambda(new_argNames, [], 0, uniquify(ast.code, variable_list))
		del variable_list[-1]
		return ret
	elif isinstance(ast, If):
		return If([(uniquify(ast.tests[0][0], variable_list), uniquify(ast.tests[0][1], variable_list))], uniquify(ast.else_, variable_list))
	elif isinstance(ast, While):
		return While(uniquify(ast.test, variable_list), uniquify(ast.body, variable_list), None)
	elif isinstance(ast, Let):
		return Let(uniquify(ast.var, variable_list), uniquify(ast.rhs, variable_list), uniquify(ast.body, variable_list))
	elif isinstance(ast, GlobalFuncName):
		return ast
	else:
		raise Exception("No AST match: " + str(ast))