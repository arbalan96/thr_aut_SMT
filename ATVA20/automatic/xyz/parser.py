from z3 import *

f = open('frb', 'r')

lines = f.readlines()
lines = [line[:-1] for line in lines]
lines = [line for line in lines if line != '']

lines_into_words = [line.split(', ') for line in lines]

parameters = lines_into_words[0][1:]
assumptions = lines_into_words[1][1:]
shared = lines_into_words[2][1:]
locations = lines_into_words[3][1:]
number_function = lines_into_words[4][1]
inits = lines_into_words[5][1:]

#print(parameters)
#print(assumptions)
#print(shared)
#print(locations)
#print(number_function)
#print(inits)

conditions = set()
rules = []
i = 0

for x in range(7,len(lines_into_words),3):
	edge = lines_into_words[x][1:]
	condition = lines_into_words[x+1][1:]
	updates = lines_into_words[x+2][1:]
	 
	for y in condition:
		conditions.add(y)


	rule = (edge,condition,updates,i)
	rules.append(rule)
	i+=1

	
num_conditions = len(conditions)
num_rules = len(rules)
#print(conditions)


#############################################################


#Now I will create a file which when compiled creates a solver, adds all the constraints and solves it


g = open('frb_constraints.py','w')

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
		g.write('%s%d = Int(\'%s%d\')\n' % (location, i, location, i))
	for i in range(2*num_conditions+2):
		g.write('s.add(%s%d >= 0)\n' % (location,i))
	g.write('\n')


g.write('\n#Adding the constraint for the number of processes\n\n')

for i in range(2*num_conditions+2):
	st = locations[0] + str(i) 
	for location in locations[1:]:
		st = st + ' + ' + location + str(i)
	st = st + ' == ' + number_function
	g.write('s.add(%s)\n' % st)


g.write('\n#Creating many copies of shared variables\n\n')

for var in shared:
	for i in range(2*num_conditions+2):
		g.write('%s%d = Int(\'%s%d\')\n' % (var, i, var, i))
	for i in range(2*num_conditions+2):
		g.write('s.add(%s%d >= 0)\n' % (var, i))
	g.write('\n')

g.write('\n#Ensuring that the odd to even indices have the same context\n\n')


for i in range(0,2*num_conditions+2,2):
	for condition in conditions:
		st = condition.split()
		st1 = ''
		st2 = ''
		fl = 0
		for letter in st:
			if letter == 'true':
				fl = 1
				break
			if letter in shared:
				st1 = st1 + letter + str(i) + ' '
				st2 = st2 + letter + str(i+1) + ' '
			else:
				st1 = st1 + letter + ' '
				st2 = st2 + letter + ' '
		if(fl == 0):
			g.write('s.add((%s) == (%s))\n' % (st1, st2))
	


g.write('\n###################Step 1 1/2###################\n\n')

g.write('\n#Creating many copies of variables for rules\n\n')

for i in range(num_rules):
	for j in range(2*num_conditions+1):
		g.write('x%d%d = Int(\'x%d%d\')\n' %(i,j,i,j))
	for j in range(2*num_conditions+1):
		g.write('s.add(x%d%d >= 0)\n' %(i,j))
	g.write('\n')


g.write('\n#Ensuring that at most one rule is fired from an odd to an even configuration\n\n')

for j in range(1,2*num_conditions+1,2):
	st = 'x0' + str(j)
	for i in range(1,num_rules):
		st = st + ' + ' + 'x' + str(i) + str(j)
		g.write('s.add(Or((x%d%d == 0), (x%d%d == 1)))\n' %(i,j,i,j))
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
				st = st + ' - ' + 'x' + str(rule_number) + str(i)
			if(incoming == location):
				st = st + ' + ' + 'x' + str(rule_number) + str(i)
		st = st + ' ==  ' + location + str(i+1) + ' - ' + location + str(i) + ')\n'
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
						st = st + ' + ' + 'x' + str(rule_number) + str(i) + ' * ' + str(value) 
		st = st + ' == ' + var + str(i+1) + ' - ' + var + str(i) + ')\n'	
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
					st0 = st0 + letter + str(i) + ' '
				else:
					st0 = st0 + letter + ' '
		
			if(fl == 0):
				g.write('s.add(Implies( (x%d%d > 0), (%s) ))\n' %(rule_number,i,st0))



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
			st0 = st0 + letter + '0' + ' '
		elif letter in shared:
			st0 = st0 + letter + '0' + ' '
		else:
			st0 = st0 + letter + ' '
	g.write('s.add(%s)\n' % st0)


g.write('\n#################Step 6####################\n\n')

g.write('\n#Specification, as of now hand written\n\n')


#Specification for strb
#g.write('s.add(loc10 == 0)\n')
#st = 's.add(Or(locAC0 > 0'
#for i in range(2*num_conditions+2):
#	st = st + ', locAC' + str(i) + ' > 0'
#st = st + '))\n'
#g.write(st)


#Specification for frb
g.write('s.add(loc10 == 0)\n')
st = 's.add(Or(locAC0 > 0'
for i in range(2*num_conditions+2):
	st = st + ', locAC' + str(i) + ' > 0'
st = st + '))\n'
g.write(st)



g.write('\nprint(s.check())\n')
#g.write('print(s.model())\n')
