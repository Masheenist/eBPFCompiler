import re
from ast import *

def convert_CIR(ast, inst_list):
	if isinstance(ast, Module):
		for entry in ast.body:
			inst_list.append(convert_CIR(entry, inst_list))
	elif isinstance(ast, FunctionDef):
		name = ast.name
		func_args_list = convert_CIR(ast.args, inst_list)

		# print("FUNCDEF_NAME: [{0}]".format(name))
		# print("FUNCDEF_ARGS: {0}".format(func_args_list))
		func_body = []
		for entry in ast.body:
			func_body.append(convert_CIR(entry, inst_list))
			# print("BODY: [{0}]".format(func_body[-1]))
		# if ast.returns:
		# 	func_body.append(str(ast.returns))
		# 	print("FUNCDEF_RETURNS: [{0}]]".format(ast.returns))
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
				# convert_CIR(entry, inst_list)
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
		# return ast.value
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
	print_string += statement[1]
	print_string += ";"
	if "return " in print_string:
		print_string += "\n"
	return print_string

def convert_to_c(inst_list, filename):
	file_lines = []
	for statement in inst_list:
		tabs = 0
		# FUNCTION - we pull out func definion, but handle body with the rest
		tabs = 0
		if len(statement) == 3:
			tabs += 1
			func_call_str = "\nint {0}(".format(statement[0]) + str(["int {0}, ".format(x) for x in statement[1]] )[2:-4].replace("', '", "")+ "):"
			# print(func_call_str)
			file_lines.append(func_call_str)
			for body_line in statement[2]:
				file_lines.append(handle_line(body_line, file_lines, tabs))
			# statement = statement[2]
		else:
			file_lines.append(handle_line(statement, file_lines, tabs))
		# # NON-FUNCTION definitions (e.g., regular code lines, or function body)
		# for item in statement[1:]:
		# 	print_string = ""
		# 	needs_def = False
		# 	if statement[0] == 'ASSIGN':
		# 		print("ITEM[0] = {0}".format(item[0]))
		# 		needs_def = True if not check_for_def(item.split(' = ')[0], file_lines) else False
		# 		if needs_def:
		# 			print_string += "int "
		# 	elif isinstance(statement[0], list):
		# 		:
		# 		print("ITEM[0] = {0}".format(item[0]))
		# 		# needs_def = True if not check_for_def(item.split(' = ')[0][1], file_lines) else False
		# 		if needs_def:
		# 			print_string += "int "
		#
		# 	if isinstance(item, str):
		# 		print_string += "\t"*tabs + item
		# 		# print(print_string)
		# 	if isinstance(item, list):
		# 		print_string += "\t"*tabs + item[1]
		# 		# print(print_string)
		# 	print_string += ";"
		# 	if "return " in print_string:
		# 		print_string += "\n"
		# 	file_lines.append(print_string)
	with open(filename, 'w') as f:
		for line in file_lines:
			# print(strline)
			f.write(line + "\n")
	return file_lines
