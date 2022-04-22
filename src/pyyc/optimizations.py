import compiler
from compiler.ast import *
from dataTypes import *
from NewDataTypes import *
import liveness

running_value_number = 1



def grab_value_number(_input, variables_to_values, values_to_variables):
	global running_value_number
	
	# if you have op var0, and var0 hasn't been defined, then var0 should get a value
	input_val = None
	if not _input in variables_to_values:
		input_val = running_value_number
		running_value_number += 1
		values_to_variables[input_val] = [_input]
		variables_to_values[_input] = input_val
	else:
		input_val = variables_to_values[_input]
	
	return input_val


def replace_in_maps(_input, input_val, new_val, variables_to_values, values_to_variables):
	# update value/variable pair in values_to_variables -> PUT THIS IN A SEPARATE FUNCTION SO YOU CAN DO CHECKS FOR WHETHER THE LISTS THAT YOU .append() AND .remove() FROM/TO EXIST
	old_val = None if not _input in variables_to_values else variables_to_values[_input]
	if not old_val == None and _input in values_to_variables[old_val]: #remove from old value binding
		values_to_variables[old_val].remove(_input)
	if not _input in values_to_variables[new_val]:
		values_to_variables[new_val].append(_input) #add to new value binding


def lvn(flattened_assembly):
	global running_value_number
	current = flattened_assembly
	
	variables_to_values = dict()
	values_to_variables = dict()
	
	while current != None:
		input1_val = None
		input2_val = None
		op_str = None

		# print "BEFORE:", current
		if current.type == "negl":
			
			# if you have negl var0, and var0 hasn't been defined, then var0 should get a value
			input1_val = grab_value_number(current.input1, variables_to_values, values_to_variables)

			# check if value of "-" var 1 in list
			op_str = "-" + str(input1_val)
			if op_str in variables_to_values:
				# if so, grab that value number
				val_of_op = variables_to_values[op_str]

				# update value/variable pair in values_to_variables 
				replace_in_maps(current.input1, input1_val, val_of_op, variables_to_values, values_to_variables)
				
				# update value for the variable
				variables_to_values[current.input1] = val_of_op

				# update instruction with liveness
				current.input1 = (current.input1, val_of_op)

			else:
				# create new number for "-var1", add "-" var 1 to list
				variables_to_values[op_str] = running_value_number

				# set var1 to new number
				variables_to_values[current.input1] = running_value_number

				# update values_to_variables with the new valuenumber
				values_to_variables[running_value_number] = [current.input1] 

				# insert number for input1
				current.input1 = (current.input1, running_value_number)

				running_value_number += 1
		

		# elif current.type == "notl":
		# 	pass

		elif current.type == "sall":
			# grab existing or create new value number for first and second arguments
			input2_val = grab_value_number(current.input2, variables_to_values, values_to_variables)
			input1_val = grab_value_number(current.input1, variables_to_values, values_to_variables)

			# check if value of var 1 "+" old value of var 2 in list
			op_str = str(input1_val) + "<<" + str(input2_val)
			op_str_flipped = str(input2_val) + "<<" + str(input1_val)
			if op_str in variables_to_values or op_str_flipped in variables_to_values:
				
				# if so, grab that value number
				if op_str in variables_to_values:
					val_of_op = variables_to_values[op_str]
				if op_str_flipped in variables_to_values:
					val_of_op = variables_to_values[op_str_flipped]
				
				# update value/variable pair in values_to_variables 
				replace_in_maps(current.input2, input2_val, val_of_op, variables_to_values, values_to_variables)
				
				# update value for the variable
				variables_to_values[current.input2] = val_of_op

				# update instruction with liveness
				current.input1 = (current.input1, input1_val)
				current.input2 = (current.input2, val_of_op)

			else:

				# add var 1 "+" old value of var 2 to list
				variables_to_values[op_str] = running_value_number

				# create new number for var2, set var2 to that in list
				variables_to_values[current.input2] = running_value_number

				# update values_to_variables with the new valuenumber
				values_to_variables[running_value_number] = [current.input2] 

				# insert numbers for input1 and input2
				current.input1 = (current.input1, input1_val)
				current.input2 = (current.input2, running_value_number)

				running_value_number += 1
		
		elif current.type == "sarl":
			# grab existing or create new value number for first and second arguments
			input2_val = grab_value_number(current.input2, variables_to_values, values_to_variables)
			input1_val = grab_value_number(current.input1, variables_to_values, values_to_variables)

			# check if value of var 1 "+" old value of var 2 in list
			op_str = str(input1_val) + ">>" + str(input2_val)
			op_str_flipped = str(input2_val) + ">>" + str(input1_val)
			if op_str in variables_to_values or op_str_flipped in variables_to_values:
				
				# if so, grab that value number
				if op_str in variables_to_values:
					val_of_op = variables_to_values[op_str]
				if op_str_flipped in variables_to_values:
					val_of_op = variables_to_values[op_str_flipped]
				
				# update value/variable pair in values_to_variables 
				replace_in_maps(current.input2, input2_val, val_of_op, variables_to_values, values_to_variables)
				
				# update value for the variable
				variables_to_values[current.input2] = val_of_op

				# update instruction with liveness
				current.input1 = (current.input1, input1_val)
				current.input2 = (current.input2, val_of_op)

			else:

				# add var 1 "+" old value of var 2 to list
				variables_to_values[op_str] = running_value_number

				# create new number for var2, set var2 to that in list
				variables_to_values[current.input2] = running_value_number

				# update values_to_variables with the new valuenumber
				values_to_variables[running_value_number] = [current.input2] 

				# insert numbers for input1 and input2
				current.input1 = (current.input1, input1_val)
				current.input2 = (current.input2, running_value_number)

				running_value_number += 1
		
		elif current.type == "andl":
			# if the variable is the stack pointer, just skip as we don't want to LVN that!
			if isinstance(current.input2, Stack):
				current = current.next
				continue
			
			# grab existing or create new value number for first and second arguments
			input2_val = grab_value_number(current.input2, variables_to_values, values_to_variables)
			input1_val = grab_value_number(current.input1, variables_to_values, values_to_variables)

			# check if value of var 1 "+" old value of var 2 in list
			op_str = str(input1_val) + "&" + str(input2_val)
			op_str_flipped = str(input2_val) + "&" + str(input1_val)
			if op_str in variables_to_values or op_str_flipped in variables_to_values:
				
				# if so, grab that value number
				if op_str in variables_to_values:
					val_of_op = variables_to_values[op_str]
				if op_str_flipped in variables_to_values:
					val_of_op = variables_to_values[op_str_flipped]
				
				# update value/variable pair in values_to_variables 
				replace_in_maps(current.input2, input2_val, val_of_op, variables_to_values, values_to_variables)
				
				# update value for the variable
				variables_to_values[current.input2] = val_of_op

				# update instruction with liveness
				current.input1 = (current.input1, input1_val)
				current.input2 = (current.input2, val_of_op)

			else:

				# add var 1 "+" old value of var 2 to list
				variables_to_values[op_str] = running_value_number

				# create new number for var2, set var2 to that in list
				variables_to_values[current.input2] = running_value_number

				# update values_to_variables with the new valuenumber
				values_to_variables[running_value_number] = [current.input2] 

				# insert numbers for input1 and input2
				current.input1 = (current.input1, input1_val)
				current.input2 = (current.input2, running_value_number)

				running_value_number += 1
		
		elif current.type == "orl":
			# if the variable is the stack pointer, just skip as we don't want to LVN that!
			if isinstance(current.input2, Stack):
				current = current.next
				continue
			
			# grab existing or create new value number for first and second arguments
			input2_val = grab_value_number(current.input2, variables_to_values, values_to_variables)
			input1_val = grab_value_number(current.input1, variables_to_values, values_to_variables)

			# check if value of var 1 "+" old value of var 2 in list
			op_str = str(input1_val) + "|" + str(input2_val)
			op_str_flipped = str(input2_val) + "|" + str(input1_val)
			if op_str in variables_to_values or op_str_flipped in variables_to_values:
				
				# if so, grab that value number
				if op_str in variables_to_values:
					val_of_op = variables_to_values[op_str]
				if op_str_flipped in variables_to_values:
					val_of_op = variables_to_values[op_str_flipped]
				
				# update value/variable pair in values_to_variables 
				replace_in_maps(current.input2, input2_val, val_of_op, variables_to_values, values_to_variables)
				
				# update value for the variable
				variables_to_values[current.input2] = val_of_op

				# update instruction with liveness
				current.input1 = (current.input1, input1_val)
				current.input2 = (current.input2, val_of_op)

			else:

				# add var 1 "+" old value of var 2 to list
				variables_to_values[op_str] = running_value_number

				# create new number for var2, set var2 to that in list
				variables_to_values[current.input2] = running_value_number

				# update values_to_variables with the new valuenumber
				values_to_variables[running_value_number] = [current.input2] 

				# insert numbers for input1 and input2
				current.input1 = (current.input1, input1_val)
				current.input2 = (current.input2, running_value_number)

				running_value_number += 1

		# elif current.type == "ret":
		# 	pass
		
		# elif current.type == "leave":
		# 	pass
		
		# elif current.type == "jmp":
		# 	pass
		

		elif current.type in ["movl", "movzbl"]:
			print current, running_value_number	

			# grab existing or create new value number for first argument
			# input2_val = grab_value_number(current.input2, variables_to_values, values_to_variables) <- will be overwritten anyways
			input1_val = grab_value_number(current.input1, variables_to_values, values_to_variables)

			# update value/variable pair in values_to_variables
			replace_in_maps(current.input2, input2_val, input1_val, variables_to_values, values_to_variables)

			# update value for the variables
			variables_to_values[current.input1] = input1_val
			variables_to_values[current.input2] = input1_val

			# replace in the instruction
			current.input1 = (current.input1, input1_val)
			current.input2 = (current.input2, input1_val)


		elif current.type == "cmpl":
			# if you have pushl var0, and var0 hasn't been defined, then var0 should get a value
			input1_val = grab_value_number(current.input1, variables_to_values, values_to_variables)
			input2_val = grab_value_number(current.input2, variables_to_values, values_to_variables)

			# update instruction with liveness; it's not being written to or anything, just read.
			current.input1 = (current.input1, input1_val)
			current.input2 = (current.input2, input2_val)
		# 	if isinstance(current.input2, Variable):
		# 		live_list.add(current.input2.name)
		# 	if isinstance(current.input1, Variable):
		# 		live_list.add(current.input1.name)


		elif current.type == "call":
			# lvn on function name/func pointer
			input1_val = grab_value_number(current.input1, variables_to_values, values_to_variables)

			# update instruction with liveness; it's not being written to or anything, just read.
			current.input1 = (current.input1, input1_val)

			# need to segment this BB from the next - recurse on next! rset running_value_number to 0.
			running_value_number = 0
			lvn(current.next)
			
			# shouldn't come back to this call and do anything
			break


		elif current.type == "addl":

			# if the variable is the stack pointer, just skip as we don't want to LVN that!
			if isinstance(current.input2, Stack):
				current = current.next
				continue
			
			# grab existing or create new value number for first and second arguments
			input2_val = grab_value_number(current.input2, variables_to_values, values_to_variables)
			input1_val = grab_value_number(current.input1, variables_to_values, values_to_variables)

			# check if value of var 1 "+" old value of var 2 in list
			op_str = str(input1_val) + "+" + str(input2_val)
			op_str_flipped = str(input2_val) + "+" + str(input1_val)
			if op_str in variables_to_values or op_str_flipped in variables_to_values:
				
				# if so, grab that value number
				if op_str in variables_to_values:
					val_of_op = variables_to_values[op_str]
				if op_str_flipped in variables_to_values:
					val_of_op = variables_to_values[op_str_flipped]
				
				# update value/variable pair in values_to_variables 
				replace_in_maps(current.input2, input2_val, val_of_op, variables_to_values, values_to_variables)
				
				# update value for the variable
				variables_to_values[current.input2] = val_of_op

				# update instruction with liveness
				current.input1 = (current.input1, input1_val)
				current.input2 = (current.input2, val_of_op)

			else:

				# add var 1 "+" old value of var 2 to list
				variables_to_values[op_str] = running_value_number

				# create new number for var2, set var2 to that in list
				variables_to_values[current.input2] = running_value_number

				# update values_to_variables with the new valuenumber
				values_to_variables[running_value_number] = [current.input2] 

				# insert numbers for input1 and input2
				current.input1 = (current.input1, input1_val)
				current.input2 = (current.input2, running_value_number)

				running_value_number += 1

		elif current.type == "sete":# if you have negl var0, and var0 hasn't been defined, then var0 should get a value
			input1_val = grab_value_number(current.input1, variables_to_values, values_to_variables)

			# check if value of "-" var 1 in list
			op_str = "sete " + str(input1_val)
			if op_str in variables_to_values:
				# if so, grab that value number
				val_of_op = variables_to_values[op_str]

				# update value/variable pair in values_to_variables 
				replace_in_maps(current.input1, input1_val, val_of_op, variables_to_values, values_to_variables)
				
				# update value for the variable
				variables_to_values[current.input1] = val_of_op

				# update instruction with liveness
				current.input1 = (current.input1, val_of_op)

			else:
				# create new number for "-var1", add "-" var 1 to list
				variables_to_values[op_str] = running_value_number

				# set var1 to new number
				variables_to_values[current.input1] = running_value_number

				# update values_to_variables with the new valuenumber
				values_to_variables[running_value_number] = [current.input1] 

				# insert number for input1
				current.input1 = (current.input1, running_value_number)

				running_value_number += 1
		
		elif current.type == "setne":
			input1_val = grab_value_number(current.input1, variables_to_values, values_to_variables)

			# check if value of "-" var 1 in list
			op_str = "setne " + str(input1_val)
			if op_str in variables_to_values:
				# if so, grab that value number
				val_of_op = variables_to_values[op_str]

				# update value/variable pair in values_to_variables 
				replace_in_maps(current.input1, input1_val, val_of_op, variables_to_values, values_to_variables)
				
				# update value for the variable
				variables_to_values[current.input1] = val_of_op

				# update instruction with liveness
				current.input1 = (current.input1, val_of_op)

			else:
				# create new number for "-var1", add "-" var 1 to list
				variables_to_values[op_str] = running_value_number

				# set var1 to new number
				variables_to_values[current.input1] = running_value_number

				# update values_to_variables with the new valuenumber
				values_to_variables[running_value_number] = [current.input1] 

				# insert number for input1
				current.input1 = (current.input1, running_value_number)

				running_value_number += 1
		
		# elif current.type == "orl":
		# 	if isinstance(current.input1, Variable):
		# 		live_list.add(current.input1.name)
		
		elif current.type == "pushl":
			
			# if you have pushl var0, and var0 hasn't been defined, then var0 should get a value
			input1_val = grab_value_number(current.input1, variables_to_values, values_to_variables)

			# update instruction with liveness; it's not being written to or anything, just read.
			current.input1 = (current.input1, input1_val)

		
		elif current.type == "IfExp":
			# handle the variable in test (this is input1), and in output (this is input2) -> ASK ABOUT THIS.
			input1_val = grab_value_number(current.input1, variables_to_values, values_to_variables)
			input2_val = grab_value_number(current.input2, variables_to_values, values_to_variables)

			# having done this, update in the instruction with lvns
			current.input1 = (current.input1, input1_val)
			current.input2 = (current.input2, input2_val)

			# now recurse on thenNext and elseNext. keep resetting running_value_number to 0, as we enter a new BB
			running_value_number = 0
			lvn(current.thenNext)

			running_value_number = 0
			lvn(current.elseNext)

			# everything after this if is a new BB. reset all.
			running_value_number = 0
			variables_to_values = dict()
			values_to_variables = dict()

		elif current.type == "While":
			# handle the variable in test (this is input1), and in output (this is input2) -> ASK ABOUT THIS.
			input1_val = grab_value_number(current.input1, variables_to_values, values_to_variables)
			input2_val = grab_value_number(current.input2, variables_to_values, values_to_variables)

			# having done this, update in the instruction with lvns
			current.input1 = (current.input1, input1_val)
			current.input2 = (current.input2, input2_val)

			# now recurse on thenNext and elseNext. keep resetting running_value_number to 0, as we enter a new BB
			running_value_number = 0
			lvn(current.thenNext)

			running_value_number = 0
			lvn(current.elseNext)

			# everything after this if is a new BB. reset all.
			running_value_number = 0
			variables_to_values = dict()
			values_to_variables = dict()

		elif current.type == "jmp":
			# like a return
			pass
		
		else:
			raise Exception("No instruction match: " + str(current.type))
		
		# print "AFTER:", current, "\n", "variables_to_values", variables_to_values, "\n", "values_to_variables", values_to_variables, "\n"#, "constants_to_variables", constants_to_variables, "\n", "variables_to_constants", variables_to_constants, "\n"
		current = current.next
	return flattened_assembly #get_first(current)


def copy_folding(live_assembly):

	# need a dict mapping value numbers that have been defined in the basic block to their variable. 
	# EACH VARIABLE HAS ONLY 1 VALUE AT A TIME BUT EACH VALUE CAN HAVE MULTIPLE VARIABLES
	currently_live = dict()
	
	current = live_assembly
	while current != None:
		# print "BEFORE:", current

		if current.type == "negl":
			print current.input1[1], currently_live

			# current.input[1] is the value the variable has after it gets negated.
			if current.input1[1] in currently_live:
				# if we have "negl var1", and var1's lvn already has a variable (say, var0), then we want this to be "movl var0, var1"
				# get rid of old value-key binding. this variable will only show up bound to 1 value, so find that value, then remove it from the list
				for k in currently_live.keys():
					# if we have found a key that contains the variable
					if current.input1[0] in currently_live[k]:

						# remove it from the list
						currently_live[k].remove(current.input1[0])

						# if list is empty after removing this element
						if len(currently_live[k]) == 0:
							# pop this key
							currently_live.pop(k)
						break

				# add variable to list corresponding to the new value
				currently_live[current.input1[1]].append(current.input1[0])

				# grab new value
				current.type = "movl"
				existing_var_with_value = currently_live[current.input1[1]][0]
				current.input2 = current.input1
				current.input1 = (existing_var_with_value, current.input1[1])

			else:
				# get rid of old value-key binding. this variable will only show up bound to 1 value, so find that value, then remove it from the list
				for k in currently_live.keys():
					# if we have found a key that contains the variable
					if current.input1[0] in currently_live[k]:

						# remove it from the list
						currently_live[k].remove(current.input1[0])

						# if list is empty after removing this element
						if len(currently_live[k]) == 0:
							# pop this key
							currently_live.pop(k)
						break

				# make a new list for this value number as it doesn't exist yet
				currently_live[current.input1[1]] = [current.input1[0]]
		

		# elif current.type == "notl":
		# 	pass

		elif current.type == "sall":

			print current.input2[1], currently_live

			if current.input2[1] in currently_live:
				# if we have "negl var1", and var1's lvn already has a variable (say, var0), then we want this to be "movl var0, var1"
				# get rid of old value-key binding. this variable will only show up bound to 1 value, so find that value, then remove it from the list
				for k in currently_live.keys():
					# if we have found a key that contains the variable
					if current.input2[0] in currently_live[k]:

						# remove it from the list
						currently_live[k].remove(current.input2[0])

						# if list is empty after removing this element
						if len(currently_live[k]) == 0:
							# pop this key
							currently_live.pop(k)
						break

				# add variable to list corresponding to the new value
				currently_live[current.input2[1]].append(current.input2[0])

				# grab new value
				current.type = "movl"
				existing_var_with_value = currently_live[current.input2[1]][0]
				current.input2 = current.input2
				current.input1 = (existing_var_with_value, current.input2[1])
			else:
				# get rid of old value-key binding. this variable will only show up bound to 1 value, so find that value, then remove it from the list
				for k in currently_live.keys():
					# if we have found a key that contains the variable
					if current.input2[0] in currently_live[k]:

						# remove it from the list
						currently_live[k].remove(current.input2[0])

						# if list is empty after removing this element
						if len(currently_live[k]) == 0:
							# pop this key
							currently_live.pop(k)
						break

				# make a new one
				currently_live[current.input2[1]] = [current.input2[0]]
		
		elif current.type == "sarl":

			print current.input2[1], currently_live

			if current.input2[1] in currently_live:
				# if we have "negl var1", and var1's lvn already has a variable (say, var0), then we want this to be "movl var0, var1"
				# get rid of old value-key binding. this variable will only show up bound to 1 value, so find that value, then remove it from the list
				for k in currently_live.keys():
					# if we have found a key that contains the variable
					if current.input2[0] in currently_live[k]:

						# remove it from the list
						currently_live[k].remove(current.input2[0])

						# if list is empty after removing this element
						if len(currently_live[k]) == 0:
							# pop this key
							currently_live.pop(k)
						break

				# add variable to list corresponding to the new value
				currently_live[current.input2[1]].append(current.input2[0])

				# grab new value
				current.type = "movl"
				existing_var_with_value = currently_live[current.input2[1]][0]
				current.input2 = current.input2
				current.input1 = (existing_var_with_value, current.input2[1])
			else:
				# get rid of old value-key binding. this variable will only show up bound to 1 value, so find that value, then remove it from the list
				for k in currently_live.keys():
					# if we have found a key that contains the variable
					if current.input2[0] in currently_live[k]:

						# remove it from the list
						currently_live[k].remove(current.input2[0])

						# if list is empty after removing this element
						if len(currently_live[k]) == 0:
							# pop this key
							currently_live.pop(k)
						break

				# make a new one
				currently_live[current.input2[1]] = [current.input2[0]]
		
		# elif current.type == "andl":
		# 	pass

		elif current.type == "cmpl":
			pass

		elif current.type == "sete":
			print current.input1[1], currently_live

			# current.input[1] is the value the variable has after it gets negated.
			if current.input1[1] in currently_live:
				# if we have "negl var1", and var1's lvn already has a variable (say, var0), then we want this to be "movl var0, var1"
				# get rid of old value-key binding. this variable will only show up bound to 1 value, so find that value, then remove it from the list
				for k in currently_live.keys():
					# if we have found a key that contains the variable
					if current.input1[0] in currently_live[k]:

						# remove it from the list
						currently_live[k].remove(current.input1[0])

						# if list is empty after removing this element
						if len(currently_live[k]) == 0:
							# pop this key
							currently_live.pop(k)
						break

				# add variable to list corresponding to the new value
				currently_live[current.input1[1]].append(current.input1[0])

				# grab new value
				current.type = "movl"
				existing_var_with_value = currently_live[current.input1[1]][0]
				current.input2 = current.input1
				current.input1 = (existing_var_with_value, current.input1[1])

			else:
				# get rid of old value-key binding. this variable will only show up bound to 1 value, so find that value, then remove it from the list
				for k in currently_live.keys():
					# if we have found a key that contains the variable
					if current.input1[0] in currently_live[k]:

						# remove it from the list
						currently_live[k].remove(current.input1[0])

						# if list is empty after removing this element
						if len(currently_live[k]) == 0:
							# pop this key
							currently_live.pop(k)
						break

				# make a new list for this value number as it doesn't exist yet
				currently_live[current.input1[1]] = [current.input1[0]]

		elif current.type == "setne":
			print current.input1[1], currently_live

			# current.input[1] is the value the variable has after it gets negated.
			if current.input1[1] in currently_live:
				# if we have "negl var1", and var1's lvn already has a variable (say, var0), then we want this to be "movl var0, var1"
				# get rid of old value-key binding. this variable will only show up bound to 1 value, so find that value, then remove it from the list
				for k in currently_live.keys():
					# if we have found a key that contains the variable
					if current.input1[0] in currently_live[k]:

						# remove it from the list
						currently_live[k].remove(current.input1[0])

						# if list is empty after removing this element
						if len(currently_live[k]) == 0:
							# pop this key
							currently_live.pop(k)
						break

				# add variable to list corresponding to the new value
				currently_live[current.input1[1]].append(current.input1[0])

				# grab new value
				current.type = "movl"
				existing_var_with_value = currently_live[current.input1[1]][0]
				current.input2 = current.input1
				current.input1 = (existing_var_with_value, current.input1[1])

			else:
				# get rid of old value-key binding. this variable will only show up bound to 1 value, so find that value, then remove it from the list
				for k in currently_live.keys():
					# if we have found a key that contains the variable
					if current.input1[0] in currently_live[k]:

						# remove it from the list
						currently_live[k].remove(current.input1[0])

						# if list is empty after removing this element
						if len(currently_live[k]) == 0:
							# pop this key
							currently_live.pop(k)
						break

				# make a new list for this value number as it doesn't exist yet
				currently_live[current.input1[1]] = [current.input1[0]]
			pass
		
		# elif current.type == "ret":
		# 	pass
		
		# elif current.type == "leave":
		# 	pass
		
		# elif current.type == "jmp":
		# 	pass
		

		elif current.type in ["movl", "movzbl"]:	
			# update currently_live with the variable name and its liveness. current.input1[0] -> Variable(@), current.input1[1] -> lvn#
			# get rid of old value-key binding. this variable will only show up bound to 1 value, so find that value, then remove it from the list
			for k in currently_live.keys():
				# if we have found a key that contains the variable
				if current.input2[0] in currently_live[k]:

					# remove it from the list
					currently_live[k].remove(current.input2[0])

					# if list is empty after removing this element
					if len(currently_live[k]) == 0:
						# pop this key
						currently_live.pop(k)
					break

			# make a new list for this value number as it doesn't exist yet
			if current.input2[1] in currently_live:
				currently_live[current.input2[1]].append(current.input2[0])
			else:
				currently_live[current.input2[1]] = [current.input2[0]]
			
			# repeat for var1 as its possible and valid that this mov is its first occurrence
			# get rid of old value-key binding. this variable will only show up bound to 1 value, so find that value, then remove it from the list
			for k in currently_live.keys():
				# if we have found a key that contains the variable
				if current.input1[0] in currently_live[k]:

					# remove it from the list
					currently_live[k].remove(current.input1[0])

					# if list is empty after removing this element
					if len(currently_live[k]) == 0:
						# pop this key
						currently_live.pop(k)
					break

			# make a new list for this value number as it doesn't exist yet
			if current.input1[1] in currently_live:
				currently_live[current.input1[1]].append(current.input1[0])
			else:
				currently_live[current.input1[1]] = [current.input1[0]]


		# elif current.type == "cmpl":
		# 	if isinstance(current.input2, Variable):
		# 		live_list.add(current.input2.name)
		# 	if isinstance(current.input1, Variable):
		# 		live_list.add(current.input1.name)


		elif current.type == "call":
			# replace value of input1 with existing value if it already exists
			print current
			if current.input1[1] in currently_live:
				existing_var_with_value = currently_live[current.input1[1]][0]
				current.input1 = (existing_var_with_value, current.input1[1])

			# and then recurse!
			copy_folding(current.next)
			break


		elif current.type == "addl":
			if isinstance(current.input2, Stack):
				current = current.next
				continue

			print current.input2[1], currently_live

			if current.input2[1] in currently_live:
				# if we have "negl var1", and var1's lvn already has a variable (say, var0), then we want this to be "movl var0, var1"
				# get rid of old value-key binding. this variable will only show up bound to 1 value, so find that value, then remove it from the list
				for k in currently_live.keys():
					# if we have found a key that contains the variable
					if current.input2[0] in currently_live[k]:

						# remove it from the list
						currently_live[k].remove(current.input2[0])

						# if list is empty after removing this element
						if len(currently_live[k]) == 0:
							# pop this key
							currently_live.pop(k)
						break

				# add variable to list corresponding to the new value
				currently_live[current.input2[1]].append(current.input2[0])

				# grab new value
				current.type = "movl"
				existing_var_with_value = currently_live[current.input2[1]][0]
				current.input2 = current.input2
				current.input1 = (existing_var_with_value, current.input2[1])
			else:
				# get rid of old value-key binding. this variable will only show up bound to 1 value, so find that value, then remove it from the list
				for k in currently_live.keys():
					# if we have found a key that contains the variable
					if current.input2[0] in currently_live[k]:

						# remove it from the list
						currently_live[k].remove(current.input2[0])

						# if list is empty after removing this element
						if len(currently_live[k]) == 0:
							# pop this key
							currently_live.pop(k)
						break

				# make a new one
				currently_live[current.input2[1]] = [current.input2[0]]

		elif current.type == "andl":

			print current.input2[1], currently_live

			if current.input2[1] in currently_live:
				# if we have "negl var1", and var1's lvn already has a variable (say, var0), then we want this to be "movl var0, var1"
				# get rid of old value-key binding. this variable will only show up bound to 1 value, so find that value, then remove it from the list
				for k in currently_live.keys():
					# if we have found a key that contains the variable
					if current.input2[0] in currently_live[k]:

						# remove it from the list
						currently_live[k].remove(current.input2[0])

						# if list is empty after removing this element
						if len(currently_live[k]) == 0:
							# pop this key
							currently_live.pop(k)
						break

				# add variable to list corresponding to the new value
				currently_live[current.input2[1]].append(current.input2[0])

				# grab new value
				current.type = "movl"
				existing_var_with_value = currently_live[current.input2[1]][0]
				current.input2 = current.input2
				current.input1 = (existing_var_with_value, current.input2[1])
			else:
				# get rid of old value-key binding. this variable will only show up bound to 1 value, so find that value, then remove it from the list
				for k in currently_live.keys():
					# if we have found a key that contains the variable
					if current.input2[0] in currently_live[k]:

						# remove it from the list
						currently_live[k].remove(current.input2[0])

						# if list is empty after removing this element
						if len(currently_live[k]) == 0:
							# pop this key
							currently_live.pop(k)
						break

				# make a new one
				currently_live[current.input2[1]] = [current.input2[0]]

		elif current.type == "orl":
			if isinstance(current.input2, Stack):
				current = current.next
				continue

			if current.input2[1] in currently_live:
				# if we have "negl var1", and var1's lvn already has a variable (say, var0), then we want this to be "movl var0, var1"
				# get rid of old value-key binding. this variable will only show up bound to 1 value, so find that value, then remove it from the list
				for k in currently_live.keys():
					# if we have found a key that contains the variable
					if current.input2[0] in currently_live[k]:

						# remove it from the list
						currently_live[k].remove(current.input2[0])

						# if list is empty after removing this element
						if len(currently_live[k]) == 0:
							# pop this key
							currently_live.pop(k)
						break

				# add variable to list corresponding to the new value
				currently_live[current.input2[1]].append(current.input2[0])

				# grab new value
				current.type = "movl"
				existing_var_with_value = currently_live[current.input2[1]][0]
				current.input2 = current.input2
				current.input1 = (existing_var_with_value, current.input2[1])
			else:
				# get rid of old value-key binding. this variable will only show up bound to 1 value, so find that value, then remove it from the list
				for k in currently_live.keys():
					# if we have found a key that contains the variable
					if current.input2[0] in currently_live[k]:

						# remove it from the list
						currently_live[k].remove(current.input2[0])

						# if list is empty after removing this element
						if len(currently_live[k]) == 0:
							# pop this key
							currently_live.pop(k)
						break

				# make a new one
				currently_live[current.input2[1]] = [current.input2[0]]

		# elif current.type == "sete":
		# 	if isinstance(current.input1, Variable):
		# 		live_list.discard(current.input1.name)
		
		# elif current.type == "setne":
		# 	if isinstance(current.input1, Variable):
		# 		live_list.discard(current.input1.name)
		
		# elif current.type == "orl":
		# 	if isinstance(current.input1, Variable):
		# 		live_list.add(current.input1.name)
		
		elif current.type == "pushl":
			# replace value of input1 with existing value if it already exists
			if current.input1[1] in currently_live:
				existing_var_with_value = currently_live[current.input1[1]][0]
				current.input1 = (existing_var_with_value, current.input1[1])
			
		
		elif current.type == "IfExp":
			# replace value of input1 with existing value if it already exists
			if current.input1[1] in currently_live:
				existing_var_with_value = currently_live[current.input1[1]][0]
				current.input1 = (existing_var_with_value, current.input1[1])

			# and then recurse!
			copy_folding(current.thenNext)
			copy_folding(current.elseNext)

			# now, we will enter a new BB, so reset any structs:
			currently_live = dict()

		elif current.type == "While":
			# replace value of input1 with existing value if it already exists
			if current.input1[1] in currently_live:
				existing_var_with_value = currently_live[current.input1[1]][0]
				current.input1 = (existing_var_with_value, current.input1[1])

			# and then recurse!
			copy_folding(current.thenNext)
			copy_folding(current.elseNext)

			# now, we will enter a new BB, so reset any structs:
			currently_live = dict()

		elif current.type == "jmp":
			# like a return
			pass

		else:
			raise Exception("No instruction match: " + str(current.type))

		# print "AFTER:", current, "currently_live", currently_live, "\n"
		current = current.next

	return live_assembly #get_first(current)


def constant_folding(live_assembly):
	
	current = live_assembly
	
	variables_to_constants = dict()
	# constants_to_variables = dict()

	current = live_assembly
	while current != None:
		# print "BEFORE:", current

		if current.type == "negl":
			# if input1 is a constant, simply update its value
			if current.input1[0] in variables_to_constants:
				const_val = variables_to_constants[current.input1[0]]
				variables_to_constants[current.input1[0]] = -const_val
	

		# elif current.type == "notl":
		# 	pass

		elif current.type == "sall":
			if isinstance(current.input2, Stack):
				current = current.next
				continue

			# can only act on input2 if it is a constant in the map
			# but you can also replace input1 if it maps to a constant
			if current.input1[0] in variables_to_constants:
				const_val = variables_to_constants[current.input1[0]]
				current.input1 = (const_val, current.input1[1])
			
			# now, will either be of form "addl const, var" or "addl var, var". 
			# if its the former, check if var is in map and if so make this a movl and map to the new, sum constant but if not do nothing. 
			if not isinstance(current.input1[0], Variable) and current.input2[0] in variables_to_constants:
				input2_val = variables_to_constants[current.input2[0]]
				sum_val = input2_val << current.input1[0]

				current.type = "movl"
				current.input1 = (sum_val, current.input2[1]) # has to have input2's lvn
				variables_to_constants[current.input2[0]] = sum_val
			else:
				# if its the latter, make sure its no longer in the constant map.
				if current.input2[0] in variables_to_constants:
					variables_to_constants.pop(current.input2[0]) 
		
		elif current.type == "sarl":
			if isinstance(current.input2, Stack):
				current = current.next
				continue

			# can only act on input2 if it is a constant in the map
			# but you can also replace input1 if it maps to a constant
			if current.input1[0] in variables_to_constants:
				const_val = variables_to_constants[current.input1[0]]
				current.input1 = (const_val, current.input1[1])
			
			# now, will either be of form "addl const, var" or "addl var, var". 
			# if its the former, check if var is in map and if so make this a movl and map to the new, sum constant but if not do nothing. 
			if not isinstance(current.input1[0], Variable) and current.input2[0] in variables_to_constants:
				input2_val = variables_to_constants[current.input2[0]]
				sum_val = input2_val >> current.input1[0]

				current.type = "movl"
				current.input1 = (sum_val, current.input2[1]) # has to have input2's lvn
				variables_to_constants[current.input2[0]] = sum_val
			else:
				# if its the latter, make sure its no longer in the constant map.
				if current.input2[0] in variables_to_constants:
					variables_to_constants.pop(current.input2[0]) 
		
		# elif current.type == "andl":
		# 	pass
		
		# elif current.type == "ret":
		# 	pass
		
		# elif current.type == "leave":
		# 	pass
		
		# elif current.type == "jmp":
		# 	pass
		

		elif current.type in ["movl", "movzbl"]:	
			if not isinstance(current.input1[0], Variable): #it is a constant.
				# update mapping - the variable input2[0] should map to this constant
				variables_to_constants[current.input2[0]] = current.input1[0]

			else:
				# check if input1 is a constant in the mapping, if so, replace
				if current.input1[0] in variables_to_constants:
					const_val = variables_to_constants[current.input1[0]]
					current.input1 = (const_val, current.input1[1])
					variables_to_constants[current.input2[0]] = const_val
				
				# if not, make sure that input2 is not mapped to a constant anymore
				else:
					if current.input2[0] in variables_to_constants:
						variables_to_constants.pop(current.input2[0]) 


		elif current.type == "cmpl":
			pass

		elif current.type == "sete":
			pass

		elif current.type == "setne":
			pass


		elif current.type == "call":
			# function name cannot be a constant, so no folding. just segment.
			copy_folding(current.next)
			break


		elif current.type == "addl":
			if isinstance(current.input2, Stack):
				current = current.next
				continue

			# can only act on input2 if it is a constant in the map
			# but you can also replace input1 if it maps to a constant
			if current.input1[0] in variables_to_constants:
				const_val = variables_to_constants[current.input1[0]]
				current.input1 = (const_val, current.input1[1])
			
			# now, will either be of form "addl const, var" or "addl var, var". 
			# if its the former, check if var is in map and if so make this a movl and map to the new, sum constant but if not do nothing. 
			if not isinstance(current.input1[0], Variable) and current.input2[0] in variables_to_constants:
				input2_val = variables_to_constants[current.input2[0]]
				sum_val = input2_val + current.input1[0]

				current.type = "movl"
				current.input1 = (sum_val, current.input2[1]) # has to have input2's lvn
				variables_to_constants[current.input2[0]] = sum_val
			else:
				# if its the latter, make sure its no longer in the constant map.
				if current.input2[0] in variables_to_constants:
					variables_to_constants.pop(current.input2[0]) 
		

		elif current.type == "andl":

			# can only act on input2 if it is a constant in the map
			# but you can also replace input1 if it maps to a constant
			if current.input1[0] in variables_to_constants:
				const_val = variables_to_constants[current.input1[0]]
				current.input1 = (const_val, current.input1[1])
			
			# now, will either be of form "addl const, var" or "addl var, var". 
			# if its the former, check if var is in map and if so make this a movl and map to the new, sum constant but if not do nothing. 
			if not isinstance(current.input1[0], Variable) and current.input2[0] in variables_to_constants:
				input2_val = variables_to_constants[current.input2[0]]
				sum_val = input2_val & current.input1[0]

				current.type = "movl"
				current.input1 = (sum_val, current.input2[1]) # has to have input2's lvn
				variables_to_constants[current.input2[0]] = sum_val
			else:
				# if its the latter, make sure its no longer in the constant map.
				if current.input2[0] in variables_to_constants:
					variables_to_constants.pop(current.input2[0]) 


		elif current.type == "orl":

			# can only act on input2 if it is a constant in the map
			# but you can also replace input1 if it maps to a constant
			if current.input1[0] in variables_to_constants:
				const_val = variables_to_constants[current.input1[0]]
				current.input1 = (const_val, current.input1[1])
			
			# now, will either be of form "addl const, var" or "addl var, var". 
			# if its the former, check if var is in map and if so make this a movl and map to the new, sum constant but if not do nothing. 
			if not isinstance(current.input1[0], Variable) and current.input2[0] in variables_to_constants:
				input2_val = variables_to_constants[current.input2[0]]
				sum_val = input2_val | current.input1[0]

				current.type = "movl"
				current.input1 = (sum_val, current.input2[1]) # has to have input2's lvn
				variables_to_constants[current.input2[0]] = sum_val
			else:
				# if its the latter, make sure its no longer in the constant map.
				if current.input2[0] in variables_to_constants:
					variables_to_constants.pop(current.input2[0]) 
			

		# elif current.type == "sete":
		# 	if isinstance(current.input1, Variable):
		# 		live_list.discard(current.input1.name)
		
		# elif current.type == "setne":
		# 	if isinstance(current.input1, Variable):
		# 		live_list.discard(current.input1.name)
		
		# elif current.type == "orl":
		# 	if isinstance(current.input1, Variable):
		# 		live_list.add(current.input1.name)
		
		elif current.type == "pushl":
			# replace input1 if it maps to a constant
			if current.input1[0] in variables_to_constants:
				const_val = variables_to_constants[current.input1[0]]
				current.input1 = (const_val, current.input1[1])
		
		elif current.type == "IfExp":
			# DO NOT DO THIS. IT WILL CAUSE A SEGFAULT, CAN'T CMPL A CONSTANT # replace input1 if it maps to a constant
			# if current.input1[0] in variables_to_constants:
			# 	const_val = variables_to_constants[current.input1[0]]
			# 	current.input1 = (const_val, current.input1[1])

			# and then recurse!
			constant_folding(current.thenNext)

			# now, we will enter a new BB, so reset any structs:
			variables_to_constants = dict()

		elif current.type == "While":
			# DO NOT DO THIS. IT WILL CAUSE A SEGFAULT, CAN'T CMPL A CONSTANT # replace input1 if it maps to a constant
			# if current.input1[0] in variables_to_constants:
			# 	const_val = variables_to_constants[current.input1[0]]
			# 	current.input1 = (const_val, current.input1[1])

			# and then recurse!
			constant_folding(current.thenNext)
			constant_folding(current.elseNext)

			# now, we will enter a new BB, so reset any structs:
			variables_to_constants = dict()
		
		elif current.type == "jmp":
			# like a return
			pass

		else:
			raise Exception("No instruction match: " + str(current.type))

		# print "AFTER:", current, "variables_to_constants", variables_to_constants, "\n"
		current = current.next

	return live_assembly #get_first(current)


# every variable is a tuple (Variable(@), value#), we just want Variable(@)
def make_compatible(optimized_assembly):
	current = optimized_assembly
	while current != None:
		if current.type == "negl":	
			current.input1 = current.input1[0]
		
		# elif current.type == "notl":
		# 	pass

		elif current.type == "sall":
			current.input1 = current.input1[0]	
			current.input2 = current.input2[0]
		
		elif current.type == "sarl":
			current.input1 = current.input1[0]	
			current.input2 = current.input2[0]
		
		# elif current.type == "andl":
		# 	pass
		
		# elif current.type == "ret":
		# 	pass
		
		# elif current.type == "leave":
		# 	pass
		
		# elif current.type == "jmp":
		# 	pass
		
		elif current.type in ["movl", "movzbl"]:	
			current.input1 = current.input1[0]	
			current.input2 = current.input2[0]

		elif current.type == "addl":	
			if not isinstance(current.input2, Stack):
				current.input1 = current.input1[0]	
				current.input2 = current.input2[0]

		elif current.type == "andl":	
			if not isinstance(current.input2, Stack):
				current.input1 = current.input1[0]	
				current.input2 = current.input2[0]

		elif current.type == "orl":	
			if not isinstance(current.input2, Stack):
				current.input1 = current.input1[0]	
				current.input2 = current.input2[0]
			
		elif current.type == "cmpl":
			if not isinstance(current.input2, Stack):
				current.input1 = current.input1[0]	
				current.input2 = current.input2[0]

		elif current.type == "sete":
			if not isinstance(current.input2, Stack):
				current.input1 = current.input1[0]
		
		elif current.type == "setne":
			if not isinstance(current.input2, Stack):
				current.input1 = current.input1[0]
		
		elif current.type == "pushl":
			current.input1 = current.input1[0]

		elif current.type == "call":
			current.input1 = current.input1[0]

			make_compatible(current.next)
			break
		
		elif current.type == "IfExp":	
			current.input1 = current.input1[0]	
			current.input2 = current.input2[0]

			make_compatible(current.thenNext)
			make_compatible(current.elseNext)

		elif current.type == "While":	
			current.input1 = current.input1[0]	
			current.input2 = current.input2[0]
			print "COMPATIBLE WHILE:", current.input1, current.input2

			make_compatible(current.thenNext)
			make_compatible(current.elseNext)

		elif current.type == "jmp":
			# like a return
			pass
		
		else:
			raise Exception("No instruction match: " + str(current.type))
		
		current = current.next
	return optimized_assembly #get_first(current)


def remove_node(node):
	mynext = node.next
	myprev = node.prev

	if mynext != None:
		mynext.prev = myprev
	if myprev != None:
		myprev.next = mynext
	
	del node

def dse_liveness(flattened_assembly, live_list):
	current = get_last(flattened_assembly)
	current.liveness = set(live_list)
	# print current
	# live_list = live
	while current != None:
		current.liveness = set(live_list)
		if current.type == "negl":
			pass
		elif current.type == "notl":
			pass
		elif current.type == "sall":
			pass
		elif current.type == "sarl":
			pass
		elif current.type == "andl":
			pass
		elif current.type == "orl":
			pass
		elif current.type == "ret":
			pass
		elif current.type == "leave":
			pass
		elif current.type == "jmp":
			pass
		elif current.type in ["movl", "movzbl"]:
			if isinstance(current.input2, Variable):
				live_list.discard(current.input2.name)
			if isinstance(current.input1, Variable):
				live_list.add(current.input1.name)
		elif current.type == "cmpl":
			if isinstance(current.input2, Variable):
				live_list.add(current.input2.name)
			if isinstance(current.input1, Variable):
				live_list.add(current.input1.name)
		elif current.type == "call":
			live_list.discard("eax")
			live_list.discard("ecx")
			live_list.discard("edx")
			if isinstance(current.input1, Variable):
				live_list.add(current.input1.name)
		elif current.type == "addl":
			if isinstance(current.input1, Variable):
				live_list.add(current.input1.name)
			if isinstance(current.input2, Variable):
				live_list.add(current.input2.name)
		elif current.type == "sete":
			if isinstance(current.input1, Variable):
				live_list.discard(current.input1.name)
		elif current.type == "setne":
			if isinstance(current.input1, Variable):
				live_list.discard(current.input1.name)
		elif current.type == "orl":
			if isinstance(current.input1, Variable):
				live_list.add(current.input1.name)
		elif current.type == "pushl":
			if isinstance(current.input1, Variable):
				live_list.add(current.input1.name)
		elif current.type == "IfExp":
			saved_livelist = set([x for x in live_list])
			# print "at if, live_list is:", live_list
			then = dse_liveness(current.thenNext, live_list)
			# print "finished then, live_list is:", saved_livelist
			elsex = dse_liveness(current.elseNext, saved_livelist)
			live_list = then | elsex
		elif current.type== "While":
			new_live = set(live_list)
			loopLive = set([])
			old_live = None
			while True:
				live_list = new_live | loopLive
				if isinstance(current.input1, Variable):
					live_list.add(current.input1.name)
				live_list = dse_liveness(current.elseNext, live_list)
				if old_live == live_list:
					break
				old_live = set(live_list)
				loopLive = dse_liveness(current.thenNext, live_list)
		else:
			raise Exception("No instruction match: " + str(current.type))
		current = current.prev
	return live_list


def dead_store_elim(compatible_assembly, global_root):
	# runs in a loop, computing liveness, i.e. FP iteration.
	# the liveness set you pass to it as a parameter is what's live at the end, so in there you put any callfuncs or the stuff marked as live propogated upwards from a loop/if...see how rhett handles liveness with ifs and callfuncs
	
	# you'll need a custom liveness for this that just analyzes it for basic blocks, and then at a callfunc or whatever you segment a basic block off, create that live set off what was being called, and then get the liveness for the BB
	modified = True
	
	itercount = 0
	
	dse_liveness(global_root, set([]))

	# print "---", itercount, "---"
	# current = compatible_assembly
	# while current != None:
	# 	print current
	# 	current = current.next
	# print '\n\n\n'

	while modified:
		# set it to True only if you modify, as it's unclear how to tell when to set it to False
		modified = False

		#compute the liveness
		dse_liveness(global_root, set([]))
		# print "---"
		# print_linked_list_new(compatible_assembly)
		# print "---\n\n"

		#iterate through the instructions, if you have to remove, then modified = True
		current = compatible_assembly
		while current != None:
			# check if target is in live set, if not, remove this node.

			if current.type == "negl" and not current.input1.name in current.liveness:	
				if current.next == None and current.prev == None:
					compatible_assembly = None	
					current = None
				else:
					remove_node(current)
				modified = True
			
			# elif current.type == "notl":
			# 	pass

			elif current.type == "sall":
				pass
			
			elif current.type == "sarl":
				pass
			
			# elif current.type == "andl":
			# 	pass
			
			# elif current.type == "ret":
			# 	pass
			
			# elif current.type == "leave":
			# 	pass
			
			# elif current.type == "jmp":
			# 	pass
			
			elif current.type in ["movl", "movzbl"] and not current.input2.name in current.liveness:
				# print current, "TARGET FOUND", current.prev
				if current.next == None and current.prev == None:
					compatible_assembly = None	
					current = None
				else:
					if not current.next == None:
						# if the head
						if current.prev == None:
							compatible_assembly = current.next
						remove_node(current)

						

				modified = True
			
			elif current.type == "addl" and not current.input2.name in current.liveness:
				if isinstance(current.input2, Stack):
					current = current.next
					continue
				if current.next == None and current.prev == None:
					compatible_assembly = None	
					current = None
				else:
					remove_node(current)

					# if the head
					if current.prev == None:
						compatible_assembly = current.next

				modified = True
				

			# elif current.type == "sete":
			# 	if isinstance(current.input1, Variable):
			# 		live_list.discard(current.input1.name)
			
			# elif current.type == "setne":
			# 	if isinstance(current.input1, Variable):
			# 		live_list.discard(current.input1.name)
			
			# elif current.type == "orl":
			# 	if isinstance(current.input1, Variable):
			# 		live_list.add(current.input1.name)
			
			elif current.type == "pushl":
				# just reading, not storing. so no dse. but do need to recurse.
				pass

			elif current.type == "call":
				# just reading, not storing. so no dse. but do need to recurse.
				dead_store_elim(current.next, global_root) # should have its own scope and all right? as its a new BB?
				return compatible_assembly# and then obv don't want to reprocess.
			
			elif current.type == "IfExp":
				# check children, not sure if we should have a local liveness or a global one??? I think global, consider:
				# g = 0
				# x = 1
				# if x:
				#    a = 3
				# else:
				#    a = 4
				# print g, if liveness is local then g will be removed as its not needed by the end of its block
				# similarly if you use print a instead of g but do liveness only locally, it'll be killed off in the then: and else: blocks as its not live by the end of the block
				# so do liveness globally. every time you need to compute liveness, do it by calling liveness on the global root, not the local root
				current.thenNext = dead_store_elim(current.thenNext, global_root)
				current.elseNext = dead_store_elim(current.elseNext, global_root)
				dead_store_elim(current.next, global_root) # should have its own scope and all right? as its a new BB?
				return compatible_assembly# and then obv don't want to reprocess.
			
			# else:
			# 	print current
			# 	print current.type == "movl"
			# 	raise Exception("No instruction match: " + str(current.type))
			if current != None:
				current = current.next

		compatible_assembly = get_first(get_last(compatible_assembly))
		itercount += 1

		# if itercount > 10:
		# print "---", itercount, "---"
		# current = compatible_assembly
		# while current != None:
		# 	print current
		# 	current = current.next
		# print '\n\n\n'
		# if itercount == 1:
		# 	break



	# print "---"
	# print_linked_list_new(compatible_assembly)
	# print_linked_list_new(compatible_assembly)
	# print "---\n\n"
	
	return compatible_assembly