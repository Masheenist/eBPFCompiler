import compiler
from compiler.ast import *
from dataTypes import *
from NewDataTypes import *

def add_variable(variables, name):
	if name != None:
		for i in variables:
			if name == variables[i]:
				return i
	ret = Variable(str(len(variables)))
	variables[ret] = name
	return ret

def flattenRecurs(ast, variables):
	if isinstance(ast, Lambda):
		new_args = []
		for var in ast.argnames:
			new_args.append(add_variable(variables, var))
		first = flattenRecurs(ast.code, variables)
		last = get_last(first)
		if last != None:
			last.next = SimpleExpression("FunctionEnd", None, last, None, None, None)
			return SimpleExpression("FunctionStart", first, None, new_args, None, None)
		return SimpleExpression("FunctionStart", SimpleExpression("FunctionEnd", None, None, None, None, None), None, new_args, None, None)
	elif isinstance(ast, Stmt):
		first = None
		last = None
		for statement in ast.nodes:
			result = flattenRecurs(statement, variables)
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
		result = flattenRecurs(ast.expr, variables)
		output = flattenRecurs(ast.nodes[0], variables)
		if result[0] == None:
			first = SimpleExpression("Assign", None, None, output, result[1], None)
		else:
			first = result[0]
			last = get_last(first)
			node = SimpleExpression("Assign", None, last, output, result[1], None)
			last.next = node
		return first
	elif isinstance(ast, AssName):
		return add_variable(variables, ast.name)
	elif isinstance(ast, Discard):
		return flattenRecurs(ast.expr, variables)[0]
	elif isinstance(ast, Const):
		return None, ast.value
	elif isinstance(ast, Bool):
		return None, ast.value
	elif isinstance(ast, Name):
		return None, add_variable(variables, ast.name)
	elif isinstance(ast, Add):
		leftTuple = flattenRecurs(ast.left, variables)
		left = leftTuple[0]
		rightTuple = flattenRecurs(ast.right, variables)
		right = rightTuple[0]
		first = None
		output = add_variable(variables, None)
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
	elif isinstance(ast, Compare):
		leftTuple = flattenRecurs(ast.expr, variables)
		left = leftTuple[0]
		rightTuple = flattenRecurs(ast.ops[0][1], variables)
		right = rightTuple[0]
		first = None
		output = add_variable(variables, None)
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
			instruction = "CompareNE"
		if first == None:
			first = SimpleExpression(instruction, None, None, output, leftTuple[1], rightTuple[1])
		else:
			last.next = SimpleExpression(instruction, None, last, output, leftTuple[1], rightTuple[1])
		return (first, output)
	elif isinstance(ast, UnarySub):
		result = flattenRecurs(ast.expr, variables)
		output = add_variable(variables, None)
		if result[0] == None:
			first = SimpleExpression("Neg", None, None, output, result[1], None)
		else:
			first = result[0]
			last = get_last(first)
			node = SimpleExpression("Neg", None, last, output, result[1], None)
			last.next = node
		return first, output
	elif isinstance(ast, Not):
		result = flattenRecurs(ast.expr, variables)
		output = add_variable(variables, None)
		if result[0] == None:
			first = SimpleExpression("Not", None, None, output, result[1], None)
		else:
			first = result[0]
			last = get_last(first)
			node = SimpleExpression("Not", None, last, output, result[1], None)
			last.next = node
		return first, output
	elif isinstance(ast, Return):
		result = flattenRecurs(ast.value, variables)
		output = add_variable(variables, None)
		if result[0] == None:
			first = SimpleExpression("Return", None, None, None, result[1], None)
		else:
			first = result[0]
			last = get_last(first)
			node = SimpleExpression("Return", None, last, None, result[1], None)
			last.next = node
		return first
	elif isinstance(ast, CallFunc): # TODO: ADD A CHECK FOR IF THIS IS A CALLFUNC TO create_closure, AS THAT HAS A SPECIAL PARAMETER OF TYPE FunctionLabel
		varsList = []
		first = None
		result = flattenRecurs(ast.node, variables)
		func = result[1]
		if result[0] != None:
			if first == None:
				first = result[0]
		for arg in ast.args:
			result = flattenRecurs(arg, variables)
			varsList.append(result[1])
			if result[0] != None:
				if first == None:
					first = result[0]
				else:
					last = get_last(first)
					last.next = result[0]
					result[0].prev = last
		output = add_variable(variables, None)
		funcNode = SimpleExpression("CallFunc", None, None, output, func, varsList)
		if first == None:
			first = funcNode
		else:
			last = get_last(first)
			last.next = funcNode
			funcNode.prev = last
		return first, output
	elif isinstance(ast, IfExp):
		result0 = flattenRecurs(ast.test, variables)
		result1 = flattenRecurs(ast.then, variables)
		result2 = flattenRecurs(ast.else_, variables)
		first = result0[0]
		last = get_last(first)
		output = add_variable(variables, None)
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
	elif isinstance(ast, GetTag):
		result = flattenRecurs(ast.arg, variables)
		output = add_variable(variables, None)
		if result[0] == None:
			first = SimpleExpression("GetTag", None, None, output, result[1], None)
		else:
			first = result[0]
			last = get_last(first)
			node = SimpleExpression("GetTag", None, last, output, result[1], None)
			last.next = node
		return first, output
	elif isinstance(ast, ProjectTo):
		result = flattenRecurs(ast.arg, variables)
		output = add_variable(variables, None)
		if result[0] == None:
			first = SimpleExpression("ProjectTo", None, None, output, result[1], ast.typ.value)
		else:
			first = result[0]
			last = get_last(first)
			node = SimpleExpression("ProjectTo", None, last, output, result[1], ast.typ.value)
			last.next = node
		return first, output
	elif isinstance(ast, InjectFrom):
		result = flattenRecurs(ast.arg, variables)
		output = add_variable(variables, None)
		if result[0] == None:
			first = SimpleExpression("InjectFrom", None, None, output, result[1], ast.typ.value)
		else:
			first = result[0]
			last = get_last(first)
			node = SimpleExpression("InjectFrom", None, last, output, result[1], ast.typ.value)
			last.next = node
		return first, output
	elif isinstance(ast, Let):
		output = add_variable(variables, ast.var.name)
		result1 = flattenRecurs(ast.body, variables)
		result0 = flattenRecurs(ast.rhs, variables)
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
			result = flattenRecurs(node, variables)
			listElem.append(result[1])
			if result[0] != None:
				if first == None:
					first = result[0]
				else:
					last = get_last(first)
					last.next = result[0]
					result[0].prev = last
		output = add_variable(variables, None)
		tmp = add_variable(variables, None)
		tmp2 = add_variable(variables, None)
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
			tmp = add_variable(variables, None)
			last.next = SimpleExpression("InjectFrom", None, last, tmp, i, 0)
			last = last.next
			last.next = SimpleExpression("CallFunc", None, last, None, GlobalFuncName("set_subscript"), [output, tmp, listElem[i]])
			last = last.next
		return first, output
	elif isinstance(ast, Dict):
		first = None
		dictElem = {}
		for item in ast.items:

			result = flattenRecurs(item[1], variables)
			elem = result[1]
			if first == None:
				first = result[0]
			else:
				last = get_last(first)
				last.next = result[0]
				result[0].prev = last

			result = flattenRecurs(item[0], variables)
			dictElem[result[1]] = elem
			if first == None:
				first = result[0]
			else:
				last = get_last(first)
				last.next = result[0]
				result[0].prev = last
		output = add_variable(variables, None)
		tmp = add_variable(variables, None)
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
	elif isinstance(ast, Subscript): #TODO: IMPLEMENT THIS I JUST WROTE SOME STUFF I'M NOT SUPER SURE HOW THIS SHOULD WORK
		tmp = add_variable(variables, None)
		last.next = SimpleExpression("InjectFrom", None, last, tmp, i, 0)
		last = last.next
		last.next = SimpleExpression("CallFunc", None, last, None, GlobalFuncName("get_subscript"), [output, tmp])
		last = last.next
	else:
		raise Exception("No AST match: {0} - flatten".format(str(ast)))

def flatten(ast):
	variables = {}
	return (flattenRecurs(ast, variables), variables)

def add_instruction(prev, new_instruction):
	if prev != None:
		prev.next = new_instruction
	new_instruction.prev = prev
	return new_instruction

def asssembly_link(first_expression, function):
	node = flatAst
	first = None
	last = None
	while node != None:
		if node.operation == "FunctionStart":
			for i in range(0, len(node.output)):
				last = add_instruction(last, IRNode("movl", Stack(str(4*(2+i)) + "(%ebp)"), node.output[i]))
		elif node.operation == "FunctionEnd":
			pass
		elif node.operation == "Assign":
			last = add_instruction(last, IRNode("movl", node.input1, node.output))
		elif node.operation == "Add":
			last = add_instruction(last, IRNode("movl", node.input1, node.output))
			last = add_instruction(last, IRNode("addl", node.input2, node.output))
		elif node.operation == "Neg":
			last = add_instruction(last, IRNode("movl", node.input1, node.output))
			last = add_instruction(last, IRNode("negl", node.output, None))
		elif node.operation == "InjectFrom":
			last = add_instruction(last, IRNode("movl", node.input1, node.output))
			if node.input2 != 3:
				last = add_instruction(last, IRNode("sall", 2, node.output))
				last = add_instruction(last, IRNode("orl", node.input2, node.output))
			else:
				last = add_instruction(last, IRNode("addl", 3, node.output))
		elif node.operation == "ProjectTo":
			last = add_instruction(last, IRNode("movl", node.input1, node.output))
			if node.input2 != 3:
				last = add_instruction(last, IRNode("sarl", 2, node.output))
			else:
				last = add_instruction(last, IRNode("andl", -4, node.output))
		elif node.operation == "GetTag":
			last = add_instruction(last, IRNode("movl", node.input1, node.output))
			last = add_instruction(last, IRNode("andl", 3, node.output))
		elif node.operation == "IfExp":
			last = add_instruction(last, IRNode("IfExp", node.input1, node.output))
			last.thenNext = createAssembly(node.thenNext, func_name)
			last.elseNext = createAssembly(node.elseNext, func_name)
		elif node.operation == "CompareEQ":
			if isinstance(node.input1, Variable):
				last = add_instruction(last, IRNode("cmpl", node.input2, node.input1))
			else:
				last = add_instruction(last, IRNode("cmpl", node.input1, node.input2))
			last = add_instruction(last, IRNode("sete", Variable("al"), None))
			last = add_instruction(last, IRNode("movzbl", Variable("al"), node.output))
		elif node.operation == "CompareNE":
			last = add_instruction(last, IRNode("cmpl", node.input1, node.input2))
			last = add_instruction(last, IRNode("setne", Variable("al"), None))
			last = add_instruction(last, IRNode("movzbl", Variable("al"), node.output))
		elif node.operation == "Not":
			last = add_instruction(last, IRNode("cmpl", 0, node.input1))
			last = add_instruction(last, IRNode("sete", Variable("al"), None))
			last = add_instruction(last, IRNode("movzbl", Variable("al"), node.output))
		elif node.operation == "CallFunc":
			for var in reversed(node.input2):
				last = add_instruction(last, IRNode("pushl", var, None))
			last = add_instruction(last, IRNode("call", node.input1, None))
			if node.output != None:
				last = add_instruction(last, IRNode("movl", Variable("eax"), node.output))
			last = add_instruction(last, IRNode("addl", 4*len(node.input2), Stack("%esp")))
		elif node.operation == "Return":
			last = add_instruction(last, dataTypes.IRNode("movl", node.input1, dataTypes.Variable("eax")))
			last = add_instruction(last, dataTypes.IRNode("jmp", func_name + "_end", None))
		else:
			raise Exception("No flatAST match: " + str(node))
		node = node.next
	return dataTypes.get_first(last)

def add_label(labels):
	name = "label_" + str(len(labels))
	labels.append(name)
	return name

def insert_into_list(first, second):
	first.next = second
	second.prev = first

def flatten_if_statement(flattened_assembly, labels, function):
	current = flattened_assembly
	while current != None:
		if current.type == "IfExp":
			label_0 = add_label(labels, function)
			label_1 = add_label(labels, function)
			compare = dataTypes.IRNode("cmpl", 0, current.input1)
			insert_into_list(current.prev, compare)
			jump_0 = dataTypes.IRNode("je", label_0, None)
			insert_into_list(compare, jump_0)
			then_ = flatten_if_statement(current.thenNext, labels, function)
			insert_into_list(jump_0, then_)
			last = dataTypes.get_last(then_)
			jump_1 = dataTypes.IRNode("jmp", label_1, None)
			insert_into_list(last, jump_1)
			inst_label = dataTypes.IRNode(label_0 + ":", None, None)
			insert_into_list(jump_1, inst_label)
			else_ = flatten_if_statement(current.elseNext, labels, function)
			insert_into_list(inst_label, else_)
			last2 = dataTypes.get_last(else_)
			inst_label2 = dataTypes.IRNode(label_1 + ":", None, None)
			insert_into_list(last2,inst_label2)
			if current.next != None:
				insert_into_list(inst_label2,current.next)
		current = current.next
	return flattened_assembly
