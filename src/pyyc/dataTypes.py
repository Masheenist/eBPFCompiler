import sys
import compiler
from NewDataTypes import *
from compiler.ast import *

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

def print_linked_list_new(node):
	while node != None:
		string = "\t"
		string += str(node)
		print string
		if node.type == "IfExp":
			string = "\t"
			string += "Then : "
			print string
			print_linked_list_new(node.thenNext)
			string = "\t"
			string += "Else : "
			print string
			print_linked_list_new(node.elseNext)
			print "\tEndif"
		if node.type == "While":
			print "\tComparison:"
			print_linked_list_new(node.elseNext)
			print "\tInWhile:"
			print_linked_list_new(node.thenNext)
			print "\tAfter"

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

def indent(str, indents):
	string = ""
	for i in range(0, indents):
		string += "\t"
	print string + str

def ast_print(ast, indents):
	if isinstance(ast, Module):
		indent("Module(", indents)
		ast_print(ast.node, indents+1)
		indent(")", indents)
	elif isinstance(ast, Stmt):
		indent("Stmt(", indents)
		ast_print(ast.nodes, indents+1)
		indent(")", indents)
	elif isinstance(ast, Printnl):
		indent("Printnl(", indents)
		ast_print(ast.nodes, indents+1)
		indent(")", indents)
	elif isinstance(ast, Assign):
		indent("Assign(", indents)
		ast_print(ast.nodes, indents+1)
		indent(",", indents+1)
		ast_print(ast.expr, indents+1)
		indent(")", indents)
	elif isinstance(ast, AssName):
		indent("AssName(", indents)
		ast_print(ast.name, indents+1)
		indent(",", indents+1)
		ast_print(ast.flags, indents+1)
		indent(")", indents)
	elif isinstance(ast, Discard):
		indent("Discard(", indents)
		ast_print(ast.expr, indents+1)
		indent(")", indents)
	elif isinstance(ast, Const):
		indent("Const(", indents)
		indent(str(ast.value), indents+1)
		indent(")", indents)
	elif isinstance(ast, Bool):
		indent("Bool(", indents)
		indent(str(ast.value), indents+1)
		indent(")", indents)
	elif isinstance(ast, Name):
		indent("Name(", indents)
		ast_print(ast.name, indents+1)
		indent(")", indents)
	elif isinstance(ast, Add):
		indent("Add(", indents)
		ast_print(ast.left, indents+1)
		indent(",", indents+1)
		ast_print(ast.right, indents+1)
		indent(")", indents)
	elif isinstance(ast, Compare):
		indent("Compare(", indents)
		ast_print(ast.expr, indents+1)
		indent(",", indents+1)
		ast_print(ast.ops, indents+1)
		indent(")", indents)
	elif isinstance(ast, UnarySub):
		indent("UnarySub(", indents)
		ast_print(ast.expr, indents+1)
		indent(")", indents)
	elif isinstance(ast, Not):
		indent("Not(", indents)
		ast_print(ast.expr, indents+1)
		indent(")", indents)
	elif isinstance(ast, CallFunc):
		indent("CallFunc(", indents)
		ast_print(ast.node, indents+1)
		indent(",", indents+1)
		ast_print(ast.args, indents+1)
		indent(")", indents+1)
	elif isinstance(ast, List):
		indent("List(", indents)
		ast_print(ast.nodes, indents+1)
		indent(")", indents)
	elif isinstance(ast, list):
		indent("[", indents)
		for node in ast:
			ast_print(node, indents)
			indent(",", indents)
		indent("]", indents)
	elif isinstance(ast, Dict):
		indent("Dict(", indents)
		ast_print(ast.items, indents+1)
		indent(")", indents)
	elif isinstance(ast, tuple):
		indent("(", indents)
		for node in ast:
			ast_print(node, indents+1)
			indent(",", indents+1)
		indent(")", indents)
	elif isinstance(ast, dict):
		indent("{", indents)
		for key in ast:
			indent(key + ":", indents)
			ast_print(ast[key], indents+1)
			indent(",", indents)
		indent("}",indents)
	elif isinstance(ast, IfExp):
		indent("IfExp(", indents)
		ast_print(ast.test, indents+1)
		indent(",", indents+1)
		ast_print(ast.then, indents+1)
		indent(",", indents+1)
		ast_print(ast.else_, indents+1)
		indent(")", indents)
	elif isinstance(ast, Let):
		indent("Let(", indents)
		ast_print(ast.var, indents+1)
		indent(",", indents+1)
		ast_print(ast.rhs, indents+1)
		indent(",", indents+1)
		ast_print(ast.body, indents+1)
		indent(")", indents)
	elif isinstance(ast, InjectFrom):
		indent("InjectFrom(", indents)
		ast_print(ast.typ, indents+1)
		indent(",", indents+1)
		ast_print(ast.arg, indents+1)
		indent(")", indents)
	elif isinstance(ast, ProjectTo):
		indent("ProjectTo(", indents)
		ast_print(ast.typ, indents+1)
		indent(",", indents+1)
		ast_print(ast.arg, indents+1)
		indent(")", indents)
	elif isinstance(ast, GetTag):
		indent("GetTag(", indents)
		ast_print(ast.arg, indents+1)
		indent(")", indents)
	elif isinstance(ast, Lambda):
		indent("Lambda(", indents)
		ast_print(ast.argnames, indents+1)
		indent(",", indents+1)
		ast_print(ast.code, indents+1)
		indent(")", indents)
	elif isinstance(ast, Function):
		indent("Function(", indents)
		ast_print(ast.name, indents+1)
		indent(",", indents+1)
		ast_print(ast.argnames, indents+1)
		indent(",", indents+1)
		ast_print(ast.code, indents+1)
		indent(")", indents)
	elif isinstance(ast, GlobalFuncName):
		indent("GlobalFuncName(", indents)
		ast_print(ast.name, indents+1)
		indent(")", indents)
	elif isinstance(ast, Return):
		indent("Return(", indents)
		ast_print(ast.value, indents+1)
		indent(")", indents)
	elif isinstance(ast, str):
		indent(ast, indents)
	else:
		raise Exception("No AST match: " + str(ast))