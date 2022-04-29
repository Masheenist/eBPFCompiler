import sys
import compiler
from compiler.ast import *

class StartNode:
    labeledType = StartNode
    def DoOption(self):
        returnValue = ".globl main\nmain:\n\tpushl %ebp\n\tmovl %esp, %ebp\n"

class InputNode:
    labeledType = Input
    def DoOption(self):
        start_stack_allocation += 4
	    stack_offset += 4
    	variableLocations[nodeSupplied.input1] = "-{0}(%ebp)".format(stack_offset)
		returnValue = "\tcall input\n\tmovl %eax, {0}\n".format(variableLocations[nodeSupplied.input1])

class ConstNode:
    labeledType = Const
    def DoOption(self):
        returnValue = "\tmovl ${0}, %eax\n".format(nodeSupplied.output)

class AssignNode:
    labeledType = Assign
    def DoOption(self):
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

class AddNode:
    labeledType = Add
    def DoOption(self):
        #first case, variable is location on stack, second case it is a constant. So check location dict, else grab value.
		# print 'true  if [{0}]'.format(left_side)
		if variableLocations.has_key(nodeSupplied.input1):
			left_side = variableLocations[nodeSupplied.input1]
		elif variableLocations.has_key(get_value(nodeSupplied, nodeSupplied.input1)):
			left_side = variableLocations[get_value(nodeSupplied, nodeSupplied.input1)]
		elif isinstance(get_value(nodeSupplied, nodeSupplied.input1), int):
			left_side = '$' + str(get_value(nodeSupplied, nodeSupplied.input1))
		else:
			left_side = variableLocations[get_value(nodeSupplied, nodeSupplied.input1)]

		if variableLocations.has_key(nodeSupplied.input2):
			right_side = variableLocations[nodeSupplied.input2]
		elif variableLocations.has_key(get_value(nodeSupplied, nodeSupplied.input2)):
			right_side = variableLocations[get_value(nodeSupplied, nodeSupplied.input2)]
		elif isinstance(get_value(nodeSupplied, nodeSupplied.input2), int):
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


class PrintNode:
    labeledType = Print
    def DoOption(self):
        if variableLocations.has_key(get_value(nodeSupplied, nodeSupplied.input1)):
			statement = variableLocations[get_value(nodeSupplied, nodeSupplied.input1)]
		elif variableLocations.has_key(nodeSupplied.input1):
			statement = variableLocations[nodeSupplied.input1]
		elif isinstance(get_value(nodeSupplied, nodeSupplied.input1), int):
			statement = '$' + str(get_value(nodeSupplied, nodeSupplied.input1))
		elif isinstance(nodeSupplied.input1, int):
			statement = '$' + str(nodeSupplied.input1)

		returnValue = "\tmovl {0}, %eax\n\tpushl %eax\n\tcall print_int_nl\n".format(statement)
		stack_offset -= 4

class UnarySubNode:
    labeledType = UnarySub
    
    def DoOption(self):

        start_stack_allocation += 4
		stack_offset += 4
		variableLocations[nodeSupplied.output] = "-{0}(%ebp)".format(stack_offset)

		if variableLocations.has_key(nodeSupplied.input1):
			 returnValue = "\tmovl {0}, %eax\n".format(variableLocations[nodeSupplied.input1])
		elif isinstance(get_value(nodeSupplied, nodeSupplied.input1), int):
			returnValue = "\tmovl ${0}, %eax\n".format(get_value(nodeSupplied, nodeSupplied.input1))
		returnValue += "\tnegl %eax\n\tmovl %eax, {0}\n".format(variableLocations[nodeSupplied.output] if variableLocations.has_key(nodeSupplied.output) else '$' + str(get_value(nodeSupplied, nodeSupplied.output)))

class EndNode:
    labeledType = EndList
    def DoOption(self):
        returnValue = "\taddl ${0}, %esp\n\tmovl $0, %eax\n\tleave\n\tret\n".format(stack_offset)

class ast_selector:

    def node_check(self, nodeSupplied, variableLocations, stack_offset, start_stack_allocation):
        eligible_nodes = [
            StartList(),
            Input(),
            Const(),
            Assign(),
            Add(),
            Print(),
            UnarySub(),
            EndList()
        ]

        returnValue = []

        for currentNode in ast_selector :
			if isinstance(ast, currentNode.labeledType):
				return currentNode.DoOption(received_types, ast, variables)

        return returnValue, stack_offset, start_stack_allocation



#takes the node type and converts to appropriate assembly
#def convertNodeToAssembly(nodeSupplied, variableLocations, stack_offset, start_stack_allocation):
#	returnValue = ""
#
#	# print 'Variable locations : [{0}]'.format(variableLocations)
#
#	if nodeSupplied.type == "StartList": # done
#		returnValue = ".globl main\nmain:\n\tpushl %ebp\n\tmovl %esp, %ebp\n"
#
#	elif nodeSupplied.type == "Input": # done
#		start_stack_allocation += 4
#		stack_offset += 4
#		variableLocations[nodeSupplied.input1] = "-{0}(%ebp)".format(stack_offset)
#		returnValue = "\tcall input\n\tmovl %eax, {0}\n".format(variableLocations[nodeSupplied.input1])
#
#	elif nodeSupplied.type == "Const":
#		returnValue = "\tmovl ${0}, %eax\n".format(nodeSupplied.output)
#
#	elif nodeSupplied.type == "Assign":
#		# print "type [{0}]\ninput1 [{1}]\ninput2 [{2}]\noutput [{3}]\n".format(nodeSupplied.type, nodeSupplied.input1, nodeSupplied.input2, nodeSupplied.output)
#		start_stack_allocation += 4
#		stack_offset += 4
#		variableLocations[nodeSupplied.input1] = "-{0}(%ebp)".format(stack_offset)
#
#		# first case, we are given a constant value and its location
#		if isinstance(nodeSupplied.output, int):
#			returnValue = "\tmovl ${0}, {1}\n".format(str(nodeSupplied.output), variableLocations[nodeSupplied.input1])
#			const = '$' + str(get_value(nodeSupplied, nodeSupplied.input1))
#		#second case, we are give a location on the stack only
#		else:
#			returnValue = "\tmovl {0}, %eax\n\tmovl %eax, {1}\n".format(variableLocations[nodeSupplied.output], variableLocations[nodeSupplied.input1])
#
#
#	elif nodeSupplied.type == "Add":
#		# print 'type [{0}] input1 [{1}] input2 [{2}] output [{3}]'.format(nodeSupplied.type, nodeSupplied.input1, nodeSupplied.input2, nodeSupplied.output)
#		#first case, variable is location on stack, second case it is a constant. So check location dict, else grab value.
#			# print 'true  if [{0}]'.format(left_side)
#		if variableLocations.has_key(nodeSupplied.input1):
#			left_side = variableLocations[nodeSupplied.input1]
#		elif variableLocations.has_key(get_value(nodeSupplied, nodeSupplied.input1)):
#			left_side = variableLocations[get_value(nodeSupplied, nodeSupplied.input1)]
#		elif isinstance(get_value(nodeSupplied, nodeSupplied.input1), int):
#			left_side = '$' + str(get_value(nodeSupplied, nodeSupplied.input1))
#		else:
#			left_side = variableLocations[get_value(nodeSupplied, nodeSupplied.input1)]
#
#		if variableLocations.has_key(nodeSupplied.input2):
#			right_side = variableLocations[nodeSupplied.input2]
#		elif variableLocations.has_key(get_value(nodeSupplied, nodeSupplied.input2)):
#			right_side = variableLocations[get_value(nodeSupplied, nodeSupplied.input2)]
#		elif isinstance(get_value(nodeSupplied, nodeSupplied.input2), int):
#			right_side = '$' + str(get_value(nodeSupplied, nodeSupplied.input2))
#		else:
#			right_side = variableLocations[get_value(nodeSupplied, nodeSupplied.input2)]
#
#
#		# left_side = variableLocations[nodeSupplied.input1] if variableLocations.has_key(nodeSupplied.input1) else '$' + str(get_value(nodeSupplied, nodeSupplied.input1))
#		# right_side = variableLocations[nodeSupplied.input2] if variableLocations.has_key(nodeSupplied.input2) else '$' + str(get_value(nodeSupplied, nodeSupplied.input2))
#		start_stack_allocation += 4
#		stack_offset += 4
#		variableLocations[nodeSupplied.output] = "-{0}(%ebp)".format(stack_offset)
#		returnValue = "\tmovl {0}, %eax\n\taddl {1}, %eax\n\tmovl %eax, -{2}(%ebp)\n".format(left_side, right_side, stack_offset)
#				# valueDictionary.update(nodeSupplied.output, returnValue)
#				# valueDictionary[nodeSupplied.output] = returnValue
#
#	elif nodeSupplied.type == "Print":
#
#		if variableLocations.has_key(get_value(nodeSupplied, nodeSupplied.input1)):
#			statement = variableLocations[get_value(nodeSupplied, nodeSupplied.input1)]
#		elif variableLocations.has_key(nodeSupplied.input1):
#			statement = variableLocations[nodeSupplied.input1]
#		elif isinstance(get_value(nodeSupplied, nodeSupplied.input1), int):
#			statement = '$' + str(get_value(nodeSupplied, nodeSupplied.input1))
#		elif isinstance(nodeSupplied.input1, int):
#			statement = '$' + str(nodeSupplied.input1)
#
#		returnValue = "\tmovl {0}, %eax\n\tpushl %eax\n\tcall print_int_nl\n".format(statement)
#		stack_offset -= 4
#
#	elif nodeSupplied.type == "UnarySub":
#		start_stack_allocation += 4
#		stack_offset += 4
#		variableLocations[nodeSupplied.output] = "-{0}(%ebp)".format(stack_offset)
#		if variableLocations.has_key(nodeSupplied.input1):
#			 returnValue = "\tmovl {0}, %eax\n".format(variableLocations[nodeSupplied.input1])
#		elif isinstance(get_value(nodeSupplied, nodeSupplied.input1), int):
#			returnValue = "\tmovl ${0}, %eax\n".format(get_value(nodeSupplied, nodeSupplied.input1))
#		returnValue += "\tnegl %eax\n\tmovl %eax, {0}\n".format(variableLocations[nodeSupplied.output] if variableLocations.has_key(nodeSupplied.output) else '$' + str(get_value(nodeSupplied, nodeSupplied.output)))
#
#	elif nodeSupplied.type == "EndList":
#		returnValue = "\taddl ${0}, %esp\n\tmovl $0, %eax\n\tleave\n\tret\n".format(stack_offset)
#
#	return returnValue, stack_offset, start_stack_allocation
#