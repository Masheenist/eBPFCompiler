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
import heapify_ange
import closureconv
import heapify
import closure
from NewDataTypes import *

import parser as parser
import uniquify
import string

def parse(program):
	return compiler.parseFile(program)

def main():
	with open(sys.argv[1], "r") as program_file:
		file_text = program_file.read()
		print('\nTest File [{1}]\n- - - - - - - -\n{0}- - - - - - - -'.format(file_text, sys.argv[1]))
# 	test0 = """
# a = [3]
# def f(b):
#     c = [a[0] + b]
#     return lambda x: c[0] + x
#
# q = f(0)
# q(1)
# """

	print "--------COMPILE--------"
	ast = compiler.parse(file_text)	# dataTypes.ast_print(ast, 0)
	
	print "ast : {0}".format(ast)
	print "\n\n\n"
	# with open(sys.argv[1], "r") as program_file:
	# 	file_text = program_file.read()
	# 	print('\nTest File [{1}]\n- - - - - - - -\n{0}- - - - - - - -'.format(file_text, sys.argv[1]))
	# ast = compiler.parse(file_text)

	#UNIQUIFY HERE
	print "--------UNIQUIFY--------"
	# functions.find_variables(ast)
	ast = uniquify.uniquify_wrapper(ast)
	print ast
	print "\n\n\n"

	#UNIFY LAMBDAS
	print "--------UNIFY_LAMBDAS--------"
	lf = functions.LambdaUnifier()
	lf.lambdaUnify(ast)
	print lf.tree
	print "\n\n\n"
	
	ast = lf.tree

	print "--------EXPLICATE--------"
	ast = explicate.explicate(ast, {})
	print("explicate {0}\n").format(ast)
	print "\n\n\n"


	#HEAPIFY
	print "--------HEAPIFY--------"
	heap_variables = heapify.determine_heap(ast)
	print "heap variables : {0}\n\n".format(heap_variables)
	ast = heapify.heapify(ast, heap_variables)
	print "heapified ast : {0}".format(ast)
	# print "pre-heap : {0}".format(ast)
	# # heapify_ange.find_frees(ast)
	# print "post-heap : {0}".format(ast)
	# # print variables_list
	#
	# hpfy = heapify_ange.Heapifier()
	# print "heapify {0}".format(hpfy)
	# hpfy.heapify(ast)
	# print hpfy.tree
	#
	# #CLOSURE CONVERSION
	# print hpfy.frees_for_each_func
	print "\n\n\n"

	print "--------CLOSURE_CONV--------"
	# cc = closureconv.ClosureConverter(hpfy.frees_for_each_func)#{'lambda_0': ['a'], 'lambda_1': ['c']})
	# cc.closureConversion(hpfy.tree)
	# ast = cc.tree
	# print ast
	# print "\n\n\n"
	#
	# for node in cc.tree.node.nodes:
	# 	if not isinstance(node, Stmt):
	# 		print "node : {0}".format(node)
	# for node in cc.tree.node.nodes[0].nodes:
	# 	print node
	all_functions = closure.closure(ast)
	print("functions:")
	# dataTypes.ast_print(all_functions, 0)
	for function in all_functions:
		print "\t{0}".format(function)
	print "\n\n\n"

	# print "--------EXPLICATE--------"
	# explicate_ast = explicate.explicate(ast, {})
	# print("explicate {0}\n").format(explicate_ast)
	# print "\n\n\n"

	# typeCheck.type_selector().type_check(explicate_ast,{})
	# all_functions = [node.defaults for node in cc.tree.node.nodes if not isinstance(node, Stmt)]
	# all_functions = [node for node in cc.tree.node.nodes if not isinstance(node, Stmt)]

	# #UNIQUIFY HERE
	# unique_ast = find_variables.find_variables(ast)

	# explicate_ast = explicate.explicate(unique_ast, {})
	# print("explicate {0}\n").format(explicate_ast)

	# typeCheck.type_selector().type_check(explicate_ast,{})

	# HEAPIFY HERE - return ast
	# heapify_ast = heapify.heapify_ast(explicate_ast)

	# CLOSURES HERE - return dict of function
	# all_functions = closure.closure(heapify_ast)

	functions_assembly = {}
	graph_nodes = {}
	graph_colors = {}

	for function in all_functions:
		print "--------FLATTEN--------"
		ast, variable_list = flatten.flatten(all_functions[function])
		print "{0} : ".format(function)
		dataTypes.print_linked_list_new(ast)
		print '\n\n\n'

		print "--------ASSEMBLY--------"
		flattened_assembly = flatten.assembly_link(ast, function)
		dataTypes.print_linked_list_new(flattened_assembly)
		print '\n\n\n'

		liveness.liveness(flattened_assembly, set([]))
		spillage_list = []
		while True:
			liveness.liveness(flattened_assembly, set([]))
			graph_nodes[function] = graph.create_graph(flattened_assembly, variable_list, spillage_list)
			print("--------COLORING--------\ngraph_nodes[{1}] : {0}\n\n").format(graph_nodes[function], function)
			graph_colors[function] = graph.color_graph(graph_nodes[function])
			print("graph_colors[{1}] : {0}\n\n\n").format(graph_colors[function],function)
			flattened_assembly, new_spill_check = spillage.spillage(flattened_assembly, graph_nodes[function], variable_list)
			if not new_spill_check:
				break
			else:
				spillage_list.extend(new_spill_check)

				print("--------SPILLS--------\nspillage : {0}\n\n\n").format(spillage_list)
		cond_assembly = flatten.flatten_if_statement(flattened_assembly, [], function)
		print("--------FINAL FUNCTION ASSEMBLY--------\ncond_assembly : {0}\n\n\n").format(cond_assembly)
		functions_assembly[function] = cond_assembly
	# assembly.write_assembly(sys.argv[1].replace(".py",".s"), functions_assembly, graph_nodes, graph_colors)

	assembly.write_assembly_file(sys.argv[1].replace(".py",".s"), functions_assembly, graph_nodes, graph_colors)

	with open(sys.argv[1].replace(".py",".s"), "r") as program_file:
		file_text = program_file.read()
		print('--------FINAL ASSEMBLY FILE--------\n[{1}] :\n{0}\n'.format(file_text, sys.argv[1]))


	os.system('gcc -m32 -g {0} runtime/libpyyruntime.a -lm -o {1}'.format(sys.argv[1].replace(".py",".s"), sys.argv[1][:-3]))
	os.system('cat {0} | {1} > {2}'.format(sys.argv[1].replace(".py",".in"), sys.argv[1][:-3], sys.argv[1]).replace(".py",".out"))

	file_exists = os.path.exists(sys.argv[1].replace(".py",".in"))
	if file_exists:
		print '\ninput: '
		with open(sys.argv[1].replace(".py",".in")) as f:
			contents = f.read()
			print contents
	file_exists = os.path.exists(sys.argv[1].replace(".py",".out"))
	if file_exists:
		print '\noutput: '
		with open(sys.argv[1].replace(".py",".out")) as f:
			contents = f.read()
			print contents
	# print '\nexpected output: '
	# os.system('python2 ' + str(sys.argv[1]))
main()