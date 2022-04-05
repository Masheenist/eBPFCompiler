import compiler
from compiler.ast import *
from dataTypes import *
from NewDataTypes import *

INT = 0
BOOL = 1
BIG = 3

def add_variable(variables):
	ret = Name(str(len(variables)))
	variables[ret] = name
	return ret

def ifElseChain(conditions, actions):
	if len(conditions) != (len(actions) - 1):
		raise Exception("conditions error")
	struct = actions[-1]
	for i in range(len(conditions)):
		struct = IfExp(conditions[i], actions[i], struct)
	return struct

def qAnd(e1,e2, variables):
	x = add_variable(variables)
	return Let(x, e1, IfExp( x, e2, x))

def qOr(e1,e2, variables):
	x = add_variable(variables)
	return Let(x, e1, IfExp(Not(x), e2, x))

def getBool(e1, variables):
	conditions = [
	    qOr(
	        Compare(GetTag(e1), [("==", Const(INT))]),
	        Compare(GetTag(e1), [("==", Const(BOOL))]),
	        variables,
	    )
	]
	actions = [ProjectTo(Const(BOOL), e1)]
	conditions.append(Compare(GetTag(e1), [("==", Const(BIG))] ))
	actions.extend((
	    Not(
	        qOr(
	            CallFunc(GlobalFuncName(
	                "equal",
	                [
	                    ProjectTo(Const(BIG), e1),
	                    ProjectTo(Const(BIG), List([])),
	                ],
	            ),
	            CallFunc(GlobalFuncName(
	                "equal",
	                [
	                    ProjectTo(Const(BIG), e1),
	                    ProjectTo(Const(BIG), Dict([])),
	                ],
	            ),
	            variables,
	        )),
	    CallFunc(GlobalFuncName("abort", []),
	)))))
	return ifElseChain(conditions, actions)

def explicate(ast, variable_list):
	if isinstance(ast, Module):
		return Module(None, explicate(ast.node, variable_list))
	elif isinstance(ast, Stmt):
		new_statements = []
		for statement in ast.nodes:
			new_statements.append(explicate(statement, variable_list))
		return Stmt(new_statements)
	elif isinstance(ast, Printnl):
		return Discard(CallFunc(GlobalFuncName("print_any"), [explicate(ast.nodes[0], variable_list)]))
	elif isinstance(ast, Return):
		return Return(explicate(ast.value, variable_list))
	elif isinstance(ast, Lambda):
		# return Lambda(ast.argnames, ast.defaults, ast.flags, Stmt([Return(explicate(ast.code, variable_list))]))
		return Lambda(ast.argnames, ast.defaults, ast.flags, explicate(ast.code, variable_list))
	# elif isinstance(ast, Function):
	# 	return Assign([AssName(ast.name, 'OP_ASSIGN')],Lambda(ast.argnames, ast.defaults, ast.flags, explicate(ast.code, variable_list)))
	elif isinstance(ast, Subscript):
		if ast.flags == 'OP_APPLY':
			return CallFunc(GlobalFuncName("get_subscript"), [explicate(ast.expr, variable_list),explicate(ast.subs[0], variable_list)])
	elif isinstance(ast, Assign):
		if isinstance(ast.nodes[0], Subscript):
			return Discard(CallFunc(GlobalFuncName("set_subscript"), [explicate(ast.nodes[0].expr, variable_list), explicate(ast.nodes[0].subs[0], variable_list), explicate(ast.expr, variable_list)]))
		else:
			return Assign([explicate(ast.nodes[0], variable_list)], explicate(ast.expr, variable_list))
	elif isinstance(ast, Dict):
		new_dict = []
		for item in ast.items:
			new_dict.append((explicate(item[0],variable_list),explicate(item[1],variable_list)))
		return Dict(new_dict)
	elif isinstance(ast, List):
		new_list = []
		for node in ast.nodes:
			new_list.append(explicate(node, variable_list))
		return List(new_list)
	elif isinstance(ast, AssName):
		return ast
	elif isinstance(ast, Discard):
		return Discard(explicate(ast.expr, variable_list))
	elif isinstance(ast, Const):
		return InjectFrom(Const(INT), ast)
	elif isinstance(ast, Name):
		if ast.name == "True":
			return InjectFrom(Const(BOOL),Bool(True))
		elif ast.name == "False":
			return InjectFrom(Const(BOOL),Bool(False))
		elif ast.name in runtime_functions:
			return GlobalFuncName(ast.name)
		else:
			return ast
	elif isinstance(ast, UnarySub):
		new_variable = add_variable(variable_list)
		conditions = [qOr(Compare(GetTag(new_variable), [("==", Const(INT))] ), Compare(GetTag(new_variable), [("==", Const(BOOL))] ), variable_list)]
		operations = [InjectFrom(Const(INT), UnarySub(ProjectTo(Const(INT), new_variable))), CallFunc(GlobalFuncName("abort"), [])]
		return Let(new_variable, explicate(ast.expr, variable_list), ifElseChain(conditions, operations))
	elif isinstance(ast, CallFunc):
		print "explicate now handling", ast
		print "\n\n"
		new_args = []
		for arg in ast.args:
			new_args.append(explicate(arg, variable_list))
		node = explicate(ast.node, variable_list)
		if isinstance(node, GlobalFuncName):
			if node.name == "input":
				return InjectFrom(Const(0), CallFunc(explicate(ast.node, variable_list), new_args))
		return CallFunc(explicate(ast.node, variable_list), new_args)
	elif isinstance(ast, Add):
		left = add_variable(variable_list)
		right = add_variable(variable_list)
		conditions = []
		operations = []
		conditions.append(qOr(qAnd(Compare(GetTag(left), [('==', Const(INT))]), Compare(GetTag(right), [('==', Const(INT))]), variable_list),qAnd(Compare(GetTag(left), [('==', Const(BOOL))]), Compare(GetTag(right), [('==', Const(BOOL))]), variable_list), variable_list))
		operations.append(InjectFrom(Const(INT), Add((ProjectTo(Const(INT), left),ProjectTo(Const(INT),right)))))
		conditions.append(qAnd(Compare(GetTag(left), [('==', Const(BIG))]), Compare(GetTag(right), [('==', Const(BIG))]), variable_list))
		operations.append(InjectFrom(Const(BIG),CallFunc(GlobalFuncName("add"), [ProjectTo(Const(BIG), left), ProjectTo(Const(BIG), right)])))
		operations.append(CallFunc(GlobalFuncName("abort"), []))
		return Let(left, explicate(ast.left, variable_list), Let(right, explicate(ast.right, variable_list), ifElseChain(conditions,operations)))
	elif isinstance(ast, IfExp):
		new_variable = add_variable(variable_list)
		return IfExp(Let(new_variable, explicate(ast.test, variable_list), getBool(new_variable, variable_list)), explicate(ast.then, variable_list), explicate(ast.else_, variable_list))
	elif isinstance(ast, Not):
		new_variable = add_variable(variable_list)
		return Let(new_variable, explicate(ast.expr, variable_list), InjectFrom(Const(BOOL), Not(getBool(new_variable, variable_list))))
	elif isinstance(ast, And):
		new_variable = add_variable(variable_list)
		return Let(new_variable, explicate(ast.nodes[0], variable_list), IfExp(getBool(new_variable, variable_list), explicate(ast.nodes[1], variable_list), new_variable))
	elif isinstance(ast, Or):
		x = add_variable(variable_list)
		return Let(new_variable, explicate(ast.nodes[0], variable_list), IfExp(Not(getBool(new_variable, variable_list)), explicate(ast.nodes[1], variable_list), new_variable))
	elif isinstance(ast, Compare):
		if ast.ops[0][0] != "is":
			left = add_variable(variable_list)
			right = add_variable(variable_list)
			conditions = []
			operations = []
			conditions.append(qOr(qAnd(Compare(GetTag(left), [('==', Const(INT))]), Compare(GetTag(right), [('==', Const(INT))]), variable_list),qAnd(Compare(GetTag(left), [('==', Const(BOOL))]), Compare(GetTag(right), [('==', Const(BOOL))]), variable_list), variable_list))
			operations.append(InjectFrom(Const(BOOL), Compare(ProjectTo(Const(INT), left),[(ast.ops[0][0],ProjectTo(Const(INT),right))])))
			conditions.append(qAnd(Compare(GetTag(left), [('==', Const(BIG))]), Compare(GetTag(right), [('==', Const(BIG))]), variable_list))
			operations.append(InjectFrom(Const(BOOL),CallFunc(GlobalFuncName("equal"), [ProjectTo(Const(BIG), left), ProjectTo(Const(BIG), right)])))
			operations.append(CallFunc(GlobalFuncName("abort"), []))
			return Let(left, explicate(ast.expr, variable_list), Let(right, explicate(ast.ops[0][1], variable_list), ifElseChain(conditions,operations)))
		else:
			return InjectFrom(Const(BOOL), Compare(explicate(ast.expr, variable_list), [("==", explicate(ast.ops[0][1], variable_list))]))
	elif isinstance(ast, FunctionLabel):
		return ast
	else:
		print ast
		raise Exception('Error: unrecognized AST node - explicate')
