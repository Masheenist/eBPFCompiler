import compiler
from dataTypes import *
from NewDataTypes import *
from compiler.ast import *


def find_frees(ast, variable_list):
	if isinstance(ast, Module):
		return find_frees(ast.node, variable_list)
	elif isinstance(ast, Stmt):
		ret = set([])
		for node in ast.nodes:
			ret = ret | find_frees(node, variable_list)
		return ret
	elif isinstance(ast, Assign):
		return find_frees(ast.expr, variable_list) | find_frees(ast.nodes[0], variable_list)
	elif isinstance(ast, AssName):
		variable_list.add(ast.name)
		return set([])
	elif isinstance(ast, Discard):
		return find_frees(ast.expr, variable_list)
	elif isinstance(ast, Name):
		if not ast.name in variable_list:
			return set([ast.name])
		else:
			return set([])
	elif isinstance(ast, Add):
		return find_frees(ast.left, variable_list) | find_frees(ast.right, variable_list)
	elif isinstance(ast, Compare):
		return find_frees(ast.expr, variable_list) | find_frees(ast.ops[0][1], variable_list)
	elif isinstance(ast, UnarySub):
		return find_frees(ast.expr, variable_list)
	elif isinstance(ast, Not):
		return find_frees(ast.expr, variable_list)
	elif isinstance(ast, IfExp):
		return find_frees(ast.test, variable_list) | find_frees(ast.then, variable_list) | find_frees(ast.else_, variable_list)
	elif isinstance(ast, Let):
		variable_list.add(ast.var.name)
		return find_frees(ast.rhs, variable_list) | find_frees(ast.body, variable_list)
	elif isinstance(ast, InjectFrom):
		return find_frees(ast.arg, variable_list)
	elif isinstance(ast, ProjectTo):
		return find_frees(ast.arg, variable_list)
	elif isinstance(ast, GetTag):
		return find_frees(ast.arg, variable_list)
	elif isinstance(ast, Const):
		return set([])
	elif isinstance(ast, Bool):
		return set([])
	elif isinstance(ast, Return):
		return find_frees(ast.value, variable_list)
	elif isinstance(ast, Lambda):
		return set([])
	elif isinstance(ast, GlobalFuncName):
		return set([])
	elif isinstance(ast, CallFunc):
		ret = find_frees(ast.node, variable_list)
		for arg in ast.args:
			ret = ret | find_frees(arg, variable_list)
		return ret
	elif isinstance(ast, List):
		ret = set([])
		for thing in ast.nodes:
			ret = ret | find_frees(thing, variable_list)
		return ret
	elif isinstance(ast, Dict):
		ret = set([])
		for item in ast.items:
			ret = ret | find_frees(item[0], variable_list) | find_frees(item[1], variable_list)
		return ret
	elif isinstance(ast, If):
		return find_frees(ast.tests[0][0], variable_list) | find_frees(ast.tests[0][1], variable_list) | find_frees(ast.else_, variable_list)
	elif isinstance(ast, While):
		return find_frees(ast.test, variable_list) | find_frees(ast.body, variable_list)
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
		return determine_heap(ast.code) | (find_frees(ast.code, set([])) - set(ast.argnames))
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
	elif isinstance(ast, If):
		return determine_heap(ast.tests[0][0]) | determine_heap(ast.tests[0][1]) | determine_heap(ast.else_)
	elif isinstance(ast, While):
		return determine_heap(ast.test) | determine_heap(ast.body)
	else:
		raise Exception("No AST match: " + str(ast))

def find_locals(ast, variable_list):
	if isinstance(ast, Module):
		return find_locals(ast.node, variable_list)
	elif isinstance(ast, Stmt):
		ret = set([])
		for node in ast.nodes:
			ret = ret | find_locals(node, variable_list)
		return ret
	elif isinstance(ast, Assign):
		return find_locals(ast.expr, variable_list) | find_locals(ast.nodes[0], variable_list)
	elif isinstance(ast, AssName):
		if ast.name in variable_list:
			return set([ast.name])
		else:
			return set([])
	elif isinstance(ast, Discard):
		return find_locals(ast.expr, variable_list)
	elif isinstance(ast, Const):
		return set([])
	elif isinstance(ast, Bool):
		return set([])
	elif isinstance(ast, Name):
		return set([])
	elif isinstance(ast, Add):
		return find_locals(ast.left, variable_list) | find_locals(ast.right, variable_list)
	elif isinstance(ast, Compare):
		return find_locals(ast.expr, variable_list) | find_locals(ast.ops[0][1], variable_list)
	elif isinstance(ast, UnarySub):
		return find_locals(ast.expr, variable_list)
	elif isinstance(ast, Not):
		return find_locals(ast.expr, variable_list)
	elif isinstance(ast, CallFunc):
		ret = find_locals(ast.node, variable_list)
		for arg in ast.args:
			ret = ret | find_locals(arg, variable_list)
		return ret
	elif isinstance(ast, List):
		ret = set([])
		for thing in ast.nodes:
			ret = ret | find_locals(thing, variable_list)
		return ret
	elif isinstance(ast, Dict):
		ret = set([])
		for item in ast.items:
			ret = ret | find_locals(item[0], variable_list) | find_locals(item[1], variable_list)
		return ret
	elif isinstance(ast, IfExp):
		return find_locals(ast.test, variable_list) | find_locals(ast.then, variable_list) | determine_heap(ast.else_)
	elif isinstance(ast, Let):
		return find_locals(ast.rhs, variable_list) | find_locals(ast.body, variable_list)
	elif isinstance(ast, InjectFrom):
		return find_locals(ast.arg, variable_list)
	elif isinstance(ast, ProjectTo):
		return find_locals(ast.arg, variable_list)
	elif isinstance(ast, GetTag):
		return find_locals(ast.arg, variable_list)
	elif isinstance(ast, Lambda):
		return set([])
	elif isinstance(ast, GlobalFuncName):
		return set([])
	elif isinstance(ast, Return):
		return find_locals(ast.value, variable_list)
	elif isinstance(ast, If):
		return find_locals(ast.tests[0][0], variable_list) | find_locals(ast.tests[0][1], variable_list) | find_locals(ast.else_, variable_list)
	elif isinstance(ast, While):
		return find_locals(ast.test, variable_list) | find_locals(ast.body, variable_list)
	else:
		raise Exception("No AST match: " + str(ast))

def heapify(ast, variables):
	if isinstance(ast, Module):
		local_list = find_locals(ast.node, variables)
		statement_list = []
		for var in local_list:
			statement_list.append(Assign([AssName(var, 'OP_ASSIGN')], List([Const(0)])))
		old_statement = heapify(ast.node, variables)
		for statement in old_statement.nodes:
			statement_list.append(statement)
		return Module(ast.doc, Stmt(statement_list))
	elif isinstance(ast, Stmt):
		statement_list = []
		for node in ast.nodes:
			statement_list.append(heapify(node, variables))
		return Stmt(statement_list)
	elif isinstance(ast, Assign):
		if ast.nodes[0].name in variables:
			return Discard(CallFunc(GlobalFuncName("set_subscript"), [Name(ast.nodes[0].name), Const(0), heapify(ast.expr, variables)]))
		else:
			return Assign(ast.nodes, heapify(ast.expr, variables))
	elif isinstance(ast, Discard):
		return Discard(heapify(ast.expr, variables))
	elif isinstance(ast, Const):
		return ast
	elif isinstance(ast, Bool):
		return ast
	elif isinstance(ast, Name):
		if ast.name in variables:
			return CallFunc(GlobalFuncName("get_subscript"),[ast, Const(0)])
		else:
			return ast
	elif isinstance(ast, Add):
		return Add((heapify(ast.left, variables), heapify(ast.right, variables)))
	elif isinstance(ast, Compare):
		return Compare(heapify(ast.expr, variables),[(ast.ops[0][0], heapify(ast.ops[0][1], variables))])
	elif isinstance(ast, UnarySub):
		return UnarySub(heapify(ast.expr, variables))
	elif isinstance(ast, Not):
		return Not(heapify(ast.expr, variables))
	elif isinstance(ast, CallFunc):
		func_args = []
		for arg in ast.args:
			func_args.append(heapify(arg, variables))
		return CallFunc(heapify(ast.node, variables), func_args)
	elif isinstance(ast, List):
		list_items = []
		for elem in ast.nodes:
			list_items.append(heapify(elem, variables))
		return List(list_items)
	elif isinstance(ast, Dict):
		dict_items = []
		for item in ast.items:
			dict_items.append((heapify(item[0], variables), heapify(item[1], variables)))
		return Dict(dict_items)
	elif isinstance(ast, IfExp):
		return IfExp(heapify(ast.test, variables), heapify(ast.then, variables), heapify(ast.else_, variables))
	elif isinstance(ast, Let):
		return Let(heapify(ast.var, variables), heapify(ast.rhs, variables), heapify(ast.body, variables))
	elif isinstance(ast, InjectFrom):
		return InjectFrom(ast.typ, heapify(ast.arg, variables))
	elif isinstance(ast, ProjectTo):
		return ProjectTo(ast.typ, heapify(ast.arg, variables))
	elif isinstance(ast, GetTag):
		return GetTag(heapify(ast.arg, variables))
	elif isinstance(ast, Lambda):
		func_args = []
		statement_list = []
		for arg in ast.argnames:
			if arg in variables:
				func_args.append(arg + "h")
				statement_list.append(Assign([AssName(arg, 'OP_ASSIGN')], List([Const(0)])))
				statement_list.append(Discard(CallFunc(GlobalFuncName("set_subscript"), [Name(arg), Const(0), Name(arg + "h")])))
			else:
				func_args.append(arg)
		local_list = find_locals(ast.code, variables)
		for var in local_list:
			statement_list.append(Assign([AssName(var, 'OP_ASSIGN')], List([Const(0)])))
		old_statement = heapify(ast.code, variables)
		for statement in old_statement.nodes:
			statement_list.append(statement)
		return Lambda(func_args, ast.defaults, ast.flags, Stmt(statement_list))
	elif isinstance(ast, GlobalFuncName):
		return ast
	elif isinstance(ast, Return):
		return Return(heapify(ast.value, variables))
	elif isinstance(ast, If):
		return If([(heapify(ast.tests[0][0], variables), heapify(ast.tests[0][1], variables))], heapify(ast.else_, variables))
	elif isinstance(ast, While):
		return While(heapify(ast.test, variables), heapify(ast.body, variables), None)
	else:
		raise Exception("No AST match in heapify: " + str(ast))