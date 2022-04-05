import compiler
from compiler.ast import *
from NewDataTypes import *

INT = 0
BOOL = 1
BIG = 3
PYOBJ = 4
NONE = -1
FUNCRET = -2

class StmtActor:
	labeledType = Stmt
	def DoOption(self, received_types, ast, variables):
		valid_type = NONE
		received_types.extend(type_selector().type_check(i, variables) for i in ast.nodes)
		ret = NONE

class ModuleActor:
	labeledType = Module
	def DoOption(self, received_types, ast, variables):
		valid_type = NONE
		received_types.append(type_selector().type_check(ast.node, variables))
		ret = NONE

class AssignActor:
	labeledType = Assign
	def DoOption(self, received_types, ast, variables):
		valid_type = PYOBJ
		typ = type_selector().type_check(ast.expr, variables)
		received_types.append(typ)
		variables[ast.nodes[0].name] = typ
		ret = NONE

class DiscardActor:
	labeledType = Module
	def DoOption(self, received_types, ast, variables):
		valid_type = PYOBJ
		received_types.append(type_selector().type_check(ast.expr, variables))
		ret = NONE

class ConstActor:
	labeledType = Const
	def DoOption(self, received_types, ast, variables):
		return INT

class BoolActor:
	labeledType = Bool
	def DoOption(self, received_types, ast, variables):
		return BOOL

class NameActor:
	labeledType = Name
	def DoOption(self, received_types, ast, variables):
		return variables[ast.name]

class AddActor:
	labeledType = Add
	def DoOption(self, received_types, ast, variables):
		valid_type = INT
		received_types.extend((type_selector().type_check(ast.left, variables), type_selector().type_check(ast.right, variables)))
		ret = INT

class CompareActor:
	labeledType = Compare
	def DoOption(self, received_types, ast, variables):
		valid_type = INT
		typ1 = type_selector().type_check(ast.expr, variables)
		typ2 = type_selector().type_check(ast.ops[0][1], variables)
		if typ1 == typ2 or typ1 == FUNCRET or typ2 == FUNCRET:
 			return BOOL

class UnarySubActor:
	labeledType = UnarySub
	def DoOption(self, received_types, ast, variables):
		valid_type = INT
		received_types.append(type_selector().type_check(ast.expr, variables))
		ret = INT

class NotActor:
	labeledType = Not
	def DoOption(self, received_types, ast, variables):
		valid_type = BOOL
		received_types.append(type_selector().type_check(ast.expr, variables))
		ret = BOOL

class CallFuncActor:
	labeledType = CallFunc
	def DoOption(self, received_types, ast, variables):
		for i in ast.args:
 			type_selector().type_check(i, variables)
		return FUNCRET

class ListActor:
	labeledType = List
	def DoOption(self, received_types, ast, variables):
		valid_type = PYOBJ
		received_types.extend(type_selector().type_check(i, variables) for i in ast.nodes)
		ret = PYOBJ

class DictActor:
	labeledType = Dict
	def DoOption(self, received_types, ast, variables):
		valid_type = PYOBJ
		for current_item in ast.items:
			received_types.extend((type_selector().type_check(current_item[0], variables), type_selector().type_check(current_item[1], variables)))
 		ret = PYOBJ

class IfExpActor:
	labeledType = IfExp
	def DoOption(self, received_types, ast, variables):
		typ = type_selector().type_check(ast.test, variables)
		if typ != BOOL:
			ValueError("Type mis-match returns:{str(ast)}, {str(typ)}, {str(BOOL)}")
			#raise Exception("Type mis-match returns:{str(ast)}, {str(typ)}, {str(BOOL)}")
 		typ1 = type_selector().type_check(ast.then, variables)
 		typ2 = type_selector().type_check(ast.else_, variables)
 		if typ1 == typ2 or typ1 != FUNCRET and typ2 == FUNCRET:
 			return typ1
 		elif typ1 == FUNCRET:
 			return typ2
		else:
			ValueError("Type mis-match returns:{str(ast)}, {str(typ1)}, {str(typ2)}")
 			#raise Exception("Type mis-match returns:{str(ast)}, {str(typ1)}, {str(typ2)}")

class LetActor:
	labeledType = Let
	def DoOption(self, received_types, ast, variables):
		typ = type_selector().type_check(ast.rhs, variables)
		received_types.append(typ)
		variables[ast.var.name] = typ
		return type_selector().type_check(ast.body, variables)

class InjectFromActor:
	labeledType = InjectFrom
	def DoOption(self, received_types, ast, variables):
		valid_type = ast.typ.value
		received_types.append(type_selector().type_check(ast.arg, variables))
		ret = PYOBJ

class ProjectToActor:
	labeledType = ProjectTo
	def DoOption(self, received_types, ast, variables):
		valid_type = PYOBJ
		received_types.append(type_selector().type_check(ast.arg, variables))
		ret = ast.typ.value

class GetTagActor:
	labeledType = GetTag
	def DoOption(self, received_types, ast, variables):
		valid_type = PYOBJ
		received_types.append(type_selector().type_check(ast.arg, variables))
		ret = INT


class type_selector:

	def type_check(self, ast, variables):
		eligible_actors = [
			StmtActor(),
			ModuleActor(),
			AssignActor(),
			DiscardActor(),
			ConstActor(),
			BoolActor(),
			NameActor(),
			AddActor(),
			CompareActor(),
			UnarySubActor(),
			NotActor(),
			CallFuncActor(),
			ListActor(),
			DictActor(),
			IfExpActor(),
			LetActor(),
			InjectFromActor(),
			GetTagActor()
		]

		received_types = []

		for i in received_types:
			if i not in [valid_type, FUNCRET]:
				ValueError("Type mis-match:{str(ast)}, {str(i)}, {str(valid_type)}")
				#raise Exception("Type mis-match:{str(ast)}, {str(i)}, {str(valid_type)}")

		for currentActor in eligible_actors :
			if isinstance(ast, currentActor.labeledType):
				return currentActor.DoOption(received_types, ast, variables)

		#return ret

##def type_check(ast, variables):
##	received_types = []
#	if isinstance(ast, Module):
#		valid_type = NONE
#		received_types.append(type_check(ast.node, variables))
#		ret = NONE
#	elif isinstance(ast, Stmt):
#		valid_type = NONE
#		received_types.extend(type_check(i, variables) for i in ast.nodes)
#		ret = NONE
#	elif isinstance(ast, Assign):
#		valid_type = PYOBJ
#		typ = type_check(ast.expr, variables)
#		received_types.append(typ)
#		variables[ast.nodes[0].name] = typ
#		ret = NONE
#	elif isinstance(ast, Discard):
#		valid_type = PYOBJ
#		received_types.append(type_check(ast.expr, variables))
#		ret = NONE
#	elif isinstance(ast, Const):
#		return INT
#	elif isinstance(ast, Bool):
#		return BOOL
#	elif isinstance(ast, Name):
#		return variables[ast.name]
#	elif isinstance(ast, Add):
#		valid_type = INT
#		received_types.extend((type_check(ast.left, variables),
#		                      type_check(ast.right, variables)))
#		ret = INT
#	elif isinstance(ast, Compare):
#		valid_type = INT
#		typ1 = type_check(ast.expr, variables)
#		typ2 = type_check(ast.ops[0][1], variables)
#		if typ1 == typ2 or typ1 == FUNCRET or typ2 == FUNCRET:
#			return BOOL
#	elif isinstance(ast, UnarySub):
#		valid_type = INT
#		received_types.append(type_check(ast.expr, variables))
#		ret = INT
#	elif isinstance(ast, Not):
#		valid_type = BOOL
#		received_types.append(type_check(ast.expr, variables))
#		ret = BOOL
#	elif isinstance(ast, CallFunc):
#		for i in ast.args:
#			type_check(i, variables)
#		return FUNCRET
#	elif isinstance(ast, List):
#		valid_type = PYOBJ
#		received_types.extend(type_check(i, variables) for i in ast.nodes)
#		ret = PYOBJ
#	elif isinstance(ast, Dict):
#		valid_type = PYOBJ
#		for i in ast.items:
#			received_types.extend((type_check(i[0], variables),
#			                      type_check(i[1], variables)))
#		ret = PYOBJ
#	elif isinstance(ast, IfExp):
#		typ = type_check(ast.test, variables)
#		if typ != BOOL:
#			raise Exception(f"Type mis-match:{str(ast)}, {str(typ)}, {str(BOOL)}")
#		typ1 = type_check(ast.then, variables)
#		typ2 = type_check(ast.else_, variables)
#		if typ1 == typ2 or typ1 != FUNCRET and typ2 == FUNCRET:
#			return typ1
#		elif typ1 == FUNCRET:
#			return typ2
#		else:
#			raise Exception(f"Type mis-match returns:{str(ast)}, {str(typ1)}, {str(typ2)}")
#	elif isinstance(ast, Let):
#		typ = type_check(ast.rhs, variables)
#		received_types.append(typ)
#		variables[ast.var.name] = typ
#		return type_check(ast.body, variables)
#	elif isinstance(ast, InjectFrom):
#		valid_type = ast.typ.value
#		received_types.append(type_check(ast.arg, variables))
#		ret = PYOBJ
#	elif isinstance(ast, ProjectTo):
#		valid_type = PYOBJ
#		received_types.append(type_check(ast.arg, variables))
#		ret = ast.typ.value
#	elif isinstance(ast, GetTag):
#		valid_type = PYOBJ
#		received_types.append(type_check(ast.arg, variables))
#		ret = INT
#	else:
#		raise Exception(f"No AST match: {str(ast)}")
#
#	for i in received_types:
#		if i not in [valid_type, FUNCRET]:
#			raise Exception(f"Type mis-match:{str(ast)}, {str(i)}, {str(valid_type)}")
#	return ret
