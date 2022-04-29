#Rhett Hanscom, Ange Ishimwe, Sylvia Llosa, and Pranav 

import sys
import os
import ast
import compiler
from compiler.ast import *

from dataTypes import *
import flatten
import assembly

def parse(program):
	return compiler.parseFile(program)

#translate txt file of ast nodes into assembly
	#traversing linked list SimpleExpression and writing to file
	#Function Defintion:
	# Name: traverse_list
	# Parameters:  instance of linkedList, type "SimpleExpression"
	#Operation:
	#1 - Visit each node on linked list
	#2 - Convert each node into assembly (string)
	#3 - Write each assembly string to the file, newline-terminated
	#4 - Save file

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

def main():
	with open(sys.argv[1], "r") as program_file:
		file_text = program_file.read()
		print('\nTest File [{1}]\n- - - - - - - -\n{0}- - - - - - - -'.format(file_text, sys.argv[1]))
		ast = compiler.parse(file_text)
	# print '\nAST\n- - - - - - - -\n{0}\n- - - - - - - -'.format(ast)
	first_expression = flatten.flatten_expression(ast)
	print_expressions(first_expression)
	traverse_list(first_expression, sys.argv[1].replace(".py",".s"))

	# os.system('gcc -m32 -g {0} runtime/libpyyruntime.a -lm -o {1}'.format(sys.argv[1].replace(".py",".s"), sys.argv[1][:-3]))
	# os.system('cat {0} | {1} > {2}'.format(sys.argv[1].replace(".py",".in"), sys.argv[1][:-3], sys.argv[1]).replace(".py",".out"))
	#
	print '\ninput: '
	with open(sys.argv[1].replace(".py",".in")) as f:
		contents = f.read()
		print contents
	
	print '\noutput: '
	with open(sys.argv[1].replace(".py",".out")) as f:
		contents = f.read()
		print contents
main()

