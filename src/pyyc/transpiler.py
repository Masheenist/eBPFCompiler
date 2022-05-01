#!/usr/bin/python
#P0 statement interpreter translates a .py into a .s
#Rhett Hanscom and Sylvia Llosa

# Rhett Notes:
 # *test3.py - too many Name type nodes possibly. Nodes 4 + 8 are the same in
 # the linked list, though this does reflect the number of Name() occurances
 # in the provided AST.

import sys
import os
from ast import *


# recursively breaking complex expression into simple expressions, pass in
# ast object and simple expression linked list, pass up simple expression linked
# list only.
def recursive_flatten(ast, expression_list, VT):

	if isinstance(ast, Module):
		return recursive_flatten(ast.body, expression_list, VT)

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




def print_python3_ast(ast, tabs=0):
	# if an assign is marked as ctx=Load() or Store() we are indifferent.

	if isinstance(ast, Module):
		# print every entry in module's body
		print("\t"*tabs + "Module(\n\tbody=[")
		for entry in ast.body:
			print_python3_ast(entry, tabs=2)
		print("\t]\n)")



	elif isinstance(ast, FunctionDef):
		# print every argument
		print("\t"*tabs + "FunctionDef(\n" + "\t"*(tabs+1) + "name=" + ast.name)
		print("\t"*(tabs+1) + "args=")
		print_python3_ast(ast.args, tabs=tabs+2)

		# print every entry in funcs's body
		print("\t"*(tabs+1) + "body=[")
		for entry in ast.body:
			print_python3_ast(entry, tabs=tabs+2)
		print("\t"*(tabs+1)+"],")

		# print decorator_list
		if len(ast.decorator_list) == 0:
			print("\t"*(tabs+1) + "decorator_list=[],")
		else:
			print("\t"*(tabs+1) + "decorator_list=[")
			for entry in ast.decorator_list:
				print_python3_ast(entry, tabs = tabs+2)
			print("\t"*(tabs+1) + "],")

		# print returns (I believe this is type stuff? not relevant though)
		if ast.returns:
			print("\t"*(tabs+1) + "returns=" + dump(ast.returns))
		else:
			print("\t"*(tabs+1) + "returns=None")

		print("\t"*tabs + ")")



	elif isinstance(ast, Assign):
		print ("\t"*tabs + "Assign(")

		# print targets
		if len(ast.targets) == 0:
			print("\t"*(tabs+1) + "targets=[]")
		else:
			print("\t"*(tabs+1) + "targets=[")
			for entry in ast.targets:
				print_python3_ast(entry, tabs = tabs+2)
			print("\t"*(tabs+1) + "],")

		# print value
		print("\t"*(tabs+1) + "value=")
		print_python3_ast(ast.value, tabs=tabs+2)

		print("\t"*tabs + ")")



	elif isinstance(ast, Expr):
		print ("\t"*tabs + "Expr(")

		# print value
		print("\t"*(tabs+1) + "value=")
		print_python3_ast(ast.value, tabs=tabs+2)

		print("\t"*tabs + ")")



	elif isinstance(ast, BinOp):
		print ("\t"*tabs + "BinOp(")

		# print left
		print("\t"*(tabs+1) + "left=")
		print_python3_ast(ast.left, tabs=tabs+2)
		
		# print op
		print("\t"*(tabs+1) + "op=" + dump(ast.op))
		
		# print right
		print("\t"*(tabs+1) + "right=")
		print_python3_ast(ast.right, tabs=tabs+2)

		print("\t"*tabs + ")")



	elif isinstance(ast, UnaryOp):
		print ("\t"*tabs + "UnaryOp(")
		
		# print op
		print("\t"*(tabs+1) + "op=" + dump(ast.op))
		
		# print operand
		print("\t"*(tabs+1) + "operand=")
		print_python3_ast(ast.operand, tabs=tabs+2)
		print("\t"*tabs + ")")



	elif isinstance(ast, Call):
		print("\t"*tabs + "Call(")

		# print args
		if len(ast.args) == 0:
			print("\t"*(tabs+1) + "args=[]")
		else:
			print("\t"*(tabs+1) + "args=[")
			for entry in ast.args:
				print_python3_ast(entry, tabs = tabs+2)
			print("\t"*(tabs+1) + "],")

		# print keywords
		if len(ast.keywords) == 0:
			print("\t"*(tabs+1) + "keywords=[]")
		else:
			print("\t"*(tabs+1) + "keywords=[")
			for entry in ast.keywords:
				print_python3_ast(entry, tabs = tabs+2)
			print("\t"*(tabs+1) + "]")

		print("\t"*tabs + ")")



	elif isinstance(ast, Name):
		# has id, and ctx (context, unimportant i think)
		print("\t"*tabs + dump(ast))

	

	elif isinstance(ast, arguments):
		print("\t"*tabs + "arguments(")

		# print args
		if len(ast.args) == 0:
			print("\t"*(tabs+1) + "args=[]")
		else:
			print("\t"*(tabs+1) + "args=[")
			for entry in ast.args:
				print_python3_ast(entry, tabs = tabs+2)
			print("\t"*(tabs+1) + "]")

		# print vararg
		if ast.vararg:
			print("\t"*(tabs+1) + "vararg=" + dump(ast.vararg))
		else:
			print("\t"*(tabs+1) + "vararg=None")

		# print kwonlyargs
		if len(ast.kwonlyargs) == 0:
			print("\t"*(tabs+1) + "kwonlyargs=[]")
		else:
			print("\t"*(tabs+1) + "kwonlyargs=[")
			for entry in ast.kwonlyargs:
				print_python3_ast(entry, tabs = tabs+2)
			print("\t"*(tabs+1) + "]")

		# print kw_defaults
		if len(ast.kw_defaults) == 0:
			print("\t"*(tabs+1) + "kw_defaults=[]")
		else:
			print("\t"*(tabs+1) + "kw_defaults=[")
			for entry in ast.kw_defaults:
				print_python3_ast(entry, tabs = tabs+2)
			print("\t"*(tabs+1) + "]")

		# print kwarg
		if ast.kwarg:
			print("\t"*(tabs+1) + "kwarg=" + dump(ast.kwarg))
		else:
			print("\t"*(tabs+1) + "kwarg=None")

		# print defaults
		if len(ast.defaults) == 0:
			print("\t"*(tabs+1) + "defaults=[]")
		else:
			print("\t"*(tabs+1) + "defaults=[")
			for entry in ast.defaults:
				print_python3_ast(entry, tabs = tabs+2)
			print("\t"*(tabs+1) + "]")



	elif isinstance(ast, Num):
		# just has n
		print("\t"*tabs + dump(ast))



	elif isinstance(ast, Str):
		# just has s
		print("\t"*tabs + dump(ast))
	


	elif isinstance(ast, arg):
		# has arg, and annotation (temporary hack if we can't figure out typing BUT if we bail on figuring out typing we need to at least do complicated types like [] {} and BPF maps)
		print("\t"*tabs + dump(ast))



	elif isinstance(ast, Return):
		# just has value
		print("\t"*tabs + dump(ast))



	else:
		print("UNCAUGHT TYPE " + str(type(ast).__name__))
		print("\t"*tabs + dump(ast))


def main():
	with open(sys.argv[1], "r") as program_file:
		file_text = program_file.read()
		print('\nTest File [{1}]\n- - - - - - - -\n{0}- - - - - - - -'.format(file_text, sys.argv[1]))
		ast = parse(file_text)#compiler.parse(file_text)
		print_python3_ast(ast)
		print()
		#print(dump(ast))
		#print()
	# print '\nAST\n- - - - - - - -\n{0}\n- - - - - - - -'.format(ast)
	first_expression = flatten_expression(ast)
	print_expressions(first_expression)
	traverse_list(first_expression, sys.argv[1].replace(".py",".s"))

main()
