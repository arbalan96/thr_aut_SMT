import time
import re
import resource
import os
import sys

start = time.time()

def extract(cond):
	result = findall(r"loc[0-9_]*",cond)
	return result

from aut_preprocessor import *
from formula_preprocessor import *

soft, hard = resource.getrlimit(resource.RLIMIT_AS) 
resource.setrlimit(resource.RLIMIT_AS, (7000000000,hard))

#Since the specifications are safety specifications and the automata are acyclic (or of the form where the cycles can be easily removed or not fired at all), we only need to implement the marking equation part of the convex semi=linear Horn formulas

specs = {}
specs['frb_NoBUGS'] = ['_unforg']
specs['frb_manual'] = ['_unforg']
specs['strb_NoBUGS'] = ['_unforg']
specs['strb_manual'] = ['_unforg']
specs['nbacg_NoBUGS'] = ['_abort_unreachable', '_abort_validity', '_agreement', '_commit_unreachable', '_commit_validity','_send_unreachable']
#specs['nbacg_manual'] = ['_abort_validity', '_agreement', '_commit_validity']
specs['aba_CASE1'] = ['_unforg']
specs['aba_CASE2'] = ['_unforg']
specs['cbc_CASE1'] = ['_unreach_ac0', '_unreach_ac1', '_unreach_cr', '_unreach_p0', '_unreach_p1','_validity_0', '_validity_1']
specs['cbc_CASE2'] = ['_unreach_ac0', '_unreach_ac1', '_unreach_cr', '_unreach_p0', '_unreach_p1','_validity_0', '_validity_1']
#specs['cbc_CASE3'] = ['_unreach_ac0'] #['_unreach_ac0', '_unreach_ac1', '_unreach_cr', '_unreach_p0', '_unreach_p1','_validity_0', '_validity_1'] Not running them because of MLE
#specs['cbc_CASE4'] = ['_unreach_ac0'] #['_unreach_ac0', '_unreach_ac1', '_unreach_cr', '_unreach_p0', '_unreach_p1','_validity_0', '_validity_1'] Not running them because of MLE
specs['cbc_manual'] = ['_agreement', '_validity0', '_validity1']
specs['cf1s_CASE1'] = ['_onestep0','_onestep1']
specs['cf1s_CASE2'] = ['_onestep0','_onestep1']
specs['cf1s_CASE3'] = ['_onestep0','_onestep1']
specs['cf1s_manual'] = ['_onestep0', '_onestep1']
specs['c1cs_CASE1'] = ['_onestep0','_onestep1', '_onestep_almost0', '_onestep_almost1']
specs['c1cs_CASE2'] = ['_onestep0','_onestep1', '_onestep_almost0', '_onestep_almost1']
specs['c1cs_CASE3'] = ['_onestep0','_onestep1', '_onestep_almost0', '_onestep_almost1']
specs['c1cs_manual'] = ['_onestep0', '_onestep1']


cases = {}

cases['frb'] = ['NoBUGS','manual']
cases['strb'] = ['NoBUGS','manual']
cases['nbacg'] = ['NoBUGS']
cases['aba'] = ['CASE1', 'CASE2']
cases['cbc'] = ['CASE1', 'CASE2', 'manual'] 
cases['cf1s'] = ['CASE1', 'CASE2', 'CASE3', 'manual']
cases['c1cs'] = ['CASE1', 'CASE2', 'CASE3', 'manual']


print("Enter the benchmark that you want to test on: frb, strb, nbacg, aba, cbc, cf1s, c1cs")
infile = input()

print("Enter the case you want to test on:" + str([x for x in cases[infile]]))
case = input()
base_folder = f"{infile}_fol/{infile}_{case}"
base_file = infile + '_' + case


for additional_file in specs[base_file]:

	print('Current automaton and specification: ' + base_file + additional_file)

	######################################################

	#Read the threshold automaton

	file_path = os.path.join(base_folder,base_file)
	with open(file_path, "r") as f:
		lines = f.readlines() #The threshold automaton    
    	
	    #Feed the automaton for preprocessing
		shared, parameters, assumptions, locations, number_function, inits, rules, total_conditions, fall_conditions, num_rules, num_conditions, cycles, SCCs = aut_master(lines)

    	


	f.close()


	############################################################

	#Read the specification

	file_path = os.path.join(base_folder,base_file+'_spec'+additional_file)
	with open(file_path, "r") as h:
		line = h.readline() #The threshold automaton    

    	#Feed the specification to the preprocessor
		init_cond, final_cond = formula_master(line)
	    
	

	h.close()

	#############################################################


	# Performing optimization w.r.t to current specification and automaton

	#Extract target locations from init_cond and final_cond
	targets = extract(init_cond) + extract(final_cond)

	#locations, inits, rules, num_rules = optimizations(locations, inits, rules, targets)
	print('Number of locations after optimizations: ' + str(len(locations)))
	print('Number of rules after optimizations: ' + str(num_rules))

	#####################################################################

	def find_vertex_outgoing(k): #Finds outgoing vertex of kth rule
		for rule in rules:
			if rule[4] == k:
				return rule[0][0]

	def find_vertex_incoming(k):
		for rule in rules:
			if rule[4] == k:
				return rule[0][1]




	##############################################################################################################


	#Reachability relation for the initial part of the lasso
	def reach_relation_init(steps = num_conditions):	

		######################################################
		#Open a file and add all the constraints in it
		g = open(os.path.join(base_folder,base_file+'_constraints'+additional_file+'.py'),"w")
        

		g.write('from z3 import *\n')

		g.write('s = Solver()\n')


		g.write('\n#Declaring parameter variables\n\n')

		for parameter in parameters:
			g.write('%s = Real(\'%s\')\n' % (parameter, parameter))
			g.write('s.add(%s >= 0)\n' % parameter)


		g.write('\n#Adding the resilience condition\n\n')

		for assumption in assumptions:
			g.write('s.add(%s)\n' % assumption)



		##################################################

		
		for index in range(steps+1):

			g.write('\n####################################################################################\n')

			g.write('\n#Creating constraints for a run between the x%dth and y%dth configurations\n' %(index, index))

			g.write('\n################Step 1#################\n\n')

			g.write('\n#Creating many copies of location variables\n\n')

			for location in locations:
				g.write('%s_x%d = Real(\'%s_x%d\')\n' % (location, index, location, index))
				g.write('%s_y%d = Real(\'%s_y%d\')\n' % (location, index, location, index))

				g.write('s.add(%s_x%d >= 0)\n' % (location,index))
				g.write('s.add(%s_y%d >= 0)\n' % (location,index))


			g.write('\n\n\n\n\n')



			g.write('\n#Creating many copies of shared variables\n\n')

			for var in shared:
				g.write('%s_x%d = Real(\'%s_x%d\')\n' % (var, index, var, index))
				g.write('%s_y%d = Real(\'%s_y%d\')\n' % (var, index, var, index))

				g.write('s.add(%s_x%d >= 0)\n' % (var, index))
				g.write('s.add(%s_y%d >= 0)\n' % (var, index))

		
			g.write('\n\n\n\n\n')



			g.write('\n#Creating many copies of variables for rules\n\n')
	
			for rule_number in range(len(rules)):
				assert rules[rule_number][-1] == rule_number				
				g.write('rule%d_x%d = Real(\'rule%d_x%d\')\n' %(rule_number,index,rule_number,index))
				g.write('s.add(rule%d_x%d >= 0)\n' %(rule_number,index))

			
			g.write('\n\n\n\n\n')



			g.write('\n###################Step 2####################\n\n')

			g.write('\n#Flow equations for the locations\n\n')

			for location in locations:
				st = 's.add(0'
				for rule_number in range(len(rules)):
					assert rules[rule_number][-1] == rule_number
					rule = rules[rule_number]

					edge = rule[0]
					outgoing = edge[0]
					incoming = edge[1]

					if(outgoing == location):
						st = st + ' - ' + 'rule' + str(rule_number) + '_x' + str(index)
					if(incoming == location):
						st = st + ' + ' + 'rule' + str(rule_number) + '_x' + str(index)

				st = st + ' ==  ' + location + '_y' + str(index) + ' - ' + location + '_x' + str(index) + ')\n'
				g.write(st)

			g.write('\n\n\n\n\n')


			g.write('\n##################Step 3########################\n\n')

			g.write('\n#Flow equations for the shared variables\n\n')


			for var in shared:
				st = 's.add(0'
				for rule_number in range(len(rules)):
					assert rules[rule_number][-1] == rule_number
					rule = rules[rule_number]

					updates = rule[3]

					for update in updates:
						if '+' in update:
							split = update.split('+')
							name = split[0]
							value = split[1]
							if name == var:
								st = st + ' + ' + 'rule' + str(rule_number) + '_x' + str(index) 

				st = st + ' == ' + var + '_y' + str(index) + ' - ' + var + '_x' + str(index) + ')\n'	
				g.write(st)

			
			g.write('\n\n\n\n\n')


			
			g.write('\n####################Step 4########################\n\n')

			g.write('\n#Rule is fired implies rule is enabled\n\n')

			for rule_number in range(len(rules)):
				assert rules[rule_number][-1] == rule_number
				rule = rules[rule_number]
				rule_conditions = rule[2]

				st = ''
				for condition in rule_conditions:
					split = condition.split()
					copy_condition = ''
					for word in split:
						if word in shared:
							copy_condition = copy_condition + word + '_x' + str(index)
						else:
							copy_condition = copy_condition + word		
					st = st + copy_condition  + ', '

				g.write('s.add(Implies( (rule%d_x%d > 0), And(%s) ))\n' %(rule_number,index,st))


			g.write('\n##################Step 5#########################\n\n')

			g.write('\n#Ensuring that configurations x%d and y%d have the same context\n\n' %(index, index))

			for condition in total_conditions:
				split = condition.split()
				stx = ''
				sty = ''
				for word in split:
					if word in shared:
						stx = stx + word + '_x' + str(index)
						sty = sty + word + '_y' + str(index)
					else:
						stx = stx + word		
						sty = sty + word		

				g.write('s.add((%s) == (%s))\n' % (stx, sty))



			if index == 0:
				g.write('\n#############Additional step for the initial configuration#####################\n\n')
				g.write('\n#############Ensure that the first configuration only contains initial locations###########\n\n')

				for init in inits:
					first = init.split(' == ')[0]
					if first[0] == '(':
						first = first[1:-1]
					first_split = first.split()

					init_condition = init
					for word in first_split:
						if word in shared or word in locations:
							init_condition = sub(word, word + '_x0', init_condition)

					g.write('s.add(%s)\n' %init_condition)	

				g.write('\n\n\n\n\n')

				g.write('\n###########Ensure that the first configuration satisfies the initial condition#############\n\n')

				init_cond_copy = init_cond
				for location in locations:
					init_cond_copy = sub(location, location + '_x0', init_cond_copy)

				g.write('s.add(%s)\n' %init_cond_copy)
				
				g.write('\n\n\n\n\n')


		
		################################################################################################################


		for index in range(steps):
	
			g.write('\n####################################################################################\n')

			g.write('\n#Creating constraints for a run between the y%dth and x%dth configurations\n' %(index, index+1))		

			g.write('\n################Step 1#################\n\n')

			g.write('\n#Creating many copies of variables for rules\n\n')

			for rule_number in range(len(rules)):
				g.write('rule%d_y%d = Real(\'rule%d_y%d\')\n' %(rule_number,index,rule_number,index))
				g.write('s.add(rule%d_y%d >= 0)\n' %(rule_number,index))

			g.write('\n\n\n\n\n')



			g.write('\n###################Step 2####################\n\n')

			g.write('\n#Flow equations for the locations\n\n')

			for location in locations:
				st = 's.add(0'
				for rule_number in range(len(rules)):
					assert rules[rule_number][-1] == rule_number
					rule = rules[rule_number]

					edge = rule[0]
					outgoing = edge[0]
					incoming = edge[1]

					if(outgoing == location):
						st = st + ' - ' + 'rule' + str(rule_number) + '_y' + str(index)
					if(incoming == location):
						st = st + ' + ' + 'rule' + str(rule_number) + '_y' + str(index)

				st = st + ' ==  ' + location + '_x' + str(index+1) + ' - ' + location + '_y' + str(index) + ')\n'
				g.write(st)

			g.write('\n\n\n\n\n')


			g.write('\n##################Step 3########################\n\n')

			g.write('\n#Flow equations for the shared variables\n\n')


			for var in shared:
				st = 's.add(0'
				for rule_number in range(len(rules)):
					assert rules[rule_number][-1] == rule_number
					rule = rules[rule_number]

					updates = rule[3]

					for update in updates:
						if '+' in update:
							split = update.split('+')
							name = split[0]
							value = split[1]
							if name == var:
								st = st + ' + ' + 'rule' + str(rule_number) + '_y' + str(index) 
				st = st + ' == ' + var + '_x' + str(index+1) + ' - ' + var + '_y' + str(index) + ')\n'	
				g.write(st)

			g.write('\n\n\n\n\n')


			g.write('\n####################Step 4########################\n\n')

			g.write('\n#Rule is fired implies rule is enabled\n\n')

			for rule_number in range(len(rules)):
				assert rules[rule_number][-1] == rule_number
				rule = rules[rule_number]
				rule_conditions = rule[2]

				st = ''
				for condition in rule_conditions:
					split = condition.split()
					copy_condition = ''
					for word in split:
						if word in shared:
							copy_condition = copy_condition + word + '_y' + str(index)
						else:
							copy_condition = copy_condition + word		
					st = st + copy_condition  + ', '

				g.write('s.add(Implies( (rule%d_y%d > 0), And(%s) ))\n' %(rule_number,index,st))


			g.write('\n##################Step 5########################\n\n')

			g.write('\n#Ensuring that at most one rule is fired alternating configurations y%d and x%d, if a fall condition is present\n\n' %(index, index))

			if fall_conditions != set([]):
	
				for condition in fall_conditions:
					split = condition.split()
					stx = ''
					sty = ''
					for word in split:
						if word in shared:
							stx = stx + word + '_x' + str(index+1)
							sty = sty + word + '_y' + str(index)
						else:
							stx = stx + word		
							sty = sty + word		

					g.write('s.add((%s) == (%s))\n' % (stx, sty))


					main_st = 'Implies(And((' + stx + '), Not(' + sty + ')), ' 		
					collect_st = ''

					for rule_number in range(num_rules):
						collect_st = collect_st + 'rule' + str(rule_number) + '_y' + str(index) + '+'
						st = main_st + 'Or((rule' + str(rule_number) + '_y' + str(index) + ' == 0), (rule' + str(rule_number) + '_y' + str(index) + ' == 1)' + '))'
						g.write('s.add(%s)\n' %st) 	

					collect_st = main_st + collect_st[:-1] + ' <= ' + '1' + ')'
					g.write('s.add(%s)\n\n' %collect_st)




		g.write('\n#############Additional step for the final configuration#####################\n\n')
		g.write('\n###########Ensure that the last configuration satisfies the final condition#############\n\n')

		final_cond_copy = final_cond
		for location in locations:
			final_cond_copy = sub(location, location + '_y' + str(steps), final_cond_copy)

		g.write('s.add(%s)\n' %final_cond_copy)
	
		g.write('\n\n\n\n\n')



		##############################################################################################################

		print ('Finished writing the constraints. Running the solver..')
		g.write('\nif s.check() == sat:\n')
		g.write('\n	print("Specification not satisfied")\n')
		g.write('\nelse:\n') 
		g.write('\n	print("Specification satisfied")\n')
		g.close()


		

	reach_relation_init()
	sys.path.append(base_folder)
	fi = base_file + '_constraints' + additional_file
	x = __import__(fi)
	
	#print '\n'

end = time.time()
print(end-start)
