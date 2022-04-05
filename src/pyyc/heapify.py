import compiler
from dataTypes import *
from compiler.ast import *


def free_variable(ast, variable_list):
	if isinstance(ast, Module):
		return free_variable(ast.node, variable_list)
	elif isinstance(ast, Stmt):
		ret = set([])
		for node in ast.nodes:
			ret = ret | free_variable(node, variable_list)
		return ret
	elif isinstance(ast, Assign):
		return free_variable(ast.expr, variable_list) | free_variable(ast.nodes[0], variable_list)
	elif isinstance(ast, AssName):
		variable_list.add(ast.name)
		return set([])
	elif isinstance(ast, Discard):
		return free_variable(ast.expr, variable_list)
	elif isinstance(ast, Name):
		if not ast.name in variable_list:
			return set([ast.name])
		else:
			return set([])
	elif isinstance(ast, Add):
		return free_variable(ast.left, variable_list) | free_variable(ast.right, variable_list)
	elif isinstance(ast, Compare):
		return free_variable(ast.expr, variable_list) | free_variable(ast.ops[0][1], variable_list)
	elif isinstance(ast, UnarySub):
		return free_variable(ast.expr, variable_list)
	elif isinstance(ast, Not):
		return free_variable(ast.expr, variable_list)
	elif isinstance(ast, IfExp):
		return free_variable(ast.test, variable_list) | free_variable(ast.then, variable_list) | free_variable(ast.else_, variable_list)
	elif isinstance(ast, Let):
		variable_list.add(ast.var.name)
		return free_variable(ast.rhs, variable_list) | free_variable(ast.body, variable_list)
	elif isinstance(ast, InjectFrom):
		return free_variable(ast.arg, variable_list)
	elif isinstance(ast, ProjectTo):
		return free_variable(ast.arg, variable_list)
	elif isinstance(ast, GetTag):
		return free_variable(ast.arg, variable_list)
	elif isinstance(ast, Const):
		return set([])
	elif isinstance(ast, Bool):
		return set([])
	elif isinstance(ast, Return):
		return free_variable(ast.value, variable_list)
	elif isinstance(ast, Lambda):
		return set([])
	elif isinstance(ast, GlobalFuncName):
		return set([])
	elif isinstance(ast, CallFunc):
		ret = free_variable(ast.node, variable_list)
		for arg in ast.args:
			ret = ret | free_variable(arg, variable_list)
		return ret
	elif isinstance(ast, List):
		ret = set([])
		for thing in ast.nodes:
			ret = ret | free_variable(thing, variable_list)
		return ret
	elif isinstance(ast, Dict):
		ret = set([])
		for item in ast.items:
			ret = ret | free_variable(item[0], variable_list) | free_variable(item[1], variable_list)
		return ret
	else:
		raise Exception("No AST match: " + str(ast))

def determine_heap(ast):
	if isinstance(ast, Module):
		return determine_heap(ast.node)
	elif isinstance(ast, Stmt):
		ret = set([])
		for node in ast.nodes:
			ret = ret | determine_heap(node)
		return ret
	elif isinstance(ast, Assign):
		return determine_heap(ast.expr)
	elif isinstance(ast, Discard):
		return determine_heap(ast.expr)
	elif isinstance(ast, Const):
		return set([])
	elif isinstance(ast, Bool):
		return set([])
	elif isinstance(ast, Name):
		return set([])
	elif isinstance(ast, Add):
		return determine_heap(ast.left) | determine_heap(ast.right)
	elif isinstance(ast, Compare):
		return determine_heap(ast.expr) | determine_heap(ast.ops[0][1])
	elif isinstance(ast, UnarySub):
		return determine_heap(ast.expr)
	elif isinstance(ast, Not):
		return determine_heap(ast.expr)
	elif isinstance(ast, CallFunc):
		ret = determine_heap(ast.node)
		for arg in ast.args:
			ret = ret | determine_heap(arg)
		return ret
	elif isinstance(ast, IfExp):
		return determine_heap(ast.test) | determine_heap(ast.then) | determine_heap(ast.else_)
	elif isinstance(ast, Let):
		return determine_heap(ast.rhs) | determine_heap(ast.body)
	elif isinstance(ast, InjectFrom):
		return determine_heap(ast.arg)
	elif isinstance(ast, ProjectTo):
		return determine_heap(ast.arg)
	elif isinstance(ast, GetTag):
		return determine_heap(ast.arg)
	elif isinstance(ast, Lambda):
		return determine_heap(ast.code) | (free_variable(ast.code, set([])) - set(ast.argnames))
	elif isinstance(ast, GlobalFuncName):
		return set([])
	elif isinstance(ast, Return):
		return determine_heap(ast.value)
	elif isinstance(ast, List):
		ret = set([])
		for thing in ast.nodes:
			ret = ret | determine_heap(thing)
		return ret
	elif isinstance(ast, Dict):
		ret = set([])
		for item in ast.items:
			ret = ret | determine_heap(item[0]) | determine_heap(item[1])
		return ret
	else:
		raise Exception("No AST match: " + str(ast))


def local_variable(ast, variable_list):
	if isinstance(ast, Module):
		return local_variable(ast.node, variable_list)
	elif isinstance(ast, Stmt):
		ret = set([])
		for node in ast.nodes:
			ret = ret | local_variable(node, variable_list)
		return ret
	elif isinstance(ast, Assign):
		return local_variable(ast.expr, variable_list) | local_variable(ast.nodes[0], variable_list)
	elif isinstance(ast, AssName):
		if ast.name in variable_list:
			return set([ast.name])
		else:
			return set([])
	elif isinstance(ast, Discard):
		return local_variable(ast.expr, variable_list)
	elif isinstance(ast, Const):
		return set([])
	elif isinstance(ast, Bool):
		return set([])
	elif isinstance(ast, Name):
		return set([])
	elif isinstance(ast, Add):
		return local_variable(ast.left, variable_list) | local_variable(ast.right, variable_list)
	elif isinstance(ast, Compare):
		return local_variable(ast.expr, variable_list) | local_variable(ast.ops[0][1], variable_list)
	elif isinstance(ast, UnarySub):
		return local_variable(ast.expr, variable_list)
	elif isinstance(ast, Not):
		return local_variable(ast.expr, variable_list)
	elif isinstance(ast, CallFunc):
		ret = local_variable(ast.node, variable_list)
		for arg in ast.args:
			ret = ret | local_variable(arg, variable_list)
		return ret
	elif isinstance(ast, List):
		ret = set([])
		for thing in ast.nodes:
			ret = ret | local_variable(thing, variable_list)
		return ret
	elif isinstance(ast, Dict):
		ret = set([])
		for item in ast.items:
			ret = ret | local_variable(item[0], variable_list) | local_variable(item[1], variable_list)
		return ret
	elif isinstance(ast, IfExp):
		return local_variable(ast.test, variable_list) | local_variable(ast.then, variable_list) | determine_heap(ast.else_)
	elif isinstance(ast, Let):
		return local_variable(ast.rhs, variable_list) | local_variable(ast.body, variable_list)
	elif isinstance(ast, InjectFrom):
		return local_variable(ast.arg, variable_list)
	elif isinstance(ast, ProjectTo):
		return local_variable(ast.arg, variable_list)
	elif isinstance(ast, GetTag):
		return local_variable(ast.arg, variable_list)
	elif isinstance(ast, Lambda):
		return set([])
	elif isinstance(ast, GlobalFuncName):
		return set([])
	elif isinstance(ast, Return):
		return local_variable(ast.value, variable_list)
	else:
		raise Exception("No AST match: " + str(ast))

#still need to do final heapify function
