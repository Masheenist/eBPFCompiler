import re
from ast import *
from random import randint, randrange
# global lam_count = 0

def convert_CIR(ast, inst_list, lambda_count):
	lambda_count = 0
	if isinstance(ast, Module):
		for entry in ast.body:
			inst_list.append(convert_CIR(entry, inst_list, lambda_count))
	elif isinstance(ast, FunctionDef):
		name = ast.name
		func_args_list = convert_CIR(ast.args, inst_list, lambda_count)
		func_body = []
		for entry in ast.body:
			func_body.append(convert_CIR(entry, inst_list, lambda_count))
		return [name, func_args_list, func_body]
	elif isinstance(ast, Tuple):
		name = ast.name
		elts_expr_list = convert_CIR(ast.expr, inst_list, lambda_count)
		elts_body = []
		for entry in ast.body:
			elts_body.append(convert_CIR(entry, inst_list, lambda_count))
		return [name, elts_expr_list, elts_body]
	elif isinstance(ast, Lambda):
		# print("HERE!!!!")
		unqiue_name = randint(10,99)
		name = "lambda_{0}".format(str(unqiue_name))
		lambda_count += 1
		func_args_list = convert_CIR(ast.args, inst_list, lambda_count)
		func_body = []
		func_body.append(["RETURN", "return("+convert_CIR(ast.body, inst_list, lambda_count)+")"])
		return [name, func_args_list, func_body]
	elif isinstance(ast, Assign):
		if len(ast.targets) != 0:
			target_name = []
			for entry in ast.targets:
				target_name.append(convert_CIR(entry, inst_list, lambda_count))

		# save func call
		if isinstance(ast.value, Call):
			use_target = ast.value.func.id
			func_args_list = []
			for entry in ast.value.args:
				func_args_list.append(convert_CIR(entry, inst_list, lambda_count))
			print_string = "{0}(".format(ast.value.func.id)
			for argu in func_args_list:
				print_string += argu
				print_string += ", "
			print_string = print_string[:-2]
			print_string += ")"
			return(["ASSIGN", target_name[-1], print_string])

		#save lambda call to var
		elif isinstance(ast.value, Lambda):
			use_target = convert_CIR(ast.value, inst_list, lambda_count)
			return(["ASSIGN", target_name[-1], use_target])

		# general simple assignment (e.g., x = 1 + 2)
		else:
			use_target = ast.value
		target_value = convert_CIR(use_target, inst_list, lambda_count)
		# return(["ASSIGN", "{} = {}".format(target_name[-1], target_value)])
		return(["ASSIGN", "{0}".format(target_name[-1]), target_value])
	elif isinstance(ast, Expr):
		if isinstance(ast.value, Call):
			function_name = ast.value.func.id
			function_arguments = convert_CIR(ast.value, inst_list, lambda_count)
			print_string = "{0}(".format(function_name)
			first = True
			for argu in function_arguments:
				if not first:
					print_string += ", {0}".format(arg)
				else:
					first = False
					print_string += argu
			print_string+=")"
			return(["CALL", print_string])
		if isinstance(ast.value, Lambda):
			return convert_CIR(ast.value, inst_list, lambda_count)
		if isinstance(ast.value, Load):
			expression_name = ast.value.expr.id
			expression_elts = convert_CIR(ast.value, inst_list, lambda_count)
			print_string = "{0}(".format(expression_name)
			first = True
			for elts in expression_elts:
				if not first:
					print_string += ", {0}".format(expr)
				else:
					first = False
					print_string += elts
			print_string+=")"
			return(["LOAD", print_string])
	elif isinstance(ast, BinOp):
		left_exp = convert_CIR(ast.left, inst_list, lambda_count)
		binop_op = str(dump(ast.op))[:-2]
		binop_sy  = ''
		if binop_op == 'Add':
			binop_sy = '+'
		elif binop_op == 'Sub':
			binop_sy = '-'
		elif binop_op == 'Mult':
			binop_sy = '*'
		elif binop_op == 'Div':
			binop_sy = '/'
		else:
			print("type = {0}".format(dump(ast.op)))
		right_exp = convert_CIR(ast.right, inst_list, lambda_count)
		return("{} {} {}".format(left_exp, binop_sy, right_exp))
	elif isinstance(ast, UnaryOp):
		if isinstance(ast.operand, Constant):
			return('-'+str(ast.operand.value))
		elif isinstance(ast.operand, Name):
			return '-'+str(ast.operand.id)
	elif isinstance(ast, Call):
		if len(ast.args) != 0:
			call_args = []
			for entry in ast.args:
				call_args.append(convert_CIR(entry, inst_list, lambda_count))
			return call_args
	elif isinstance(ast, Name):
		name_string = str(dump(ast)).split('\'')[1]
		return name_string
	elif isinstance(ast, arguments):
		if len(ast.args) != 0:
			args_list = []
			for entry in ast.args:
				args_list.append(convert_CIR(entry, inst_list, lambda_count))
			return args_list
	elif isinstance(ast, Num):
		const_num_list = re.findall(r'\d+', str(dump(ast)))
		return const_num_list[0]
	elif isinstance(ast, Str):
		return str("\"{0}\"".format(str(ast.s)[:-1]))
	elif isinstance(ast, arg):
		return_string = str(dump(ast)).split('\'')
		return return_string[1]
	elif isinstance(ast, Return):
		return ["RETURN", "return(" + str(convert_CIR(ast.value, inst_list, lambda_count))+")"]
	elif isinstance(ast, Constant):
		if ast.value == False:
			return 0
		elif ast.value == True:
			return 1
		else:
			print("Constant value not matched! {1}{0}".format(ast.value, type(ast.value)))
	elif isinstance(ast, If):

		op_sym = ""
		if isinstance(ast.test.ops[0], Gt):
			op_sym = ">"
		elif isinstance(ast.test.ops[0], Lt):
			op_sym = "<"
		elif isinstance(ast.test.ops[0], GtE):
			op_sym = ">="
		elif isinstance(ast.test.ops[0], LtE):
			op_sym = "<="
		elif isinstance(ast.test.ops[0], Eq):
			op_sym = "!="
		elif isinstance(ast.test.ops[0], NotEq):
			op_sym = "<="
		else:
			print("op type {0}\nop {1}".format(type(ast.test.ops[0], ast.test.ops[0])))
			# print("op dump {0}".format(dump(ast.test.ops)))
		if isinstance(ast.test.left, Constant):
			left_side = ast.test.left.value
		elif isinstance(ast.test.left, Name):
			left_side = ast.test.left.id
		if isinstance(ast.test.comparators[0], Constant):
			right_side = ast.test.comparators[0].value
		elif isinstance(ast.test.comparators[0], Name):
			right_side = ast.test.comparators[0].id


		then_body = []
		for entry in ast.body:
			then_body.append(convert_CIR(entry, inst_list, lambda_count))

		else_body = []
		for entry in ast.orelse:
			else_body.append(convert_CIR(entry, inst_list, lambda_count))
		return ["IF", '{0} {1} {2}'.format(left_side, op_sym, right_side), then_body, else_body]
	elif isinstance(ast, list):
		for entry in ast:
			try:
				return entry.value
			except:
				print("NO VALUE {0}".format((entry)))
			# print("value :{0}".format(entry.value))
	elif isinstance(ast, str):
			return str(ast)
		# print("str :{0}".format(ast))
			# return ["IF", '{0} {1} {2}'.format(left_side, op_sym, right_side), then_body, else_body]
			# print("list :{0}".format(entry))
	else:
		print(("CONVERT UNCAUGHT TYPE " + str(type(ast).__name__)))
		print(((ast)))
	return inst_list

def check_for_def(name, inst_list, type):
	for statement in inst_list:
		if '{1} {0} '.format(name, type) in statement:
			return True
		elif '{1} {0};'.format(name, type) in statement:
			return True
	return False

def handle_line(statement, file_lines, tabs):
	print_string = "" + ("\t"*tabs)
	needs_def = False
	if statement[0] == 'ASSIGN':
		type = 'int'
		needs_def = True if not check_for_def(statement[1].split(' = ')[0], file_lines, type) else False
		if needs_def:
			print_string += "{0} ".format(type)
		print_string += statement[1]
		print_string += " = "
		print_string += statement[2]
		print_string += ";"
		# print("Can't add : {0}".format(statement[2]))
	elif statement[0] == 'IF':
		print_string += "if ({0}){{\n".format(statement[1])
		for condition in statement[2]:
			print_string += handle_line(condition, file_lines, tabs+1)
		print_string += "\n"+ str("\t"*tabs) +"}"
		if statement[3] != []:
			print_string += " else {\n"
			else_conditions = []
			for condition in statement[3]:
				print_string += handle_line(condition, file_lines, tabs+1)
			print_string += "\n"+ str("\t"*tabs) +"}"
	else:
		print_string += statement[1]
		print_string += ";"
		# if "return(" in print_string:
		# 	print_string += "\n"
	return print_string

# def add_main(file_lines):
# 	for statement in file_lines:
# 		for x in statement()

def move_lamdas(inst_list):
	statements_to_prepend = []
	for k in range(len(inst_list)):
		if len(inst_list[k]) != 2:
			for i in range(len(inst_list[k][2])):
				if inst_list[k][2][i][0][:6]== 'lambda':
					args = inst_list[k][2][i][1]
					args_str = ""
					for arg in args:
						args_str += "int {0}".format(arg) + ", "
					args_str = args_str[:-2]
					statements_to_prepend.append(inst_list[k][2][i])
					inst_list[k][2][i] = ["CALL",  "{0}({1})".format(inst_list[k][2][i][0], args_str)]
				else:
					try:
						if inst_list[k][2][i][2][0][:6] == 'lambda':
							args = inst_list[k][2][i][2][1]
							args_str = ""
							for arg in args:
								args_str += "int {0}".format(arg) + ", "
							args_str = args_str[:-2]
							statements_to_prepend.append(inst_list[k][2][i][2])
							inst_list[k][2][i][2] = "{0}({1})".format(inst_list[k][2][i][2][0], args_str)
					except:

						continue

	for i in range(len(statements_to_prepend)):
		# print("INSERTING:{0}".format(statements_to_prepend[i]))
		inst_list.insert(i, statements_to_prepend[i])
	return inst_list

def convert_to_c(inst_list, filename):
	file_lines = []
	tabs = 0
	# print("inst list", inst_list)

	# make header
	file_lines.append("#define KBUILD_MODNAME \"{0}\"\n#include <linux/bpf.h>\n#include <linux/if_ether.h>\n#include <linux/ip.h>\n#include <linux/udp.h>\n\n".format(filename.replace(".c", "").replace(".py", "")))

	for statement in inst_list:
		print(statement)

		if len(statement) == 3:
			# print ("here", statement)
			tabs += 1
			# func_call_str = "\nint {0}(".format(statement[0]) + str(["int {0}, ".format(x) for x in statement[1]] )[2:-4].replace("', '", "")+ "):"
			
			# TODO: INTEGRATE TYPES HERE
			# handle func header
			func_call_str = "int {0}(".format(statement[0])
			arguments = ""
			if len(statement[1]) == 1 and statement[1][0] == "ctx": # very specific parameter that requires special handling
				arguments = "struct xdp_md* ctx"
			else:
				arguments = str(["int {0}, ".format(x) for x in statement[1]] )[2:-4].replace("', '", "")

			func_call_str += arguments
			func_call_str += ") {"



			# print(func_call_str)
			file_lines.append(func_call_str)
			for body_line in statement[2]:
				file_lines.append(handle_line(body_line, file_lines, tabs))
			tabs -= 1
			file_lines.append("}")
		else:
			# print("flop", statement)
			file_lines.append(handle_line(statement, file_lines, tabs))

	with open(filename, 'w') as f:
		for line in file_lines:
			# print(strline)
			f.write(line + "\n")
	return file_lines
