import compiler
from compiler.ast import *

from dataTypes import *

class VariableTracking():
	names = []
	def get_name(self, name = None):
		if name is None:
			VariableTracking.names.append(str("temp"+str(len(VariableTracking.names))))
			return "temp"+str(len(VariableTracking.names))
		else:
			if name not in VariableTracking.names:
				VariableTracking.names.append(str(name))
			return str(name)

	def data():
		return VariableTracking.names

	def count():
		return len(VariableTracking.names)

#  recursively breaking complex expression into simple expressions, pass in
# ast object and simple expression linked list, pass up simple expression linked
# list only.
def recursive_flatten(ast, expression_list, VT):

	if isinstance(ast, Module):
		return recursive_flatten(ast.node, expression_list, VT)

	elif isinstance(ast, Stmt):
		for node in ast.nodes:
			recursive_flatten(node, expression_list, VT)
		# recursive_flatten(x, expression_list, VT) for x in ast.nodes
		prev_expression = get_last(expression_list)
		current_expression = SimpleExpression("EndList", None, None, None,  \
		    prev_expression, None)
		prev_expression.next = current_expression
		return SimpleExpression("EndList", None, None, None, None, None)

	elif isinstance(ast, Assign):
		# print 'Assign : [{0}]'.format(ast)
		input1 = recursive_flatten(ast.expr, expression_list, VT)
		#assigning INPUT type - have to go back and get it
		if input1.output == None:
			prev_expression = get_last(expression_list)
			# print "Assign previous = type [{0}]\ninput1 [{1}]\ninput2 [{2}]\noutput [{3}]\n".format(prev_expression.type, prev_expression.input1, prev_expression.input2, prev_expression.output)
			input1 = prev_expression.input1
		else:
			input1 = input1.output

		# print 'input1 : [{0}]'.format(ast)
		output = recursive_flatten(ast.nodes[0], expression_list, VT)
		# print 'ouput : [{0}]'.format(output.input1)
		prev_expression = get_last(expression_list)
		current_expression = SimpleExpression("Assign", output.input1 , None, \
    		input1, prev_expression, None)
		prev_expression.next = current_expression
		return current_expression

	elif isinstance(ast, AssName):
		# print 'AssName : [{0}]'.format(ast)
		prev_expression = get_last(expression_list)
		current_expression = SimpleExpression("AssName", ast.name, None, prev_expression.input1,  \
		    prev_expression, None)
		prev_expression.next = current_expression
		return current_expression

	elif isinstance(ast, Discard):
		prev_expression = get_last(expression_list)
		current_expression = SimpleExpression("Discard", ast.name, None, None,  \
		    prev_expression, None)
		prev_expression.next = current_expression
		return current_expression


	elif isinstance(ast, Const):
		prev_expression = get_last(expression_list)
		current_expression = SimpleExpression("Const", VT.get_name(), None, ast.value, \
		    prev_expression, None)
		prev_expression.next = current_expression
		return current_expression

	elif isinstance(ast, Name):
		# print 'Name : [{0}]'.format(ast)
		prev_expression = get_last(expression_list)
		current_expression = SimpleExpression("Name", VT.get_name(ast.name), None, None, \
		    prev_expression, None)

		prev_expression.next = current_expression
		return current_expression

	elif isinstance(ast, Printnl):
		print_statement = recursive_flatten(ast.nodes[0], expression_list, VT)
		# print "Print statment = type [{0}]\ninput1 [{1}]\ninput2 [{2}]\noutput [{3}]\n".format(print_statement.type, print_statement.input1, print_statement.input2, print_statement.output)
		prev_expression = print_statement
		current_expression = SimpleExpression("Print", print_statement.output if print_statement.output != None else print_statement.input1, None, None, prev_expression, None)
		prev_expression.next = current_expression
		return current_expression

	elif isinstance(ast, Add):

		# print 'Add : [{0}]'.format(ast)

		left_add = recursive_flatten(ast.left, expression_list, VT)
		if left_add == None:
			left_add = get_last(expression_list)

		# print 'left [{0}]'.format(left_add.type)

		right_add = recursive_flatten(ast.right, expression_list, VT)
		if right_add == None:
			right_add = get_last(expression_list)
		# print 'right [{0}]'.format(right_add.type)

		prev_expression = get_last(expression_list)
		current_expression = SimpleExpression("Add", left_add.output if left_add.type == 'Add' or left_add.type == 'UnarySub' else left_add.input1, right_add.output if right_add.type == 'Add' or right_add.type == 'UnarySub'  else right_add.input1, \
		    VT.get_name(), prev_expression, None)
		prev_expression.next = current_expression

		return current_expression

	elif isinstance(ast, UnarySub):
		# print 'UnarySub : [{0}]'.format(ast)
		negate = recursive_flatten(ast.expr, expression_list, VT)
		prev_expression = get_last(expression_list)
		current_expression = SimpleExpression("UnarySub", negate.input1, None, \
		     VT.get_name(), prev_expression, None)
		prev_expression.next = current_expression
		return current_expression

	elif isinstance(ast, CallFunc):
		# print 'CallFunc : [{0}]'.format(ast)
		if ast.node.name == 'input':
			prev_expression = get_last(expression_list)
			current_expression = SimpleExpression("Input", VT.get_name(), None, \
			    None, prev_expression, None)
			prev_expression.next = current_expression
		return current_expression

	else:
		raise Exception('Error: unrecognized AST node')

#flatten by breaking into series of assignment statements
def flatten_expression(ast):
	VT = VariableTracking()
	expression_list = SimpleExpression("StartList", None, None, None, None, None)
	recursive_flatten(ast, expression_list, VT)
	return expression_list
