#!/usr/bin/python
#Rhett Hanscom and Sylvia Llosa

import sys
import os
import ast
import compiler
from compiler.ast import *

import dataTypes
import assembly
import flatten
import liveness
import graph
import spillage
import explicate
import typeCheck
import functions
from NewDataTypes import *


def parse(program):
	return compiler.parseFile(program)

def main():
	with open(sys.argv[1], "r") as program_file:
		file_text = program_file.read()
		print('\nTest File [{1}]\n- - - - - - - -\n{0}- - - - - - - -'.format(file_text, sys.argv[1]))
	ast = compiler.parse(file_text)

	#UNIQUIFY HERE
	unique_ast = find_variables.find_variables(ast)

	explicate_ast = explicate.explicate(unique_ast, {})
	print("explicate {0}\n").format(explicate_ast)

	typeCheck.type_selector().type_check(explicate_ast,{})

	# HEAPIFY HERE - return ast
	# heapify_ast = heapify.heapify_ast(explicate_ast)

	# CLOSURES HERE - return dict of function
	# all_functions = closure.closure(heapify_ast)

	# functions_assembly = {}
	# graph_nodes = {}
	# graph_colors = {}
	#
	# for function in all_functions:
	# 	flattened_ast, variable_list = flatten.flatten_expression(all_functions[function])
	# 	flattened_assembly = flatten.assembly_link(flattened_ast, function)
	# 	liveness.liveness(flattened_assembly, set([]))
	# 	spillage_list = []
	# 	while True:
	# 		liveness.liveness(flattened_assembly, set([]))
	# 		graph_nodes[function] = graph.create_graph(flattened_assembly, variable_list, spillage_list)
	# 		print("graph_nodes[function] : {0}").format(graph_nodes[function])
	# 		graph_colors[function] = graph.color_graph(graph_nodes[function])
	# 		print("graph_colors[function] : {0}").format(graph_colors[function])
	# 		flattened_assembly, new_spill_check = spillage.spillage(flattened_assembly, graph_nodes[function], variable_list)
	# 		if not new_spill_check:
	# 			break
	# 		else:
	# 			spillage_list.extend(new_spill_check)
	# 			print("spillage : {0}").format(spillage_list)
	# 	cond_assembly = flatten.flatten_if_statement(flattened_assembly, [], function)
	# 	print("cond_assembly : {0}").format(cond_assembly)
	# 	functions_assembly[function] = cond_assembly
	# 	assembly.write_assembly(sys.argv[1].replace(".py",".s"), functions_assembly, graph_nodes, graph_colors)
	#
	# assembly.write_assembly_file(sys.argv[1].replace(".py",".s"), functions_assembly, graph_nodes, graph_colors)
	#
	# with open(sys.argv[1].replace(".py",".s"), "r") as program_file:
	# 	file_text = program_file.read()
	# 	print('final assembly file [{1}] :\n{0}\n'.format(file_tesxt, sys.argv[1]))


	# os.system('gcc -m32 -g {0} runtime/libpyyruntime.a -lm -o {1}'.format(sys.argv[1].replace(".py",".s"), sys.argv[1][:-3]))
	# os.system('cat {0} | {1} > {2}'.format(sys.argv[1].replace(".py",".in"), sys.argv[1][:-3], sys.argv[1]).replace(".py",".out"))
	#
	# file_exists = os.path.exists(sys.argv[1].replace(".py",".in"))
	# if file_exists:
	# 	print '\ninput: '
	# 	with open(sys.argv[1].replace(".py",".in")) as f:
	# 		contents = f.read()
	# 		print contents
	# file_exists = os.path.exists(sys.argv[1].replace(".py",".out"))
    #     if file_exists:
    #         print '\noutput: '
    #         with open(sys.argv[1].replace(".py",".out")) as f:
	# 	    contents = f.read()
	# 	    print contents
	# # print '\nexpected output: '
	# # os.system('python2 ' + str(sys.argv[1]))
main()
