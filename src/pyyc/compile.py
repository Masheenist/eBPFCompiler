#Rhett Hanscom, Ange Ishimwe, Sylvia Llosa, and Pranav 

import sys
import os
import ast
import compiler
from compiler.ast import *

from dataTypes import *
import flatten


def parse(program):
	ast = compiler.parseFile(program)
	return ast

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
			#print(currentNode.type + "==>" + currentNode.next.type)
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
		# print "type [{0}]\ninput1 [{1}]\ninput2 [{2}]\noutput [{3}]\n".format(nodeSupplied.type, nodeSupplied.input1, nodeSupplied.input2, nodeSupplied.output)
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
		# print 'type [{0}] input1 [{1}] input2 [{2}] output [{3}]'.format(nodeSupplied.type, nodeSupplied.input1, nodeSupplied.input2, nodeSupplied.output)
		#firt case, variable is location on stack, second case it is a constant. So check location dict, else grab value.
			# print 'true  if [{0}]'.format(left_side)
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


		# left_side = variableLocations[nodeSupplied.input1] if variableLocations.has_key(nodeSupplied.input1) else '$' + str(get_value(nodeSupplied, nodeSupplied.input1))
		# right_side = variableLocations[nodeSupplied.input2] if variableLocations.has_key(nodeSupplied.input2) else '$' + str(get_value(nodeSupplied, nodeSupplied.input2))
		start_stack_allocation += 4
		stack_offset += 4
		variableLocations[nodeSupplied.output] = "-{0}(%ebp)".format(stack_offset)
		returnValue = "\tmovl {0}, %eax\n\taddl {1}, %eax\n\tmovl %eax, -{2}(%ebp)\n".format(left_side, right_side, stack_offset)
		# valueDictionary.update(nodeSupplied.output, returnValue)
		# valueDictionary[nodeSupplied.output] = returnValue

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
		ast = compiler.parse(file_text)
	# print '\nAST\n- - - - - - - -\n{0}\n- - - - - - - -'.format(ast)
	first_expression = flatten.flatten_expression(ast)
	print_expressions(first_expression)
	traverse_list(first_expression, sys.argv[1].replace(".py",".s"))

	# os.system('gcc -m32 -g {0} runtime/libpyyruntime.a -lm -o {1}'.format(sys.argv[1].replace(".py",".s"), sys.argv[1][:-3]))
	# os.system('cat {0} | {1} > {2}'.format(sys.argv[1].replace(".py",".in"), sys.argv[1][:-3], sys.argv[1]).replace(".py",".out"))
	#
	# print '\ninput: '
	# with open(sys.argv[1].replace(".py",".in")) as f:
	# 	contents = f.read()
	# 	print contents
	#
	# print '\noutput: '
	# with open(sys.argv[1].replace(".py",".out")) as f:
	# 	contents = f.read()
	# 	print contents
main()
# starting :
#     print - input() + 2
#
# final :
#     temp0 = input()
#     temp1 = - input()
#     temp2 = temp1 + 2
#     print temp2
