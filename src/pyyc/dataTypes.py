import sys
import compiler
from compiler.ast import *

# SimpleExpression Node Guide :
  # NODE TYPE : Module
  # 	*can ignore
  # NODE TYPE : Stmt
  # 	*will mark BEGINNING and END
  # 	of statement (where end of link
  # 	list is inserted.)
  # NODE TYPE : Assign
  # 	*input1 = name
  # 	*output = value
  # NODE TYPE : AssName
  # 	*input1 = name
  # NODE TYPE : Discard
  # 	*input1 = name
  # NODE TYPE : Const
  # 	*input1 = temp name
  # 	*output = value
  # NODE TYPE : Name
  # 	*input1 = name
  # NODE TYPE : Print
  # 	*input1 = name of variable to print
  # NODE TYPE : ADD
  # 	*input1 = left variable name
  # 	*input2 = right variable name
  # 	*ouput 	= new variable (holds sum)
  # NODE TYPE : UnarySub
  # 	*input1  = new variable to hold term
  # 	*output = negative term
  # NODE TYPE : CallFunc::Input
  # 	*input1 = new variable name to hold
  # 			  input value


# class which forms a doubly linked list of nodes, comprised of simple expressions
# formed from the input ast built from complex expression
class SimpleExpression():
	def __init__(self, type, input1, input2, output, prev, next):
		self.type   = type      # can be AST node type
		self.input1 = input1    # will be Name of Variable types (Such as AssName, etc..)
		self.input2 = input2
		self.output = output    # will hold Value of Variable type data
		self.prev   = prev
		self.next   = next

# return simple expression currently at the end of the linked list
def get_last(simple_expression):
	while simple_expression.prev != None:
		simple_expression = simple_expression.prev
	while simple_expression.next != None:
		simple_expression = simple_expression.next
	return simple_expression

def get_value(simple_expression, variable_name):
	returnValue = None
	negate = False
	while simple_expression.prev != None:
		simple_expression = simple_expression.prev
	while simple_expression != None:
		if simple_expression.type != "Add":
			if simple_expression.input1 == variable_name and simple_expression.output != None:
				returnValue = simple_expression.output
		simple_expression = simple_expression.next
	return returnValue

def print_expressions(simple_expression):
	while simple_expression.prev != None:
		simple_expression = simple_expression.prev
	count = 0

	print '\nSimple Expression Linked List\n- - - - - - - -'

	print '[count]\t[type]\t\t[input1]\t[input2]\t[output]'
	while simple_expression != None:
		if simple_expression.type == "StartList" :
			print '[{0}]\t{1}\t{2}\t\t{3}\t\t{4}'.format(count, simple_expression.type, simple_expression.input1, simple_expression.input2, simple_expression.output)
		elif simple_expression.type == "UnarySub" :
			print '[{0}]\t{1}\t{2}\t\t{3}\t\t{4}'.format(count, simple_expression.type, simple_expression.input1, simple_expression.input2, simple_expression.output)
		else:
			print '[{0}]\t{1}\t\t{2}\t\t{3}\t\t{4}'.format(count, simple_expression.type, simple_expression.input1, simple_expression.input2, simple_expression.output)
		count += 1
		simple_expression = simple_expression.next
	print '- - - - - - - -\n'
	return
