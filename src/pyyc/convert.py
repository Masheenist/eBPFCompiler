import re
from ast import *

def convert_CIR(ast, inst_list):
	if isinstance(ast, Module):
		for entry in ast.body:
			inst_list.append(convert_CIR(entry, inst_list))
	elif isinstance(ast, FunctionDef):
		name = ast.name
		func_args_list = convert_CIR(ast.args, inst_list)
		func_body = []
		for entry in ast.body:
			func_body.append(convert_CIR(entry, inst_list))
		return [name, func_args_list, func_body]
	elif isinstance(ast, Assign):
		if len(ast.targets) != 0:
			target_name = []
			for entry in ast.targets:
				target_name.append(convert_CIR(entry, inst_list))
		target_value = convert_CIR(ast.value, inst_list)
		return(["ASSIGN", "{} = {}".format(target_name[-1], target_value)])
	elif isinstance(ast, Expr):
		if isinstance(ast.value, Call):
			function_name = ast.value.func.id
			function_arguments = convert_CIR(ast.value, inst_list)
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
	elif isinstance(ast, BinOp):
		left_exp = convert_CIR(ast.left, inst_list)
		binop_op = str(dump(ast.op))[:-2]
		binop_sy  = ''
		if binop_op == 'Add':
			binop_sy = '+'
		right_exp = convert_CIR(ast.right, inst_list)
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
				call_args.append(convert_CIR(entry, inst_list))
			return call_args
	elif isinstance(ast, Name):
		name_string = str(dump(ast)).split('\'')[1]
		return name_string
	elif isinstance(ast, arguments):
		if len(ast.args) != 0:
			args_list = []
			for entry in ast.args:
				args_list.append(convert_CIR(entry, inst_list))
			return args_list
	elif isinstance(ast, Num):
		const_num_list = re.findall(r'\d+', str(dump(ast)))
		return const_num_list[0]
	elif isinstance(ast, Str):
		return str("\"{0}\"".format(str(ast.value)[:-2]))
	elif isinstance(ast, arg):
		return_string = str(dump(ast)).split('\'')
		return return_string[1]
	elif isinstance(ast, Return):
		return ["RETURN", "return " + str(convert_CIR(ast.value, inst_list))]
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
			then_body.append(convert_CIR(entry, inst_list))

		else_body = []
		for entry in ast.orelse:
			else_body.append(convert_CIR(entry, inst_list))
		return ["IF", '{0} {1} {2}'.format(left_side, op_sym, right_side), then_body, else_body]

	else:
		print(("CONVERT UNCAUGHT TYPE " + str(type(ast).__name__)))
		print(("\t"+ dump(ast)))
	return inst_list

def check_for_def(name, inst_list):
	for statement in inst_list:
		# print(statement)
		if 'int {0} '.format(name) in statement:
			return True
		elif 'int {0};'.format(name) in statement:
			return True
	return False

def handle_line(statement, file_lines, tabs):
	print_string = "" + ("\t"*tabs)
	needs_def = False
	if statement[0] == 'ASSIGN':
		needs_def = True if not check_for_def(statement[1].split(' = ')[0], file_lines) else False
		if needs_def:
			print_string += "int "
	if statement[0] == 'IF':
		print("FOUND IF {0}".format(statement))
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
		if "return " in print_string:
			print_string += "\n"
	return print_string

def convert_to_c(inst_list, filename):
	file_lines = []
	tabs = 0
	for statement in inst_list:
		if len(statement) == 3:
			tabs += 1
			func_call_str = "\nint {0}(".format(statement[0]) + str(["int {0}, ".format(x) for x in statement[1]] )[2:-4].replace("', '", "")+ "):"
			# print(func_call_str)
			file_lines.append(func_call_str)
			for body_line in statement[2]:
				file_lines.append(handle_line(body_line, file_lines, tabs))
			tabs -= 1
		else:
			file_lines.append(handle_line(statement, file_lines, tabs))

	with open(filename, 'w') as f:
		for line in file_lines:
			# print(strline)
			f.write(line + "\n")
	return file_lines
