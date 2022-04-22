import dataTypes

def spillage(flattened_assembly, graph_nodes, variable_list):
	registers = ["%eax", "%ecx", "%edx", "%ebx", "%edi", "%esi"]
	current = flattened_assembly
	return_assembly = flattened_assembly
	spillage_list = []
	while current != None:
		if current.type in ["IfExp", "While"]:
			result = spillage(current.thenNext, graph_nodes, variable_list)
			current.thenNext = result[0]
			spillage_list.extend(result[1])
			result = spillage(current.elseNext, graph_nodes, variable_list)
			current.elseNext = result[0]
			spillage_list.extend(result[1])
		else:
			input1Stack = False
			input2Stack = False
			if isinstance(current.input1, dataTypes.Stack):
				input1Stack = True
			elif isinstance(current.input1, dataTypes.Variable):
				if not graph_nodes[current.input1.name].color in registers:
					input1Stack = True
			if isinstance(current.input2, dataTypes.Stack):
				input2Stack = True
			elif isinstance(current.input2, dataTypes.Variable):
				if not graph_nodes[current.input2.name].color in registers:
					input2Stack = True
			if input1Stack and input2Stack:
				new_var = dataTypes.add_variable(variable_list, None)
				new_instr = dataTypes.IRNode("movl", current.input1, new_var)
				new_instr.next = current
				new_instr.prev = current.prev
				current.input1 = new_var
				if current.prev != None:
					current.prev.next = new_instr
				else:
					return_assembly = new_instr
				current.prev = new_instr
				spillage_list.append(new_var)

		current = current.next

	return (return_assembly, spillage_list)