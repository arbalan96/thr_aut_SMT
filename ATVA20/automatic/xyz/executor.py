import time
start = time.time()

base = ['frb','frb_hand', 'strb', 'strb_hand', 'nbacg', 'nbacg_hand', 'nbacr', 'nbacr_hand', 'aba', 'aba1', 
'aba_hand']

additional = ['_abort_validity', '_agreement', '_commit_validity']


base_file = 'aba_hand'
additional_file = ''


f = open(base_file,'r')

lines = f.readlines()

def func(arr,j):
	res = []
	for elem in arr:
		if elem != '\n':
			elem = elem[:-1]
			res.append(elem)
			j+=1
		else:
			j+=1
			break
	return (res,j)


(shared,i) = func(lines[1:],1)
(parameters,i) = func(lines[i+1:],i+1)
(assumptions,i) = func(lines[i+1:],i+1)
(locations,i) = func(lines[i+1:],i+1)
(number_function,i) = func(lines[i+1:],i+1)
(inits,i) = func(lines[i+1:],i+1)
(unformatted_rules,i) = func(lines[i+1:],i+1)


locations = [location.split(':')[0] for location in locations]

rules = []
count = 0
total_conditions = set()
for x in range(0,len(unformatted_rules),3):
	unformatted_edge = unformatted_rules[x].split(': ')[1]
	edge = unformatted_edge.split(' -> ')

	unformatted_condition = unformatted_rules[x+1].split('when ')[1]
	condition = unformatted_condition.split(', ')
	for y in condition:
		total_conditions.add(y)

	unformatted_update = (unformatted_rules[x+2].split('do ')[1]).split(', ')
	update = []
	for y in unformatted_update:
		l = (y.split(' == ')[1]).split()
		st = ''
		for z in l:
			st = st + z
		
		update.append(st)

	rules.append((edge, condition, update, count))
	count+=1

num_conditions = len(total_conditions)
num_rules = len(rules)

f.close()


############################################################

h = open(base_file+'_spec'+additional_file, 'r')

lines = h.readlines()
lines = [line[:-1] for line in lines]
lines = [line for line in lines if line != '\n']

x = lines[0].split(', ')
y = lines[2].split(', ')

if x[0] == 'Or':
	initial_cond = 's.add(Or('
else:
	initial_cond = 's.add(And('

for word in x[1:]:
	c = word.split()
	loc = c[0] + '_0'
	eq = c[1]
	num = c[2]

	c = loc + ' ' + eq + ' ' + num

	initial_cond = initial_cond + c + ', '

initial_cond = initial_cond[:-2] + '))'

if y[0] == 'Or':
	final_cond = 's.add(Or('
else:
	final_cond = 's.add(And('

for word in y[1:]:
	if y[0] == 'Or':
		test  = 'Or('
	else:
		test  = 'And('

	c = word.split()
	loc = c[0]
	eq = c[1]
	num = c[2]
	
	for i in range(2*num_conditions+2):
		c = loc + '_' + str(i) + ' ' + eq + ' ' + num
		test = test + c + ', '
	test = test[:-2] + '), '
	final_cond = final_cond + test

final_cond = final_cond[:-2] + '))'		

h.close()

#############################################################


#Now I will create a file which when compiled creates a solver, adds all the constraints and solves it


g = open(base_file+'_constraints'+additional_file+'.py','w')

g.write('import time\n')
g.write('start = time.time()\n')

g.write('from z3 import *\n')
g.write('s = Solver()\n')


g.write('\n################Step 1#################\n\n')

g.write('\n#Declaring parameter variables\n\n')

for parameter in parameters:
	g.write('%s = Int(\'%s\')\n' % (parameter, parameter))

for parameter in parameters:
	g.write('s.add(%s >= 0)\n' % parameter)



g.write('\n#Adding the resilience condition\n\n')

for assumption in assumptions:
	g.write('s.add(%s)\n' % assumption)


g.write('\n#Creating many copies of location variables\n\n')

for location in locations:
	for i in range(2*num_conditions+2):
		g.write('%s_%d = Int(\'%s_%d\')\n' % (location, i, location, i))
	for i in range(2*num_conditions+2):
		g.write('s.add(%s_%d >= 0)\n' % (location,i))
	g.write('\n')


g.write('\n#Adding the constraint for the number of processes\n\n')

for i in range(2*num_conditions+2):
	st = locations[0] + '_' + str(i) 
	for location in locations[1:]:
		st = st + ' + ' + location + '_' + str(i)
	st = st + ' == ' + number_function[0]
	g.write('s.add(%s)\n' % st)


g.write('\n#Creating many copies of shared variables\n\n')

for var in shared:
	for i in range(2*num_conditions+2):
		g.write('%s_%d = Int(\'%s_%d\')\n' % (var, i, var, i))
	for i in range(2*num_conditions+2):
		g.write('s.add(%s_%d >= 0)\n' % (var, i))
	g.write('\n')


g.write('\n#Ensuring that the odd to even indices have the same context\n\n')

for i in range(0,2*num_conditions+2,2):
	for condition in total_conditions:
		st = condition.split()
		st1 = ''
		st2 = ''
		fl = 0
		for letter in st:
			if letter == 'true':
				fl = 1
				break
			if letter in shared:
				st1 = st1 + letter + '_' + str(i) + ' '
				st2 = st2 + letter + '_' + str(i+1) + ' '
			else:
				st1 = st1 + letter + ' '
				st2 = st2 + letter + ' '
		if(fl == 0):
			g.write('s.add((%s) == (%s))\n' % (st1, st2))
	


g.write('\n###################Step 1 1/2###################\n\n')

g.write('\n#Creating many copies of variables for rules\n\n')

for i in range(num_rules):
	for j in range(2*num_conditions+1):
		g.write('x%d_%d = Int(\'x%d_%d\')\n' %(i,j,i,j))
	for j in range(2*num_conditions+1):
		g.write('s.add(x%d_%d >= 0)\n' %(i,j))
	g.write('\n')


g.write('\n#Ensuring that at most one rule is fired from an odd to an even configuration\n\n')

for j in range(1,2*num_conditions+1,2):
	st = 'x0_' + str(j)
	g.write('s.add(Or((x0_%d == 0), (x0_%d == 1)))\n' %(j,j))
	for i in range(1,num_rules):
		st = st + ' + ' + 'x' + str(i) + '_' + str(j)
		g.write('s.add(Or((x%d_%d == 0), (x%d_%d == 1)))\n' %(i,j,i,j))
	st = st + ' <= ' + '1'
	g.write('s.add(%s)\n\n' % st)



g.write('\n###################Step 2####################\n\n')

g.write('\n#Flow equations for the locations\n\n')


for i in range(2*num_conditions+1):
	for location in locations:
		st = 's.add('
		for rule in rules:
			edge = rule[0]
			outgoing = edge[0]
			incoming = edge[1]
			rule_number = rule[3]
			if(outgoing == location):
				st = st + ' - ' + 'x' + str(rule_number) + '_' + str(i)
			if(incoming == location):
				st = st + ' + ' + 'x' + str(rule_number) + '_' + str(i)
		st = st + ' ==  ' + location + '_' + str(i+1) + ' - ' + location + '_' + str(i) + ')\n'
		g.write(st)




g.write('\n##################Step 3########################\n\n')

g.write('\n#Flow equations for the shared variables\n\n')


for i in range(2*num_conditions+1):
	for var in shared:
		st = 's.add(0'
		for rule in rules:
			updates = rule[2]
			rule_number = rule[3]
			for update in updates:
				if '+' in update:
					split = update.split('+')
					name = split[0]
					value = split[1]
					if name == var:
						st = st + ' + ' + 'x' + str(rule_number) + '_' + str(i) + ' * ' + str(value) 
		st = st + ' == ' + var + '_' + str(i+1) + ' - ' + var + '_' + str(i) + ')\n'	
		g.write(st)




g.write('\n####################Step 4########################\n\n')

g.write('\n#Rule is fired implies rule is enabled\n\n')

for rule in rules:
	rule_number = rule[3]
	rule_conditions = rule[1]
	for i in range(2*num_conditions+1):
		for condition in rule_conditions:
			st = condition.split()
			st0 = ''
			fl = 0
			for letter in st:
				if letter == 'true':
					fl = 1
					break
				if letter in shared:
					st0 = st0 + letter + '_' + str(i) + ' '
				else:
					st0 = st0 + letter + ' '
		
			if(fl == 0):
				g.write('s.add(Implies( (x%d_%d > 0), (%s) ))\n' %(rule_number,i,st0))




#g.write('\n#################Step 5#######################\n\n')

#g.write('\n#Existence of fireable chains, but simplified because of canonical automata\n\n')

#for rule in rules:
#	rule_number = rule[3]
#	outgoing = rule[0][0]
#	for i in range(2*num_conditions+1):
#		l = 'Or( x'+str(rule_number)+str(i) + ' == 0, ' + '' + outgoing + str(i) + ' > 0 )'
#		g.write('s.add(%s)\n' % l)


g.write('\n####################Step 5#################\n\n')

g.write('\n#Constraints for initial configuration\n\n')

for init in inits:
	st = init.split()
	st0 = ''
	for letter in st:
		if letter in locations:
			st0 = st0 + letter + '_0' + ' '
		elif letter in shared:
			st0 = st0 + letter + '_0' + ' '
		else:
			st0 = st0 + letter + ' '
	g.write('s.add(%s)\n' % st0)


g.write('\n#################Step 6####################\n\n')

g.write('\n#Specification, as of now hand written\n\n')


#Specification for strb

#g.write('s.add(loc0_1_0 == 0)\n')
#st = 's.add(Or(loc3_3_0 > 0'
#for i in range(2*num_conditions+2):
#	st = st + ', loc3_3_' + str(i) + ' > 0'
#st = st + '))\n'
#g.write(st)


#Specification for frb

#g.write('s.add(loc0_1_0 == 0)\n')
#st = 's.add(Or(loc0_2_0 > 0'
#for i in range(2*num_conditions+2):
#	st = st + ', loc0_2_' + str(i) + ' > 0'
#st = st + '))\n'
#g.write(st)

#st = 's.add(Or(loc1_2_0 > 0'
#for i in range(2*num_conditions+2):
#	st = st + ', loc1_2_' + str(i) + ' > 0'
#st = st + '))\n'
#g.write(st)


#Specification for nbacc
#g.write('s.add(loc0_0_0_0_0 > 0)\n')
#se = ['loc1_3_3_0','loc1_3_3_1','loc0_3_3_1','loc2_3_3_0','loc2_3_3_1','loc3_3_3_1','loc3_3_3_0','loc0_3_3_0']
#st = ('s.add(Or(loc1_3_3_0_0 > 0')

#for x in se:
#	for i in range(2*num_conditions+2):
#		st = st + ', ' + x + '_' + str(i) + ' > 0'
#st = st + '))\n'
#g.write(st)	
	


#Specification for nbacr

g.write('%s\n' %initial_cond)
g.write('%s\n' %final_cond)







g.write('\nprint(s.check())\n')

g.write('end = time.time()\n')
g.write('print(end-start)\n')

#g.write('print(s.model())\n')

end = time.time()
print(end-start)
