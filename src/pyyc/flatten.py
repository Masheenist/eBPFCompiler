import compiler
from compiler.ast import *
from dataTypes import *
from NewDataTypes import *

def add_variable(variable_list, name):
	if name != None:
		for i in variable_list:
			if name == variable_list[i]:
				return i
	ret = Variable(str(len(variable_list)))
	variable_list[ret] = name
	return ret

def flatten_recursive(ast, variable_list):
	if isinstance(ast, Lambda):
		new_args = []
		for var in ast.argnames:
			new_args.append(add_variable(variable_list, var))
		first = flatten_recursive(ast.code, variable_list)
		last = get_last(first)
		if last != None:
			last.next = SimpleExpression("FunctionEnd", None, last, None, None, None)
			return SimpleExpression("FunctionStart", first, None, new_args, None, None)
		return SimpleExpression("FunctionStart", SimpleExpression("FunctionEnd", None, None, None, None, None), None, new_args, None, None)
	elif isinstance(ast, Stmt):
		first = None
		last = None
		for statement in ast.nodes:
			result = flatten_recursive(statement, variable_list)
			if result != None:
				if first == None:
					first = result
					last = get_last(first)
				else:
					if isinstance(result, tuple):
						print str(result[0])
					last.next = result
					result.prev = last
					last = get_last(last)
		return first
	elif isinstance(ast, Assign):
		result = flatten_recursive(ast.expr, variable_list)
		output = flatten_recursive(ast.nodes[0], variable_list)
		if result[0] == None:
			first = SimpleExpression("Assign", None, None, output, result[1], None)
		else:
			first = result[0]
			last = get_last(first)
			node = SimpleExpression("Assign", None, last, output, result[1], None)
			last.next = node
		return first
	elif isinstance(ast, AssName):
		return add_variable(variable_list, ast.name)
	elif isinstance(ast, Discard):
		return flatten_recursive(ast.expr, variable_list)[0]
	elif isinstance(ast, Const):
		return None, ast.value
	elif isinstance(ast, String):
		return None, ast.value
	elif isinstance(ast, Bool):
		return None, ast.value
	elif isinstance(ast, Name):
		return None, add_variable(variable_list, ast.name)
	elif isinstance(ast, Add):
		leftTuple = flatten_recursive(ast.left, variable_list)
		left = leftTuple[0]
		rightTuple = flatten_recursive(ast.right, variable_list)
		right = rightTuple[0]
		first = None
		output = add_variable(variable_list, None)
		if left != None:
			first = left
			last = get_last(left)
		if right != None:
			if first == None:
				first = right
			else:
				right.prev = last
				last.next = right
			last = get_last(right)
		if first == None:
			first = SimpleExpression("Add", None, None, output, leftTuple[1], rightTuple[1])
		else:
			last.next = SimpleExpression("Add", None, last, output, leftTuple[1], rightTuple[1])
		return (first, output)

	elif isinstance(ast, Or):
		leftTuple = flatten_recursive(ast.left, variable_list)
		left = leftTuple[0]
		rightTuple = flatten_recursive(ast.right, variable_list)
		right = rightTuple[0]
		first = None
		output = add_variable(variable_list, None)
		if left != None:
			first = left
			last = get_last(left)
		if right != None:
			if first == None:
				first = right
			else:
				right.prev = last
				last.next = right
			last = get_last(right)
		if first == None:
			first = SimpleExpression("Or", None, None, output, leftTuple[1], rightTuple[1])
		else:
			last.next = SimpleExpression("Or", None, last, output, leftTuple[1], rightTuple[1])
		return (first, output)

	elif isinstance(ast, Compare):
		leftTuple = flatten_recursive(ast.expr, variable_list)
		left = leftTuple[0]
		rightTuple = flatten_recursive(ast.ops[0][1], variable_list)
		right = rightTuple[0]
		first = None
		output = add_variable(variable_list, None)
		if left != None:
			first = left
			last = get_last(left)
		if right != None:
			if first == None:
				first = right
			else:
				right.prev = last
				last.next = right
			last = get_last(right)

		instruction = "Compare"
		if ast.ops[0][0] == "!=":
			instruction = "CompareNE"
		elif ast.ops[0][0] == "==":
			instruction = "CompareEQ"
		elif ast.ops[0][0] == ">=":
			instruction = "CompareGE"
		elif ast.ops[0][0] == ">":
			instruction = "CompareGT"
		elif ast.ops[0][0] == "<=":
			instruction = "CompareLE"
		elif ast.ops[0][0] == "<":
			instruction = "CompareLT"
		if first == None:
			first = SimpleExpression(instruction, None, None, output, leftTuple[1], rightTuple[1])
		else:
			last.next = SimpleExpression(instruction, None, last, output, leftTuple[1], rightTuple[1])
		return (first, output)
	elif isinstance(ast, UnarySub):
		result = flatten_recursive(ast.expr, variable_list)
		output = add_variable(variable_list, None)
		if result[0] == None:
			first = SimpleExpression("Neg", None, None, output, result[1], None)
		else:
			first = result[0]
			last = get_last(first)
			node = SimpleExpression("Neg", None, last, output, result[1], None)
			last.next = node
		return first, output
	elif isinstance(ast, Not):
		result = flatten_recursive(ast.expr, variable_list)
		output = add_variable(variable_list, None)
		if result[0] == None:
			first = SimpleExpression("Not", None, None, output, result[1], None)
		else:
			first = result[0]
			last = get_last(first)
			node = SimpleExpression("Not", None, last, output, result[1], None)
			last.next = node
		return first, output
	elif isinstance(ast, Return):
		result = flatten_recursive(ast.value, variable_list)
		output = add_variable(variable_list, None)
		if result[0] == None:
			first = SimpleExpression("Return", None, None, None, result[1], None)
		else:
			first = result[0]
			last = get_last(first)
			node = SimpleExpression("Return", None, last, None, result[1], None)
			last.next = node
		return first
	elif isinstance(ast, CallFunc):
		varsList = []
		first = None
		result = flatten_recursive(ast.node, variable_list)
		func = result[1]
		if result[0] != None:
			if first == None:
				first = result[0]
		for arg in ast.args:
			result = flatten_recursive(arg, variable_list)
			varsList.append(result[1])
			if result[0] != None:
				if first == None:
					first = result[0]
				else:
					last = get_last(first)
					last.next = result[0]
					result[0].prev = last
		output = add_variable(variable_list, None)
		funcNode = SimpleExpression("CallFunc", None, None, output, func, varsList)
		if first == None:
			first = funcNode
		else:
			last = get_last(first)
			last.next = funcNode
			funcNode.prev = last
		return first, output
	elif isinstance(ast, IfExp):
		result0 = flatten_recursive(ast.test, variable_list)
		result1 = flatten_recursive(ast.then, variable_list)
		result2 = flatten_recursive(ast.else_, variable_list)
		first = result0[0]
		last = get_last(first)
		output = add_variable(variable_list, None)
		ifNode = SimpleExpression("IfExp", None, last, output, result0[1], None)
		if first == None:
			first = ifNode
		else:
			last.next = ifNode
		first1 = result1[0]
		first2 = result2[0]
		last1 = get_last(first1)
		last2 = get_last(first2)
		if first1 != None:
			last1.next = SimpleExpression("Assign", None, last1, output, result1[1], None)
		else:
			first1 = SimpleExpression("Assign", None, None, output, result1[1], None)
		if first2 != None:
			last2.next = SimpleExpression("Assign", None, last2, output, result2[1], None)
		else:
			first2 = SimpleExpression("Assign", None, None, output, result2[1], None)
		ifNode.thenNext = first1
		first1.prev = ifNode
		ifNode.elseNext = first2
		first2.prev = ifNode
		return first, output
	elif isinstance(ast, If):
		result0 = flatten_recursive(ast.tests[0][0], variable_list)
		result1 = flatten_recursive(ast.tests[0][1], variable_list)
		result2 = flatten_recursive(ast.else_, variable_list)
		first = result0[0]
		last = get_last(first)
		ifNode = SimpleExpression("IfExp", None, last, None, result0[1], None)
		if first == None:
			first = ifNode
		else:
			last.next = ifNode
		ifNode.thenNext = result1
		result1.prev = ifNode
		ifNode.elseNext = result2
		result2.prev = ifNode
		return first
	elif isinstance(ast, While):
		result0 = flatten_recursive(ast.test, variable_list)
		result1 = flatten_recursive(ast.body, variable_list)
		whileNode = SimpleExpression("While", None, None, None, result0[1], None)
		whileNode.thenNext = result1
		result1.prev = whileNode
		whileNode.elseNext = result0[0]
		result0[0].prev = whileNode
		return whileNode
	elif isinstance(ast, GetTag):
		result = flatten_recursive(ast.arg, variable_list)
		output = add_variable(variable_list, None)
		if result[0] == None:
			first = SimpleExpression("GetTag", None, None, output, result[1], None)
		else:
			first = result[0]
			last = get_last(first)
			node = SimpleExpression("GetTag", None, last, output, result[1], None)
			last.next = node
		return first, output
	elif isinstance(ast, ProjectTo):
		result = flatten_recursive(ast.arg, variable_list)
		output = add_variable(variable_list, None)
		if result[0] == None:
			first = SimpleExpression("ProjectTo", None, None, output, result[1], ast.typ.value)
		else:
			first = result[0]
			last = get_last(first)
			node = SimpleExpression("ProjectTo", None, last, output, result[1], ast.typ.value)
			last.next = node
		return first, output
	elif isinstance(ast, InjectFrom):
		result = flatten_recursive(ast.arg, variable_list)
		output = add_variable(variable_list, None)
		if result[0] == None:
			first = SimpleExpression("InjectFrom", None, None, output, result[1], ast.typ.value)
		else:
			first = result[0]
			last = get_last(first)
			node = SimpleExpression("InjectFrom", None, last, output, result[1], ast.typ.value)
			last.next = node
		return first, output
	elif isinstance(ast, Let):
		output = add_variable(variable_list, ast.var.name)
		result1 = flatten_recursive(ast.body, variable_list)
		result0 = flatten_recursive(ast.rhs, variable_list)
		first0 = result0[0]
		first1 = result1[0]
		last = get_last(first0)
		assignNode = SimpleExpression("Assign", first1, last, output, result0[1], None)
		if first0 != None:
			last.next = assignNode
		else:
			first0 = assignNode
		if first1 != None:
			first1.prev = assignNode
		return first0, result1[1]
	elif isinstance(ast, List):
		first = None
		listElem = []
		for node in ast.nodes:
			result = flatten_recursive(node, variable_list)
			listElem.append(result[1])
			if result[0] != None:
				if first == None:
					first = result[0]
				else:
					last = get_last(first)
					last.next = result[0]
					result[0].prev = last
		output = add_variable(variable_list, None)
		tmp = add_variable(variable_list, None)
		tmp2 = add_variable(variable_list, None)
		injectNode = SimpleExpression("InjectFrom", None, None, tmp, len(ast.nodes), 0)
		listNode = SimpleExpression("CallFunc", None, injectNode, tmp2, GlobalFuncName("create_list"), [tmp])
		injectNode2 = SimpleExpression("InjectFrom", None, listNode, output, tmp2, 3)
		injectNode.next = listNode
		listNode.next = injectNode2
		if first == None:
			first = injectNode
		else:
			last = get_last(first)
			last.next = injectNode
			injectNode.prev = last
		last = injectNode2
		for i in range(0, len(listElem)):
			tmp = add_variable(variable_list, None)
			last.next = SimpleExpression("InjectFrom", None, last, tmp, i, 0)
			last = last.next
			last.next = SimpleExpression("CallFunc", None, last, None, GlobalFuncName("set_subscript"), [output, tmp, listElem[i]])
			last = last.next
		return first, output
	elif isinstance(ast, Dict):
		first = None
		dictElem = {}
		for item in ast.items:

			result = flatten_recursive(item[1], variable_list)
			elem = result[1]
			if first == None:
				first = result[0]
			else:
				last = get_last(first)
				last.next = result[0]
				result[0].prev = last

			result = flatten_recursive(item[0], variable_list)
			dictElem[result[1]] = elem
			if first == None:
				first = result[0]
			else:
				last = get_last(first)
				last.next = result[0]
				result[0].prev = last
		output = add_variable(variable_list, None)
		tmp = add_variable(variable_list, None)
		dictNode = SimpleExpression("CallFunc", None, None, tmp, GlobalFuncName("create_dict"), [])
		injectNode = SimpleExpression("InjectFrom", None, dictNode, output, tmp, 3)
		dictNode.next = injectNode
		if first == None:
			first = dictNode
		else:
			last = get_last(first)
			last.next = dictNode
			dictNode.prev = last
		last = injectNode
		for key in dictElem:
			last.next = SimpleExpression("CallFunc", None, last, None, GlobalFuncName("set_subscript"), [output, key, dictElem[key]])
			last = last.next
		return first, output
	elif isinstance(ast, GlobalFuncName):
		return None, ast
	# elif isinstance(ast, Subscript):
	# 	tmp = add_variable(variable_list, None)
	# 	last.next = SimpleExpression("InjectFrom", None, last, tmp, i, 0)
	# 	last = last.next
	# 	last.next = SimpleExpression("CallFunc", None, last, None, GlobalFuncName("get_subscript"), [output, tmp])
	# 	last = last.next
	else:
		raise Exception("No AST match in flatten: " + str(ast))

def flatten(ast):
	variable_list = {}
	return (flatten_recursive(ast, variable_list), variable_list)

def add_instruction(prev, new_instruction):
	if prev != None:
		prev.next = new_instruction
	new_instruction.prev = prev
	return new_instruction

def assembly_link(first_expression, function):
	node = first_expression
	first = None
	last = None
	while node != None:
		if node.type == "FunctionStart":
			for i in range(0, len(node.output)):
				last = add_instruction(last, IRNode("movl", Stack(str(4*(2+i)) + "(%ebp)"), node.output[i]))
		elif node.type == "FunctionEnd":
			pass
		elif node.type == "Assign":
			last = add_instruction(last, IRNode("movl", node.input1, node.output))
		elif node.type == "Add":
			last = add_instruction(last, IRNode("movl", node.input1, node.output))
			last = add_instruction(last, IRNode("addl", node.input2, node.output))

		elif node.type == "And":
			last = add_instruction(last, IRNode("movl", node.input1, node.output))
			last = add_instruction(last, IRNode("andl", node.input2, node.output))

		elif node.type == "Or":
			last = add_instruction(last, IRNode("movl", node.input1, node.output))
			last = add_instruction(last, IRNode("orl", node.input2, node.output))

		elif node.type == "Neg":
			last = add_instruction(last, IRNode("movl", node.input1, node.output))
			last = add_instruction(last, IRNode("negl", node.output, None))
		elif node.type == "InjectFrom":
			last = add_instruction(last, IRNode("movl", node.input1, node.output))
			if node.input2 != 3:
				last = add_instruction(last, IRNode("sall", 2, node.output))
				last = add_instruction(last, IRNode("orl", node.input2, node.output))
			else:
				last = add_instruction(last, IRNode("addl", 3, node.output))
		elif node.type == "ProjectTo":
			last = add_instruction(last, IRNode("movl", node.input1, node.output))
			if node.input2 != 3:
				last = add_instruction(last, IRNode("sarl", 2, node.output))
			else:
				last = add_instruction(last, IRNode("andl", -4, node.output))
		elif node.type == "GetTag":
			last = add_instruction(last, IRNode("movl", node.input1, node.output))
			last = add_instruction(last, IRNode("andl", 3, node.output))
		elif node.type == "IfExp":
			last = add_instruction(last, IRNode("IfExp", node.input1, node.output))
			last.thenNext = assembly_link(node.thenNext, function)
			last.elseNext = assembly_link(node.elseNext, function)
		elif node.type == "While":
			last = add_instruction(last, IRNode("While", node.input1, node.output))
			last.elseNext = assembly_link(node.elseNext, function)
			last.thenNext = assembly_link(node.thenNext, function)
		elif node.type == "CompareEQ":
			if isinstance(node.input1, Variable):
				last = add_instruction(last, IRNode("cmpl", node.input2, node.input1))
			else:
				last = add_instruction(last, IRNode("cmpl", node.input1, node.input2))
			last = add_instruction(last, IRNode("sete", Variable("al"), None))
			last = add_instruction(last, IRNode("movzbl", Variable("al"), node.output))
		elif node.type == "CompareNE":
			last = add_instruction(last, IRNode("cmpl", node.input1, node.input2))
			last = add_instruction(last, IRNode("setne", Variable("al"), None))
			last = add_instruction(last, IRNode("movzbl", Variable("al"), node.output))
		elif node.type == "Not":
			last = add_instruction(last, IRNode("cmpl", 0, node.input1))
			last = add_instruction(last, IRNode("sete", Variable("al"), None))
			last = add_instruction(last, IRNode("movzbl", Variable("al"), node.output))
		elif node.type == "CallFunc":
			for var in reversed(node.input2):
				last = add_instruction(last, IRNode("pushl", var, None))
			last = add_instruction(last, IRNode("call", node.input1, None))
			if node.output != None:
				last = add_instruction(last, IRNode("movl", Variable("eax"), node.output))
			last = add_instruction(last, IRNode("addl", 4*len(node.input2), Stack("%esp")))
		elif node.type == "Return":
			last = add_instruction(last, IRNode("movl", node.input1, Variable("eax")))
			last = add_instruction(last, IRNode("jmp", function + "_end", None))
		else:
			raise Exception("No ast match in assembly link: " + str(node))
		node = node.next
	return get_first(last)

def add_label(labels, function):
	name = function + "_label_" + str(len(labels))
	labels.append(name)
	return name

def insert_into_list(first, second):
	if first != None:
		first.next = second
	if second != None:
		second.prev = first

def fix_ordering(flattened_assembly):
	current = flattened_assembly
	current.prev = None
	while True:
		n = current.next
		if n != None:
			n.prev = current
		else:
			break
		current = current.next

def flatten_if_statement(flattened_assembly, labels, function):
	current = flattened_assembly
	while current != None:
		if current.type == "IfExp":
			print current
			label_0 = add_label(labels, function)
			label_1 = add_label(labels, function)
			compare = IRNode("cmpl", 0, current.input1)
			insert_into_list(current.prev, compare)
			jump_0 = IRNode("je", label_0, None)
			insert_into_list(compare, jump_0)
			then_ = flatten_if_statement(current.thenNext, labels, function)
			insert_into_list(jump_0, then_)
			last = get_last(then_)
			jump_1 = IRNode("jmp", label_1, None)
			insert_into_list(last, jump_1)
			inst_label = IRNode(label_0 + ":", None, None)
			insert_into_list(jump_1, inst_label)
			else_ = flatten_if_statement(current.elseNext, labels, function)
			insert_into_list(inst_label, else_)
			last2 = get_last(else_)
			inst_label2 = IRNode(label_1 + ":", None, None)
			insert_into_list(last2,inst_label2)
			if current.next != None:
				insert_into_list(inst_label2,current.next)
		if current.type == "While":
			label_0 = add_label(labels, function)
			label_1 = add_label(labels, function)
			inst_label = IRNode(label_0 + ":", None, None)
			if current.prev == None:
				x86IR = inst_label
			else:
				insert_into_list(current.prev, inst_label)
			comp_res = flatten_if_statement(current.elseNext, labels, function)
			insert_into_list(inst_label, comp_res)
			last = get_last(comp_res)
			comp_node = IRNode("cmpl", 0, current.input1)
			insert_into_list(last, comp_node)
			jump1 = IRNode("je", label_1, None)
			insert_into_list(comp_node, jump1)
			loop = flatten_if_statement(current.thenNext, labels, function)
			insert_into_list(jump1,loop)
			last = get_last(loop)
			jump2 = IRNode("jmp", label_0, None)
			insert_into_list(last, jump2)
			inst_label2 = IRNode(label_1 + ":", None, None)
			insert_into_list(jump2, inst_label2)
			if current.next != None:
				insert_into_list(inst_label2, current.next)
		current = current.next
	return flattened_assembly