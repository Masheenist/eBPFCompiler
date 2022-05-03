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

def parseAST(ast, expression_list, VT):

    if isinstance(ast, Module):
        return recursive_flatten(ast.node, expression_list, VT)

    if isinstance(ast, Stmt):
        prev_expression = get_last(expression_list)
		current_expression = SimpleExpression("EndList", None, None, None,  \
		    prev_expression, None)
		prev_expression.next = current_expression
		return SimpleExpression("EndList", None, None, None, None, None)

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

#creates the .s file and traverses the linked list
def traverse_list(linkListNodes, fileNameToWriteTo):
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
	with open(fileNameToWriteTo,"w") as s_file:
		#write to file
		for line in lines:
			s_file.write(line)

def converter(nodeSupplied, variableLocations):
    returnValue = ""

    if nodeSupplied.type == "StartList": # done
		returnValue = "#include <stdio.h>\nint main() {"

    elif nodeSupplied.type == "Print":
        if variableLocations.has_key(dataTypes.get_value(nodeSupplied, nodeSupplied.input1)):
			statement = variableLocations[dataTypes.get_value(nodeSupplied, nodeSupplied.input1)]
		elif variableLocations.has_key(nodeSupplied.input1):
			statement = variableLocations[nodeSupplied.input1]
		elif isinstance(dataTypes.get_value(nodeSupplied, nodeSupplied.input1), int):
			statement = '$' + str(dataTypes.get_value(nodeSupplied, nodeSupplied.input1))
		elif isinstance(nodeSupplied.input1, int):
			statement = '$' + str(nodeSupplied.input1)

        returnValue = "\tprintf({0})"
    
    elif nodeSupplied.type == "Const":
        returnValue = "\t{0}".format(nodeSupplied.output)

def convertNodeToC(ast):
	VT = VariableTracking()
    expression_list = SimpleExpression("StartList", None, None, None, None, None)
    parseAST(ast, expression_list, VT)
	return (expression_list)