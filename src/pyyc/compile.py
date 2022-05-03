#Rhett Hanscom, Ange Ishimwe, Sylvia Llosa, and Pranav 

import sys
import os
import ast
import compiler
from compiler.ast import *

from dataTypes import *
from flatten import *
#import assembly
from astToC import *

def parse(program):
	return compiler.parseFile(program)

#translate txt file of ast nodes into C
	#Function Defintion:
	# Name: traverse_list
	#Operation:
	#1 - Visit each ast node
	#2 - Convert python to C
	#3 - Save file

def main():
	with open(sys.argv[1], "r") as program_file:
		file_text = program_file.read()
		print('\nTest File [{1}]\n- - - - - - - -\n{0}- - - - - - - -'.format(file_text, sys.argv[1]))
		ast = compiler.parse(file_text)
	print '\nAST\n- - - - - - - -\n{0}\n- - - - - - - -'.format(ast)
	#first_expression = flatten_expression(ast)
	#print_expressions(first_expression)
	#assembly.traverse_list(first_expression, sys.argv[1].replace(".py",".s"))
	first_expression = convertNodeToC(ast)
	print_expressions(first_expression)
	astToC.traverse_ast(first_expression, sys.argv[1].replace(".py",".c"))

	#os.system('gcc -m32 -g {0} runtime/libpyyruntime.a -lm -o {1}'.format(sys.argv[1].replace(".py",".s"), sys.argv[1][:-3]))
	#os.system('cat {0} | {1} > {2}'.format(sys.argv[1].replace(".py",".in"), sys.argv[1][:-3], sys.argv[1]).replace(".py",".out"))
	
	print '\ninput: '
	with open(sys.argv[1].replace(".py",".in")) as f:
		contents = f.read()
		print contents
	
	print '\noutput: '
	with open(sys.argv[1].replace(".py",".out")) as f:
		contents = f.read()
		print contents
main()

