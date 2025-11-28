from re import *


def infix_to_prefix(raw_text):

	raw_text = raw_text[::-1]
	text = ''

	for letter in raw_text:
		if letter == '(':
			text = text + ')'
		elif letter == ')':
			text = text + '('
		else:
			text = text + letter
	
	stack = []
	postfix = ''

	i = 0
	while(i < len(text)):
		letter = text[i]

		if letter == '(':
			stack.append('(')
			postfix = postfix + ')'
		elif letter == ')':
			x = stack.pop()
			while(x != '('):
				postfix = postfix + x
				x = stack.pop()
			postfix = postfix + '('
		elif letter == '|':
			postfix = postfix + ','
			if stack == []:
				stack.append(' rO')
				i+=1
			else:
				x = stack.pop()
				while(x != '('):
					postfix = postfix + x
					x = stack.pop()
				stack.append('(')
				stack.append(' rO')
				i+=1

		elif letter == '&':
			postfix = postfix + ','
			if stack == []:
				stack.append(' dnA')
				i+=1
			else:
				x = stack.pop()
				while(x != '('):
					postfix = postfix + x
					x = stack.pop()
				stack.append('(')
				stack.append(' dnA')
				i+=1

		else:
			postfix = postfix + letter 

		i+=1

	while(stack != []):
		x = stack.pop()
		postfix = postfix + x

	prefix = postfix[::-1]
	prefix = sub('\(Or ','Or(', prefix)
	prefix = sub('\(And ','And(', prefix)
	
	
	#Also have to return the set of conditions
	arr = prefix.split(',')
	arr = [sub('And|Or|\(|\)|','',cond) for cond in arr]
	arr = [cond.strip() for cond in arr]		
	return (prefix,arr)


def Tarjan(vertices,edges):
	
	index = 0
	stack = []
	arr_index = [-1 for vertex in vertices]
	low_link = [len(vertices)+1 for vertex in vertices]
	on_stack = [False for vertex in vertices]
	SCCs = []

	def strong_connect(v,index):
		vertex = vertices[v]

		arr_index[v] = index
		low_link[v] = index
		index+=1
		stack.append(v)
		on_stack[v] = True

		for w in range(len(vertices)):
			incoming = vertices[w]
			if [vertex,incoming] not in edges:
				continue
			
			if arr_index[w] == -1:
				strong_connect(w,index)
				low_link[v] = min(low_link[v],low_link[w])

			elif on_stack[w]:
				low_link[v] = min(low_link[v],arr_index[w])

		
		

		if low_link[v] == arr_index[v]:
			scc = []
			w = -1
			while(w != v):
				w = stack.pop()
				on_stack[w] = False
				scc.append(vertices[w])
			SCCs.append(scc[:])
		return index
			

	for i in range(len(vertices)):
		vertex = vertices[i]
		if arr_index[i] == -1:
			index = strong_connect(i,index)

			
	
	return SCCs



def aut_master(lines):
		
	lines = lines[2:]
	lines = [line[:-1] for line in lines] #Removing the newline
	
	def func(arr,j):
		res = []
		i = j
		for elem in arr[j:]:
			if elem != '}':
				if elem[-1] == ';':
					elem = elem[:-1]
				res.append(elem) #Skipping the semicolon 
				i+=1
			else:
				i+=3 #Skipping the new line and the additional string at the start of the next module
				break
		return (res,i)
			


	#Getting shared variables

	
	shared = lines[0].split(' ')[1:] #Removing the initial string 'shared'
	shared = [var[:-1] for var in shared] #Removing the commas and semi-colons

	parameters = lines[1].split(' ')[1:]
	parameters = [parameter[:-1] for parameter in parameters]

	(assumptions, next_line) = func(lines,3)

	(locations,next_line) = func(lines, next_line)
	locations = [location.split(':')[0] for location in locations]

	(inits,next_line) = func(lines, next_line)
	
	number_function = inits[0].split('== ')[1]

	(unformatted_rules,next_line) = func(lines, next_line)


	#print(shared)
	#print(parameters)
	#print(assumptions)
	#print(locations)
	#print(inits)
	#print(number_function)
	#print(unformatted_rules)


	rules = []
	all_conditions = set()
	all_edges = []
	count = 0

	for x in range(0,len(unformatted_rules),3):
		unformatted_edge = unformatted_rules[x].split(': ')[1]
		edge = unformatted_edge.split(' -> ')
		all_edges.append(edge)

		unformatted_condition = unformatted_rules[x+1].split('when ')[1]
		if unformatted_condition == '(1)':
			unformatted_condition = '(True)'
		
		condition,arr = infix_to_prefix(unformatted_condition)
		for cond in arr:
			all_conditions.add(cond)


		unformatted_update = unformatted_rules[x+2].split('do ')[1]
		unformatted_update = sub(' }|{ |\(|\)','',unformatted_update)
		unformatted_update = sub(';',',',unformatted_update)
		unformatted_update = unformatted_update.split(', ')
		update = [sub('[a-z,A-Z,0-9].*\ == ','',z) for z in unformatted_update]
		update = [sub('\ |,','',z) for z in update]
		
		rules.append((edge, condition, arr, update, count))
		count+=1

	num_conditions = len(all_conditions)
	num_rules = len(rules)


	#Do Tarjan and identify all the sccs

	SCCs = Tarjan(locations,all_edges)
	
	cycles = [] #Assuming that the graph contains only simple cycles. Hence a SCC is just a cycle
	for scc in SCCs:
		cycle = []
		for rule in rules:
			edge = rule[0]
			rule_no = rule[4]
			if edge[0] in scc and edge[1] in scc:
				cycle.append(rule_no)
		if cycle != []:
			cycles.append(cycle)


	return(shared, parameters, assumptions, locations, number_function, inits, rules, all_conditions, num_rules, num_conditions, cycles, SCCs)


#files = ['frb','strb','nbacg','nbacr','aba_CASE1','aba_CASE2','cbc_CASE1', 'cbc_CASE2', 'cbc_CASE3', 'cbc_CASE4',
#'cf1s_CASE1','cf1s_CASE2','cf1s_CASE3','c1cs_CASE1','c1cs_CASE2','c1cs_CASE3','bosco_CASE1','bosco_CASE2','bosco_CASE3','bosco_CASE4']

#f = open(files[15],'r')
#lines = f.readlines()
#shared, parameters, assumptions, locations, number_function, inits, rules, all_conditions, num_rules, num_conditions, cycles, SCCs = aut_master(lines)

#print(all_conditions)
#print(set([rule[1] for rule in rules]))

#print([scc for scc in SCCs if len(scc) >= 2])

'''
for rule in rules:
	if rule[0][0] == rule[0][1]:
		rules.remove(rule)

visited = []
depth = {}
fl = 0
while fl == 0:
	fl = 1
	for loc in locations:
		if loc in visited:
			continue
		source = True
		for rule in rules:
			if rule[0][1] == loc:
				if rule[0][0] not in visited:
					source = False
					break
		if source == True:
			fl = 0
			visited.append(loc)
			dep = 0
			for rule in rules:
				if rule[0][1] == loc:
					dep = max(dep,depth[rule[0][0]]+1)
			depth[loc] = dep


max_depth = 0
for loc in locations:
	if loc in depth.keys():
		max_depth = max(max_depth,depth[loc])

print(max_depth)
'''
