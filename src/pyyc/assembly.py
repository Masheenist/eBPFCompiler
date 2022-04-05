import dataTypes

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


def write_assembly_file(output_file, flattened_assembly, graph_nodes, graph_colors):
	ebx = False
	edi = False
	esi = False
	for item in graph_nodes:
		if graph_nodes[item].color == "%ebx":
			ebx = True
		elif graph_nodes[item].color == "%edi":
			edi = True
		elif graph_nodes[item].color == "%esi":
			esi = True

	with open(output_file, "w") as output_filename:
		current = flattened_assembly
		output_filename.write(".globl main\nmain:\n\tpushl %ebp\n\tmovl %esp, %ebp\n")
		if ebx:
			output_filename.write("\tmovl %ebx, -" + str(graph_colors * 4) + "(%ebp)\n")
			graph_colors += 1
		if edi:
			output_filename.write("\tmovl %edi, -" + str(graph_colors * 4) + "(%ebp)\n")
			graph_colors += 1
		if esi:
			output_filename.write("\tmovl %esi, -" + str(graph_colors * 4) + "(%ebp)\n")
			graph_colors += 1
		output_filename.write("\tsubl $" + str(graph_colors * 4) + ", %esp\n")
		while current != None:
			if isinstance(current.input1, dataTypes.Variable) and isinstance(current.input2, dataTypes.Variable) and str(graph_nodes[current.input1.name].color) == str(graph_nodes[current.input2.name].color) and current.type == "movl":
				current = current.next
			else:
				output_filename.write("\t" + current.type + " ")
				if isinstance(current.input1, dataTypes.Variable):
					if current.input1.name == "al":
						output_filename.write("%al")
					else:
						output_filename.write(str(graph_nodes[current.input1.name].color))
				elif current.type in ["call", "jmp", "je"]:
					output_filename.write(str(current.input1))
				else:
					if current.input1 != None:
						if current.input1 == True:
							output_filename.write("$1")
						elif current.input1 == False:
							output_filename.write("$0")
						else:
							output_filename.write("$" + str(current.input1))
				if isinstance(current.input2, dataTypes.Variable):
					output_filename.write(", " + str(graph_nodes[current.input2.name].color))
				elif current.input2 != None:
					output_filename.write(", " + str(current.input2))
				output_filename.write("\n")
				current = current.next
		if esi:
			graph_colors -= 1
			output_filename.write("\tmovl -" + str(graph_colors * 4) + "(%ebp), %esi\n")
		if edi:
			graph_colors -= 1
			output_filename.write("\tmovl -" + str(graph_colors * 4) + "(%ebp), %edi\n")
		if ebx:
			graph_colors -= 1
			output_filename.write("\tmovl -" + str(graph_colors * 4) + "(%ebp), %ebx\n")
		output_filename.write("\tmovl $0, %eax\n\tleave\n\tret\n")
		output_filename.close()
