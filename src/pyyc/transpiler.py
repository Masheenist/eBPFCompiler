#!/usr/bin/python
#P0 statement interpreter translates a .py into a .s
#Rhett Hanscom and Sylvia Llosa

# Rhett Notes:
 # *test3.py - too many Name type nodes possibly. Nodes 4 + 8 are the same in
 # the linked list, though this does reflect the number of Name() occurances
 # in the provided AST.

import sys
import os
import re
from ast import *
from convert import convert_CIR, convert_to_c


def print_python3_ast(ast, tabs=0):
	# if an assign is marked as ctx=Load() or Store() we are indifferent.
	if isinstance(ast, Module):
		# print every entry in module's body
		print("\t"*tabs + "Module(\n\tbody=[")
		for entry in ast.body:
			print_python3_ast(entry, tabs=2)
		print("\t]\n)")
	elif isinstance(ast, FunctionDef):
		# print every argument
		print("\t"*tabs + "FunctionDef(\n" + "\t"*(tabs+1) + "name=" + ast.name)
		print("\t"*(tabs+1) + "args=")
		print_python3_ast(ast.args, tabs=tabs+2)
		# print every entry in funcs's body
		print("\t"*(tabs+1) + "body=[")
		for entry in ast.body:
			print_python3_ast(entry, tabs=tabs+2)
		print("\t"*(tabs+1)+"],")
		# print decorator_list
		if len(ast.decorator_list) == 0:
			print("\t"*(tabs+1) + "decorator_list=[],")
		else:
			print("\t"*(tabs+1) + "decorator_list=[")
			for entry in ast.decorator_list:
				print_python3_ast(entry, tabs = tabs+2)
			print("\t"*(tabs+1) + "],")
		# print returns (I believe this is type stuff? not relevant though)
		if ast.returns:
			print("\t"*(tabs+1) + "returns=" + dump(ast.returns))
		else:
			print("\t"*(tabs+1) + "returns=None")
		print("\t"*tabs + ")")
	elif isinstance(ast, Assign):
		print ("\t"*tabs + "Assign(")
		# print targets
		if len(ast.targets) == 0:
			print("\t"*(tabs+1) + "targets=[]")
		else:
			print("\t"*(tabs+1) + "targets=[")
			for entry in ast.targets:
				print_python3_ast(entry, tabs = tabs+2)
			print("\t"*(tabs+1) + "],")
		# print value
		print("\t"*(tabs+1) + "value=")
		print_python3_ast(ast.value, tabs=tabs+2)
		print("\t"*tabs + ")")
	elif isinstance(ast, Expr):
		print ("\t"*tabs + "Expr(")
		# print value
		print("\t"*(tabs+1) + "value=")
		print_python3_ast(ast.value, tabs=tabs+2)
		print("\t"*tabs + ")")
	elif isinstance(ast, BinOp):
		print ("\t"*tabs + "BinOp(")
		# print left
		print("\t"*(tabs+1) + "left=")
		print_python3_ast(ast.left, tabs=tabs+2)
		# print op
		print("\t"*(tabs+1) + "op=" + dump(ast.op))
		# print right
		print("\t"*(tabs+1) + "right=")
		print_python3_ast(ast.right, tabs=tabs+2)
		print("\t"*tabs + ")")
	elif isinstance(ast, UnaryOp):
		print ("\t"*tabs + "UnaryOp(")
		# print op
		print("\t"*(tabs+1) + "op=" + dump(ast.op))
		# print operand
		print("\t"*(tabs+1) + "operand=")
		print_python3_ast(ast.operand, tabs=tabs+2)
		print("\t"*tabs + ")")
	elif isinstance(ast, Call):
		print("\t"*tabs + "Call(")
		# print args
		if len(ast.args) == 0:
			print("\t"*(tabs+1) + "args=[]")
		else:
			print("\t"*(tabs+1) + "args=[")
			for entry in ast.args:
				print_python3_ast(entry, tabs = tabs+2)
			print("\t"*(tabs+1) + "],")
		# print keywords
		if len(ast.keywords) == 0:
			print("\t"*(tabs+1) + "keywords=[]")
		else:
			print("\t"*(tabs+1) + "keywords=[")
			for entry in ast.keywords:
				print_python3_ast(entry, tabs = tabs+2)
			print("\t"*(tabs+1) + "]")
		print("\t"*tabs + ")")
	elif isinstance(ast, Name):
		# has id, and ctx (context, unimportant i think)
		print("\t"*tabs + dump(ast))
	elif isinstance(ast, arguments):
		print("\t"*tabs + "arguments(")
		# print args
		if len(ast.args) == 0:
			print("\t"*(tabs+1) + "args=[]")
		else:
			print("\t"*(tabs+1) + "args=[")
			for entry in ast.args:
				print_python3_ast(entry, tabs = tabs+2)
			print("\t"*(tabs+1) + "]")
		# print vararg
		if ast.vararg:
			print("\t"*(tabs+1) + "vararg=" + dump(ast.vararg))
		else:
			print("\t"*(tabs+1) + "vararg=None")

		# print kwonlyargs
		if len(ast.kwonlyargs) == 0:
			print("\t"*(tabs+1) + "kwonlyargs=[]")
		else:
			print("\t"*(tabs+1) + "kwonlyargs=[")
			for entry in ast.kwonlyargs:
				print_python3_ast(entry, tabs = tabs+2)
			print("\t"*(tabs+1) + "]")
		# print kw_defaults
		if len(ast.kw_defaults) == 0:
			print("\t"*(tabs+1) + "kw_defaults=[]")
		else:
			print("\t"*(tabs+1) + "kw_defaults=[")
			for entry in ast.kw_defaults:
				print_python3_ast(entry, tabs = tabs+2)
			print("\t"*(tabs+1) + "]")
		# print kwarg
		if ast.kwarg:
			print("\t"*(tabs+1) + "kwarg=" + dump(ast.kwarg))
		else:
			print("\t"*(tabs+1) + "kwarg=None")
		# print defaults
		if len(ast.defaults) == 0:
			print("\t"*(tabs+1) + "defaults=[]")
		else:
			print("\t"*(tabs+1) + "defaults=[")
			for entry in ast.defaults:
				print_python3_ast(entry, tabs = tabs+2)
			print("\t"*(tabs+1) + "]")
	elif isinstance(ast, Num):
		# just has n
		print("\t"*tabs + dump(ast))
	elif isinstance(ast, Str):
		# just has s
		print("\t"*tabs + dump(ast))
	elif isinstance(ast, arg):
		# has arg, and annotation (temporary hack if we can't figure out typing BUT if we bail on figuring out typing we need to at least do complicated types like [] {} and BPF maps)
		print("\t"*tabs + dump(ast))
	elif isinstance(ast, Return):
		# just has value
		print("\t"*tabs + dump(ast))
	else:
		print("UNCAUGHT TYPE " + str(type(ast).__name__))
		print("\t"*tabs + dump(ast))


def print_IRC(inst_list):
	for statement in inst_list:
		# FUNCTION
		if len(statement) == 3:
			print("FUNC_NAME : {0}".format(statement[0]))
			print("FUNC_ARGS : {0}".format(statement[1]))
			for item in statement[2]:
				print("BODY : {0}".format(item))
		else:
			print(statement)

def main():
	with open(sys.argv[1], "r") as program_file:
		file_text = program_file.read()
		print('\nTest File [{1}]\n- - - - - - - -\n{0}- - - - - - - -'.format(file_text, sys.argv[1]))
		ast = parse(file_text)#compiler.parse(file_text)
		# print("ast:[{0}]".format(ast))
		print_python3_ast(ast)

		IRC = convert_CIR(ast, [])
		print_IRC(IRC)
		convert_to_c(IRC, sys.argv[1].replace('.py', '.c'))

		f = open(sys.argv[1].replace('.py', '.c'), "r")
		print("\n\nC FILE CREATED:\n\n{0}\n".format(f.read()))
		# print()
		#print(dump(ast))
		#print()
	# print('\nAST\n- - - - - - - -\n{0}\n- - - - - - - -'.format(ast))
	# first_expression = flatten_expression(ast)
	# print_expressions(first_expression)
	# traverse_list(first_expression, sys.argv[1].replace(".py",".s"))

main()
