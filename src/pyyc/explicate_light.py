import compiler
from compiler.ast import *
from dataTypes import *
from NewDataTypes import *

INT = 0
BOOL = 1
BIG = 3

def explicate(ast, variable_list):
	runtime_functions = ["print_any", "input", "get_subscript", "set_subscript", "create_list", "abort", "equal", "add"]
	if isinstance(ast, Module):
		return Module(None, explicate(ast.node, variable_list))
	
	elif isinstance(ast, Stmt):
		new_statements = []
		for statement in ast.nodes:
			new_statements.append(explicate(statement, variable_list))
		return Stmt(new_statements)
	
	elif isinstance(ast, Lambda):
		print "HAHAHAAHHAAHAH"
		# return Lambda(ast.argnames, ast.defaults, ast.flags, Stmt([Return(explicate(ast.code, variable_list))]))
		return Lambda(ast.argnames, ast.defaults, ast.flags, explicate(ast.code, variable_list))
	
	elif isinstance(ast, Printnl):
		# print "HERE! I AM HERE"
		return Discard(CallFunc(GlobalFuncName("print_int_nl"), [explicate(ast.nodes[0], variable_list)]))
	
	elif isinstance(ast, Assign):
		if isinstance(ast.nodes[0], Subscript):
			return Discard(CallFunc(GlobalFuncName("set_subscript"), [explicate(ast.nodes[0].expr, variable_list), explicate(ast.nodes[0].subs[0], variable_list), explicate(ast.expr, variable_list)]))
		else:
			return Assign([explicate(ast.nodes[0], variable_list)], explicate(ast.expr, variable_list))
	
	elif isinstance(ast, Name):
		if ast.name == "True":
			return InjectFrom(Const(BOOL),Bool(True))
		elif ast.name == "False":
			return InjectFrom(Const(BOOL),Bool(False))
		elif ast.name in runtime_functions:
			return GlobalFuncName(ast.name)
		else:
			return ast

	# elif isinstance(ast, IfExp):
	# 	# new_variable = add_variable(variable_list)
	# 	return IfExp(Let(new_variable, explicate(ast.test, variable_list), getBool(new_variable, variable_list)), explicate(ast.then, variable_list), explicate(ast.else_, variable_list))

	else:
		return ast