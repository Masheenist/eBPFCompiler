import sys
import compiler
from compiler.ast import *

import dataTypes

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
	with open(fileNameToWriteTo,"w") as s_file:
		#write to file
		for line in lines:
			s_file.write(line)


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
		elif variableLocations.has_key(dataTypes.get_value(nodeSupplied, nodeSupplied.input1)):
			left_side = variableLocations[dataTypes.get_value(nodeSupplied, nodeSupplied.input1)]
		elif isinstance(dataTypes.get_value(nodeSupplied, nodeSupplied.input1), int):
			left_side = '$' + str(dataTypes.get_value(nodeSupplied, nodeSupplied.input1))
		else:
			left_side = variableLocations[dataTypes.get_value(nodeSupplied, nodeSupplied.input1)]

		if variableLocations.has_key(nodeSupplied.input2):
			right_side = variableLocations[nodeSupplied.input2]
		elif variableLocations.has_key(dataTypes.get_value(nodeSupplied, nodeSupplied.input2)):
			right_side = variableLocations[dataTypes.get_value(nodeSupplied, nodeSupplied.input2)]
		elif isinstance(dataTypes.get_value(nodeSupplied, nodeSupplied.input2), int):
			right_side = '$' + str(dataTypes.get_value(nodeSupplied, nodeSupplied.input2))
		else:
			right_side = variableLocations[dataTypes.get_value(nodeSupplied, nodeSupplied.input2)]


		# left_side = variableLocations[nodeSupplied.input1] if variableLocations.has_key(nodeSupplied.input1) else '$' + str(get_value(nodeSupplied, nodeSupplied.input1))
		# right_side = variableLocations[nodeSupplied.input2] if variableLocations.has_key(nodeSupplied.input2) else '$' + str(get_value(nodeSupplied, nodeSupplied.input2))
		start_stack_allocation += 4
		stack_offset += 4
		variableLocations[nodeSupplied.output] = "-{0}(%ebp)".format(stack_offset)
		returnValue = "\tmovl {0}, %eax\n\taddl {1}, %eax\n\tmovl %eax, -{2}(%ebp)\n".format(left_side, right_side, stack_offset)
				# valueDictionary.update(nodeSupplied.output, returnValue)
				# valueDictionary[nodeSupplied.output] = returnValue

	elif nodeSupplied.type == "Print":

		if variableLocations.has_key(dataTypes.get_value(nodeSupplied, nodeSupplied.input1)):
			statement = variableLocations[dataTypes.get_value(nodeSupplied, nodeSupplied.input1)]
		elif variableLocations.has_key(nodeSupplied.input1):
			statement = variableLocations[nodeSupplied.input1]
		elif isinstance(dataTypes.get_value(nodeSupplied, nodeSupplied.input1), int):
			statement = '$' + str(dataTypes.get_value(nodeSupplied, nodeSupplied.input1))
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
		elif isinstance(dataTypes.get_value(nodeSupplied, nodeSupplied.input1), int):
			returnValue = "\tmovl ${0}, %eax\n".format(dataTypes.get_value(nodeSupplied, nodeSupplied.input1))
		returnValue += "\tnegl %eax\n\tmovl %eax, {0}\n".format(variableLocations[nodeSupplied.output] if variableLocations.has_key(nodeSupplied.output) else '$' + str(dataTypes.get_value(nodeSupplied, nodeSupplied.output)))

	elif nodeSupplied.type == "EndList":
		returnValue = "\taddl ${0}, %esp\n\tmovl $0, %eax\n\tleave\n\tret\n".format(stack_offset)

	return returnValue, stack_offset, start_stack_allocation
