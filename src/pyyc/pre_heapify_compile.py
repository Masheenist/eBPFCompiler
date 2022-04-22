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
import closureconv
from NewDataTypes import *


def parse(program):
	return compiler.parseFile(program)

def main():
    test0 = """
a = [3]
def f(b):
    c = [a[0] + b]
    return lambda x: c[0] + x
q = f(0)
q(1)
"""

    ast = compiler.parse(test0)
    print ast
    print "\n\n\n"
    # with open(sys.argv[1], "r") as program_file:
    # 	file_text = program_file.read()
    # 	print('\nTest File [{1}]\n- - - - - - - -\n{0}- - - - - - - -'.format(file_text, sys.argv[1]))
    # ast = compiler.parse(file_text)

    #UNIQUIFY HERE
    functions.find_variables(ast)
    print ast
    print "\n\n\n"
    
    #UNIFY LAMBDAS
    lf = functions.LambdaUnifier()
    lf.lambdaUnify(ast)
    print lf.tree
    print "\n\n\n"

    ast = lf.tree

    #SKIP HEAPIFY FOR NOW

    #CLOSURE CONVERSION
    cc = closureconv.ClosureConverter({'lambda_0': ['a'], 'lambda_1': ['c']})
    cc.closureConversion(lf.tree)
    ast = cc.tree

    for node in cc.tree.node.nodes:
        if not isinstance(node, Stmt):
            print node
    for node in cc.tree.node.nodes[0].nodes:
        print node
    print "\n\n\n"

    explicate_ast = explicate.explicate(ast, {})
    print("explicate {0}\n").format(explicate_ast)
    print "\n\n\n"

    # typeCheck.type_selector().type_check(explicate_ast,{})
    # all_functions = [node.defaults for node in cc.tree.node.nodes if not isinstance(node, Stmt)]
    all_functions = [node for node in cc.tree.node.nodes if not isinstance(node, Stmt)]
    # print all_functions

    functions_assembly = {}
    graph_nodes = {}
    graph_colors = {}

    for function in all_functions:
        # flattened_ast, variable_list = flatten.flatten_expression(all_functions[function])
        flattened_ast, variable_list = flatten.flatten(function)

        flattened_assembly = flatten.assembly_link(flattened_ast, function)
        liveness.liveness(flattened_assembly, set([]))
        spillage_list = []
        while True:
            liveness.liveness(flattened_assembly, set([]))
            graph_nodes[function] = graph.create_graph(flattened_assembly, variable_list, spillage_list)
            print("graph_nodes[function] : {0}").format(graph_nodes[function])
            graph_colors[function] = graph.color_graph(graph_nodes[function])
            print("graph_colors[function] : {0}").format(graph_colors[function])
            flattened_assembly, new_spill_check = spillage.spillage(flattened_assembly, graph_nodes[function], variable_list)
            if not new_spill_check:
                break
            else:
                spillage_list.extend(new_spill_check)
                print("spillage : {0}").format(spillage_list)
        cond_assembly = flatten.flatten_if_statement(flattened_assembly, [], function)
        print("cond_assembly : {0}").format(cond_assembly)
        functions_assembly[function] = cond_assembly
        assembly.write_assembly(sys.argv[1].replace(".py",".s"), functions_assembly, graph_nodes, graph_colors)

    assembly.write_assembly_file(sys.argv[1].replace(".py",".s"), functions_assembly, graph_nodes, graph_colors)

    with open(sys.argv[1].replace(".py",".s"), "r") as program_file:
        file_text = program_file.read()
        print('final assembly file [{1}] :\n{0}\n'.format(file_tesxt, sys.argv[1]))


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