from dataTypes import *

def liveness(flattened_assembly, live_list):
	current = get_last(flattened_assembly)
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
			then = liveness(current.thenNext, live_list)
			elsex = liveness(current.elseNext, live_list)
			live_list = then | elsex
		elif current.type== "While":
			new_live = set(live_list)
			loopLive = set([])
			old_live = None
			while True:
				live_list = new_live | loopLive
				if isinstance(current.input1, Variable):
					live_list.add(current.input1.name)
				live_list = liveness(current.elseNext, live_list)
				if old_live == live_list:
					break
				old_live = set(live_list)
				loopLive = liveness(current.thenNext, live_list)
		else:
			raise Exception("No instruction match: " + str(current.type))
		current = current.prev
	return live_list