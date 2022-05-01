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
# import compiler
# from compiler.ast import *

# SimpleExpression Node Guide :
  # NODE TYPE : Module
  # 	*can ignore
  # NODE TYPE : Stmt
  # 	*will mark BEGINNING and END
  # 	of statement (where end of link
  # 	list is inserted.)
  # NODE TYPE : Assign
  # 	*input1 = name
  # 	*output = value
  # NODE TYPE : AssName
  # 	*input1 = name
  # NODE TYPE : Discard
  # 	*input1 = name
  # NODE TYPE : Const
  # 	*input1 = temp name
  # 	*output = value
  # NODE TYPE : Name
  # 	*input1 = name
  # NODE TYPE : Print
  # 	*input1 = name of variable to print
  # NODE TYPE : ADD
  # 	*input1 = left variable name
  # 	*input2 = right variable name
  # 	*ouput 	= new variable (holds sum)
  # NODE TYPE : UnarySub
  # 	*input1  = new variable to hold term
  # 	*output = negative term
  # NODE TYPE : CallFunc::Input
  # 	*input1 = new variable name to hold
  # 			  input value


# class which forms a doubly linked list of nodes, comprised of simple expressions
# formed from the input ast built from complex expression
class SimpleExpression():
	def __init__(self, type, input1, input2, output, prev, next):
		self.type   = type      # can be AST node type
		self.input1 = input1    # will be Name of Variable types (Such as AssName, etc..)
		self.input2 = input2
		self.output = output    # will hold Value of Variable type data
		self.prev   = prev
		self.next   = next

class VariableTracking():
	names = []
	def get_name(self, name = None):
		if name == None:
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


# return simple expression currently at the end of the linked list
def get_last(simple_expression):
	while simple_expression.prev != None:
		simple_expression = simple_expression.prev
	while simple_expression.next != None:
		simple_expression = simple_expression.next
	return simple_expression

def get_value(simple_expression, variable_name):
	returnValue = None
	negate = False
	while simple_expression.prev != None:
		simple_expression = simple_expression.prev
	while simple_expression != None:
		if simple_expression.type != "Add":
			if simple_expression.input1 == variable_name and simple_expression.output != None:
				returnValue = simple_expression.output
		simple_expression = simple_expression.next
	return returnValue

def print_expressions(simple_expression):
	while simple_expression.prev != None:
		simple_expression = simple_expression.prev
	count = 0

	print ('\nSimple Expression Linked List\n- - - - - - - -')

	print ('[count]\t[type]\t\t[input1]\t[input2]\t[output]')
	while simple_expression != None:
		if simple_expression.type == "StartList" :
			print ('[{0}]\t{1}\t{2}\t\t{3}\t\t{4}'.format(count, simple_expression.type, simple_expression.input1, simple_expression.input2, simple_expression.output))
		elif simple_expression.type == "UnarySub" :
			print ('[{0}]\t{1}\t{2}\t\t{3}\t\t{4}'.format(count, simple_expression.type, simple_expression.input1, simple_expression.input2, simple_expression.output))
		else:
			print ('[{0}]\t{1}\t\t{2}\t\t{3}\t\t{4}'.format(count, simple_expression.type, simple_expression.input1, simple_expression.input2, simple_expression.output))
		count += 1
		simple_expression = simple_expression.next
	print ('- - - - - - - -\n')
	return

# def parse(program):
# 	ast = parse(program)#compiler.parseFile(program)
# 	return ast

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

#translate txt file of ast nodes into assembly
	#traversing linked list SimpleExpression and writing to file
	#Function Defintion:
	# Name: traverse_list
	# Parameters:  instance of linkedList, type "SimpleExpression"
	#Operation:
	#1 - Visit each node on linked list
	#2 - Convert each node into assembly (string)
	#3 - Write each assembly string to the file, newline-terminated
	#4 - Save file

#creates the .s file and traverses the linked list
def traverse_list(linkListNodes, fileNameToWriteTo):
		stack_offset = 0
		start_stack_allocation = 0
		variableLocations = {}
		currentNode = linkListNodes
		lines = []

		#covert simple expression nodes to assembly strings
		while currentNode:
			currentNodeAssembly, stack_offset, start_stack_allocation = convertNodeToAssembly(currentNode, variableLocations, stack_offset, start_stack_allocation)
			lines.append(currentNodeAssembly)
			currentNode = currentNode.next

		# allocate space on stack, if needed
		if start_stack_allocation != 0:
			lines.insert(1, '\tsubl ${0}, %esp\n'.format(start_stack_allocation))
		s_file = open(fileNameToWriteTo,"w")

		#write to file
		for line in lines:
			s_file.write(line)
		s_file.close()

#takes the node type and converts to appropriate assembly
def convertNodeToAssembly(nodeSupplied, variableLocations, stack_offset, start_stack_allocation):
	returnValue = ""

	# print 'Variable locations : [{0}]'.format(variableLocations)

	if nodeSupplied.type == "StartList": # done
		returnValue = ".globl main\nmain:\n\tpushl %ebp\n\tmovl %esp, %ebp\n"


	elif nodeSupplied.type == "Input": # done
		start_stack_allocation += 4
		stack_offset += 4
		variableLocations[nodeSupplied.input1] = "-{0}(%ebp)".format(stack_offset)
		returnValue = "\tcall input\n\tmovl %eax, {0}\n".format(variableLocations[nodeSupplied.input1])


	elif nodeSupplied.type == "Const":
		returnValue = "\tmovl ${0}, %eax\n".format(nodeSupplied.output)


	elif nodeSupplied.type == "Assign":
		start_stack_allocation += 4
		stack_offset += 4
		variableLocations[nodeSupplied.input1] = "-{0}(%ebp)".format(stack_offset)

		# first case, we are given a constant value and its location
		if isinstance(nodeSupplied.output, int):
			returnValue = "\tmovl ${0}, {1}\n".format(str(nodeSupplied.output), variableLocations[nodeSupplied.input1])
			const = '$' + str(get_value(nodeSupplied, nodeSupplied.input1))
		#second case, we are give a location on the stack only
		else:
			returnValue = "\tmovl {0}, %eax\n\tmovl %eax, {1}\n".format(variableLocations[nodeSupplied.output], variableLocations[nodeSupplied.input1])


	elif nodeSupplied.type == "Add":
		#firt case, variable is location on stack, second case it is a constant. So check location dict, else grab value.
		if variableLocations.has_key(nodeSupplied.input1):
			left_side = variableLocations[nodeSupplied.input1]
		elif variableLocations.has_key(get_value(nodeSupplied, nodeSupplied.input1)):
			left_side = variableLocations[get_value(nodeSupplied, nodeSupplied.input1)]
		else:
			if isinstance(get_value(nodeSupplied, nodeSupplied.input1), int):
				left_side = '$' + str(get_value(nodeSupplied, nodeSupplied.input1))
			else:
				left_side = variableLocations[get_value(nodeSupplied, nodeSupplied.input1)]

		if variableLocations.has_key(nodeSupplied.input2):
			right_side = variableLocations[nodeSupplied.input2]
		elif variableLocations.has_key(get_value(nodeSupplied, nodeSupplied.input2)):
			right_side = variableLocations[get_value(nodeSupplied, nodeSupplied.input2)]
		else:
			if isinstance(get_value(nodeSupplied, nodeSupplied.input2), int):
				right_side = '$' + str(get_value(nodeSupplied, nodeSupplied.input2))
			else:
				right_side = variableLocations[get_value(nodeSupplied, nodeSupplied.input2)]



		start_stack_allocation += 4
		stack_offset += 4
		variableLocations[nodeSupplied.output] = "-{0}(%ebp)".format(stack_offset)
		returnValue = "\tmovl {0}, %eax\n\taddl {1}, %eax\n\tmovl %eax, -{2}(%ebp)\n".format(left_side, right_side, stack_offset)

	elif nodeSupplied.type == "Print":

		if variableLocations.has_key(get_value(nodeSupplied, nodeSupplied.input1)):
			statement = variableLocations[get_value(nodeSupplied, nodeSupplied.input1)]
		elif variableLocations.has_key(nodeSupplied.input1):
			statement = variableLocations[nodeSupplied.input1]
		else:
			if isinstance(get_value(nodeSupplied, nodeSupplied.input1), int):
				statement = '$' + str(get_value(nodeSupplied, nodeSupplied.input1))
			elif isinstance(nodeSupplied.input1, int):
				statement = '$' + str(nodeSupplied.input1)

		returnValue = "\tmovl {0}, %eax\n\tpushl %eax\n\tcall print_int_nl\n".format(statement)
		stack_offset -= 4

	elif nodeSupplied.type == "UnarySub":
		start_stack_allocation += 4
		stack_offset += 4
		variableLocations[nodeSupplied.output] = "-{0}(%ebp)".format(stack_offset)
		if variableLocations.has_key(nodeSupplied.input1):
			 returnValue = "\tmovl {0}, %eax\n".format(variableLocations[nodeSupplied.input1])
		elif isinstance(get_value(nodeSupplied, nodeSupplied.input1), int):
			returnValue = "\tmovl ${0}, %eax\n".format(get_value(nodeSupplied, nodeSupplied.input1))
		returnValue += "\tnegl %eax\n\tmovl %eax, {0}\n".format(variableLocations[nodeSupplied.output] if variableLocations.has_key(nodeSupplied.output) else '$' + str(get_value(nodeSupplied, nodeSupplied.output)))

	elif nodeSupplied.type == "EndList":
		returnValue = "\taddl ${0}, %esp\n\tmovl $0, %eax\n\tleave\n\tret\n".format(stack_offset)

	return returnValue, stack_offset, start_stack_allocation




def main():
	with open(sys.argv[1], "r") as program_file:
		file_text = program_file.read()
		print('\nTest File [{1}]\n- - - - - - - -\n{0}- - - - - - - -'.format(file_text, sys.argv[1]))
		ast = parse(file_text)#compiler.parse(file_text)
		print(dump(ast))
	# print '\nAST\n- - - - - - - -\n{0}\n- - - - - - - -'.format(ast)
	first_expression = flatten_expression(ast)
	print_expressions(first_expression)
	traverse_list(first_expression, sys.argv[1].replace(".py",".s"))

main()
