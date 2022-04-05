import dataTypes


def addToHeap(heap, item, value):
	heap.append(dataTypes.storeHeap(item))
	return increment(heap, len(heap) - 1, value)

def increment(heap, loc, new_value):
	if loc != -1:
		parent_loc = ((loc + 1) / 2) - 1
		if parent_loc != -1 and new_value > heap[parent_loc].value:
			swap(heap, parent_loc, loc)
			update_heap(heap, loc)
			return increment(heap, parent_loc, new_value)
		else:
			heap[loc].value = new_value
			update_heap(heap, loc)
			return loc

def swap(heap, loc1, loc2):
	holder = heap[loc1]
	heap[loc1] = heap[loc2]
	heap[loc2] = holder

def update_heap(heap, loc):
	heap[loc].object.key = loc;

def pop(heap):
	if not heap:
		return None
	else:
		object = heap[0].object
		heap[0] = heap[len(heap) - 1]
		del heap[-1]
		if heap:
			move_down(heap, 0)
		object.key = -1
		return object

def move_down(heap, loc):
	left_loc = loc * 2 + 1
	right_loc = loc * 2 + 2
	if left_loc > (len(heap) - 1):
		left_value = 0
		right_value = 0
	elif left_loc == (len(heap) - 1):
		left_value = heap[left_loc].value
		right_value = 0
	else:
		left_value = heap[left_loc].value
		right_value = heap[right_loc].value
	value = heap[loc].value
	if left_value > value:
		if left_value > right_value:
			swap(heap, loc, left_loc)
			move_down(heap, left_loc)
		else:
			swap(heap, loc, right_loc)
			move_down(heap, right_loc)
	elif right_value > value:
		swap(heap, loc, right_loc)
		move_down(heap, right_loc)
	update_heap(heap, loc)

def create_graph(flattened_assembly, variable_list, unspillable):
	nodes = {"eax":dataTypes.GraphNode(True), "ecx":dataTypes.GraphNode(True), "edx":dataTypes.GraphNode(True), "al":dataTypes.GraphNode(True)}

	for var in variable_list:
		spill = False
		if var in unspillable:
			spill = True
		nodes[var.name] = dataTypes.GraphNode(True)
	finish_graph(flattened_assembly, nodes)
	return nodes

def add_edge(input1, input2, nodes):
	nodes[input1].edges.add(input2)
	nodes[input2].edges.add(input1)

def add_edges(modVar, liveness, nodes):
	if isinstance(modVar, dataTypes.Variable):
		for var in liveness:
			if not (modVar.name == var):
				add_edge(modVar.name, var, nodes)

def finish_graph(flattened_assembly, nodes):
	working = flattened_assembly
	while (working != None):
		if working.type in ["movl", "movzbl"]:
			if isinstance(working.input2, dataTypes.Variable):
				for var in working.liveness:
					if not (working.input2.name == var):
						if isinstance(working.input1, dataTypes.Variable):
							if not working.input1.name == var:
								add_edge(working.input2.name, var, nodes)
						else:
							add_edge(working.input2.name, var, nodes)
		elif working.type == "IfExp":
			add_edges(working.input1, working.liveness, nodes)
			finish_graph(working.thenNext, nodes)
			finish_graph(working.elseNext, nodes)
		elif working.type in ["addl", "andl", "sall", "sarl", "orl"]:
			add_edges(working.input2, working.liveness, nodes)
		elif working.type in ["negl", "notl", "sete", "setne"]:
			add_edges(working.input1, working.liveness, nodes)
		elif working.type == "call":
			for var in working.liveness:
				nodes[var].edges.add("eax")
				nodes[var].edges.add("ecx")
				nodes[var].edges.add("edx")
				nodes["eax"].edges.add(var)
				nodes["ecx"].edges.add(var)
				nodes["edx"].edges.add(var)
		working = working.next

def color(saturation, colors):
	for color in colors:
		if color not in saturation:
			return color
	new_color = "-" + str((len(colors) - 5)*4) + "(%ebp)"
	colors.append(new_color)
	return new_color

def saturate(node, color, nodes, queue):
	node.color = color
	for nodekey in node.edges:
		nodes[nodekey].saturation.add(color)
		increment(queue, nodes[nodekey].key, (nodes[nodekey].unspillable, len(nodes[nodekey].saturation)))

def color_graph(nodes):
	colors = ["%eax", "%ecx", "%edx", "%ebx", "%edi", "%esi"]

	queue = []
	for node in nodes:
		if not node in ["eax", "al", "ecx", "edx"]:
			nodes[node].key = addToHeap(queue, nodes[node], (nodes[node].unspillable, 0))

	saturate(nodes["eax"],"%eax", nodes, queue)
	saturate(nodes["al"],"%eax", nodes, queue)
	saturate(nodes["ecx"],"%ecx", nodes, queue)
	saturate(nodes["edx"],"%edx", nodes, queue)

	while True:
		next_node = pop(queue)
		"""
		max_saturation = (False, -1)
		for node in nodes:
			if nodes[node].color == None:
				if (nodes[node].unspillable, len(nodes[node].saturation)) > max_saturation:
					max_saturation = (nodes[node].unspillable, len(nodes[node].saturation))
					next_node = node
					"""
		if next_node == None:
			break
		saturate(next_node, color(next_node.saturation, colors), nodes, queue)
	return len(colors) - 6
