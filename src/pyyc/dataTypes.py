
class SimpleExpression():
	def __init__(self, _type, _next, _prev, _output, _input1, _input2):
		self.type = _type
		self.next = _next
		self.thenNext = None
		self.elseNext = None
		self.prev = _prev
		self.output = _output
		self.input1 = _input1
		self.input2 = _input2
	def __str__(self):
		return "(" + str(self.type) + ", " + str(self.output) + ", " + str(self.input1) + ", " + str(self.input2) + ")"

class Variable():
	def __init__(self, _name):
		self.name = _name
	def __str__(self):
		return "Variable(" + str(self.name) + ")"
	def __repr__(self):
		return "Variable(" + str(self.name) + ")"

class FunctionLabel():
	def __init__(self, _name):
		self.name = _name
	def __str__(self):
		return "FunctionLabel(\'" + str(self.name) + "\')"
	def __repr__(self):
		return "FunctionLabel(\'" + str(self.name) + "\')"


class IRNode():
	'''
	def __init__(self, _type, _input1, _input2, _prev, _next):
		self.type = _type
		self.next = _next
		self.prev = _prev
		self.input1 = _input1
		self.input2 = _input2
		self.liveness = set([])
		'''
	def __init__(self, _type, _input1, _input2):
		self.type = _type
		self.input1 = _input1
		self.input2 = _input2
		self.next = None
		self.thenNext = None
		self.elseNext = None
		self.prev = None
		self.liveness = set([])
	def __str__(self):
		return "(" + str(self.type) + ", " + str(self.input1) + ", " + str(self.input2) + ", " + set_to_str(self.liveness) + ")"

class stackPointer():
	def __init__(self):
		pass
	def __str__(self):
		return "%esp"

class Stack():
	def __init__(self, _name):
		self.name = _name
	def __str__(self):
		return "Stack(" + str(self.name) + ")"
	def __repr__(self):
		return "Stack(" + str(self.name) + ")"

class GraphNode():
	def __init__(self, _unspillable):
		self.color = None
		self.saturation = set([])
		self.edges = set([])
		self.unspillable = _unspillable
		self.key = -1
	def __str__(self):
		return "GraphNode(" + str(self.color) + ", " + str(self.saturation) + ", " + str(self.unspillable) + ", " + str(self.edges) + ")"
	def __repr__(self):
		return "GraphNode(" + str(self.color) + ", " + str(self.saturation) + ", " + str(self.unspillable) + ", " + str(self.edges) + ")"

class storeHeap():
	def __init__(self, object_):
		self.value = 0
		self.object = object_
	def __repr__(self):
		return "HE(" + str(self.value) + "," + str(self.object) + ")"

def print_linked_list(node):
	while node != None:
		print node
		node = node.next

def get_last(node):
	if node != None:
		while node.next != None:
			node = node.next
	return node

def get_first(node):
	if node != None:
		while node.prev != None:
			node = node.prev
	return node

def set_to_str(set):
	string = "Set("
	first = True
	for i in set:
		if first:
			first = False
		else:
			string += ", "
		string += str(i)
	string += ")"
	return string

def dict_to_str(dict):
	string = "{"
	first = True
	for i in dict:
		if first:
			first = False
		else:
			string += ", "
		string += str(i) + " : " + str(dict[i]) + "\n"
	string += "}"
	return string

def add_variable(variable_list, name):
	if name != None:
		for i in variable_list:
			if name == variable_list[i]:
				return i
	ret = Variable(str(len(variable_list)))
	variable_list[ret] = name
	return ret
