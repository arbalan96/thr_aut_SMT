from z3 import *
s = Solver()

#Declaring parameter variables

N = Real('N')
s.add(N >= 0)
T = Real('T')
s.add(T >= 0)
F = Real('F')
s.add(F >= 0)

#Adding the resilience condition

s.add(N > (3 * T))
s.add(N > 3)
s.add(F >= 0)
s.add(T >= 1)
s.add(F <= T)

####################################################################################

#Creating constraints for a run between the x0th and y0th configurations

################Step 1#################


#Creating many copies of location variables

loc0_0_x0 = Real('loc0_0_x0')
loc0_0_y0 = Real('loc0_0_y0')
s.add(loc0_0_x0 >= 0)
s.add(loc0_0_y0 >= 0)
loc3_3_x0 = Real('loc3_3_x0')
loc3_3_y0 = Real('loc3_3_y0')
s.add(loc3_3_x0 >= 0)
s.add(loc3_3_y0 >= 0)
loc1_0_x0 = Real('loc1_0_x0')
loc1_0_y0 = Real('loc1_0_y0')
s.add(loc1_0_x0 >= 0)
s.add(loc1_0_y0 >= 0)
loc2_2_x0 = Real('loc2_2_x0')
loc2_2_y0 = Real('loc2_2_y0')
s.add(loc2_2_x0 >= 0)
s.add(loc2_2_y0 >= 0)
loc0_1_x0 = Real('loc0_1_x0')
loc0_1_y0 = Real('loc0_1_y0')
s.add(loc0_1_x0 >= 0)
s.add(loc0_1_y0 >= 0)
loc1_2_x0 = Real('loc1_2_x0')
loc1_2_y0 = Real('loc1_2_y0')
s.add(loc1_2_x0 >= 0)
s.add(loc1_2_y0 >= 0)
loc0_2_x0 = Real('loc0_2_x0')
loc0_2_y0 = Real('loc0_2_y0')
s.add(loc0_2_x0 >= 0)
s.add(loc0_2_y0 >= 0)






#Creating many copies of shared variables

nsnt_x0 = Real('nsnt_x0')
nsnt_y0 = Real('nsnt_y0')
s.add(nsnt_x0 >= 0)
s.add(nsnt_y0 >= 0)






#Creating many copies of variables for rules

rule0_x0 = Real('rule0_x0')
s.add(rule0_x0 >= 0)
rule1_x0 = Real('rule1_x0')
s.add(rule1_x0 >= 0)
rule2_x0 = Real('rule2_x0')
s.add(rule2_x0 >= 0)
rule3_x0 = Real('rule3_x0')
s.add(rule3_x0 >= 0)
rule4_x0 = Real('rule4_x0')
s.add(rule4_x0 >= 0)
rule5_x0 = Real('rule5_x0')
s.add(rule5_x0 >= 0)
rule6_x0 = Real('rule6_x0')
s.add(rule6_x0 >= 0)
rule7_x0 = Real('rule7_x0')
s.add(rule7_x0 >= 0)
rule8_x0 = Real('rule8_x0')
s.add(rule8_x0 >= 0)
rule9_x0 = Real('rule9_x0')
s.add(rule9_x0 >= 0)
rule10_x0 = Real('rule10_x0')
s.add(rule10_x0 >= 0)
rule11_x0 = Real('rule11_x0')
s.add(rule11_x0 >= 0)
rule12_x0 = Real('rule12_x0')
s.add(rule12_x0 >= 0)
rule13_x0 = Real('rule13_x0')
s.add(rule13_x0 >= 0)
rule14_x0 = Real('rule14_x0')
s.add(rule14_x0 >= 0)
rule15_x0 = Real('rule15_x0')
s.add(rule15_x0 >= 0)
rule16_x0 = Real('rule16_x0')
s.add(rule16_x0 >= 0)
rule17_x0 = Real('rule17_x0')
s.add(rule17_x0 >= 0)
rule18_x0 = Real('rule18_x0')
s.add(rule18_x0 >= 0)
rule19_x0 = Real('rule19_x0')
s.add(rule19_x0 >= 0)
rule20_x0 = Real('rule20_x0')
s.add(rule20_x0 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule13_x0 - rule14_x0 + rule14_x0 - rule15_x0 - rule16_x0 ==  loc0_0_y0 - loc0_0_x0)
s.add(0 + rule3_x0 + rule6_x0 + rule8_x0 + rule12_x0 + rule16_x0 + rule19_x0 - rule20_x0 + rule20_x0 ==  loc3_3_y0 - loc3_3_x0)
s.add(0 + rule15_x0 - rule17_x0 - rule18_x0 + rule18_x0 - rule19_x0 ==  loc1_0_y0 - loc1_0_x0)
s.add(0 + rule2_x0 + rule5_x0 - rule7_x0 + rule7_x0 - rule8_x0 + rule11_x0 + rule13_x0 + rule17_x0 ==  loc2_2_y0 - loc2_2_x0)
s.add(0 - rule9_x0 - rule10_x0 - rule11_x0 - rule12_x0 ==  loc0_1_y0 - loc0_1_x0)
s.add(0 + rule1_x0 - rule4_x0 + rule4_x0 - rule5_x0 - rule6_x0 + rule10_x0 ==  loc1_2_y0 - loc1_2_x0)
s.add(0 - rule0_x0 + rule0_x0 - rule1_x0 - rule2_x0 - rule3_x0 + rule9_x0 ==  loc0_2_y0 - loc0_2_x0)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule9_x0 + rule10_x0 + rule11_x0 + rule12_x0 + rule13_x0 + rule16_x0 + rule17_x0 + rule19_x0 == nsnt_y0 - nsnt_x0)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x0 > 0), And(True, ) ))
s.add(Implies( (rule1_x0 > 0), And(nsnt_x0+F>=1, ) ))
s.add(Implies( (rule2_x0 > 0), And(nsnt_x0+F>=T+1, ) ))
s.add(Implies( (rule3_x0 > 0), And(nsnt_x0+F>=N-T, ) ))
s.add(Implies( (rule4_x0 > 0), And(nsnt_x0+F>=1, ) ))
s.add(Implies( (rule5_x0 > 0), And(nsnt_x0+F>=T+1, ) ))
s.add(Implies( (rule6_x0 > 0), And(nsnt_x0+F>=N-T, ) ))
s.add(Implies( (rule7_x0 > 0), And(nsnt_x0+F>=T+1, ) ))
s.add(Implies( (rule8_x0 > 0), And(nsnt_x0+F>=N-T, ) ))
s.add(Implies( (rule9_x0 > 0), And(True, ) ))
s.add(Implies( (rule10_x0 > 0), And(nsnt_x0+F>=1, ) ))
s.add(Implies( (rule11_x0 > 0), And(nsnt_x0+F>=T+1, ) ))
s.add(Implies( (rule12_x0 > 0), And(nsnt_x0+F>=N-T, ) ))
s.add(Implies( (rule13_x0 > 0), And(nsnt_x0+F>=T+1, ) ))
s.add(Implies( (rule14_x0 > 0), And(True, ) ))
s.add(Implies( (rule15_x0 > 0), And(nsnt_x0+F>=1, ) ))
s.add(Implies( (rule16_x0 > 0), And(nsnt_x0+F>=N-T, ) ))
s.add(Implies( (rule17_x0 > 0), And(nsnt_x0+F>=T+1, ) ))
s.add(Implies( (rule18_x0 > 0), And(nsnt_x0+F>=1, ) ))
s.add(Implies( (rule19_x0 > 0), And(nsnt_x0+F>=N-T, ) ))
s.add(Implies( (rule20_x0 > 0), And(nsnt_x0+F>=N-T, ) ))

##################Step 5#########################


#Ensuring that configurations x0 and y0 have the same context

s.add((True) == (True))
s.add((nsnt_x0+F>=1) == (nsnt_y0+F>=1))
s.add((nsnt_x0+F>=T+1) == (nsnt_y0+F>=T+1))
s.add((nsnt_x0+F>=N-T) == (nsnt_y0+F>=N-T))

#############Additional step for the initial configuration#####################


#############Ensure that the first configuration only contains initial locations###########

s.add((loc0_1_x0 + loc0_0_x0) == (N - F))
s.add(loc3_3_x0 == 0)
s.add(loc1_0_x0 == 0)
s.add(loc2_2_x0 == 0)
s.add(loc1_2_x0 == 0)
s.add(loc0_2_x0 == 0)
s.add(nsnt_x0 == 0)






###########Ensure that the first configuration satisfies the initial condition#############

s.add(And(loc0_2_x0 == 0, loc1_2_x0 == 0, loc0_1_x0 == 0, loc2_2_x0 == 0, loc3_3_x0 == 0))






####################################################################################

#Creating constraints for a run between the x1th and y1th configurations

################Step 1#################


#Creating many copies of location variables

loc0_0_x1 = Real('loc0_0_x1')
loc0_0_y1 = Real('loc0_0_y1')
s.add(loc0_0_x1 >= 0)
s.add(loc0_0_y1 >= 0)
loc3_3_x1 = Real('loc3_3_x1')
loc3_3_y1 = Real('loc3_3_y1')
s.add(loc3_3_x1 >= 0)
s.add(loc3_3_y1 >= 0)
loc1_0_x1 = Real('loc1_0_x1')
loc1_0_y1 = Real('loc1_0_y1')
s.add(loc1_0_x1 >= 0)
s.add(loc1_0_y1 >= 0)
loc2_2_x1 = Real('loc2_2_x1')
loc2_2_y1 = Real('loc2_2_y1')
s.add(loc2_2_x1 >= 0)
s.add(loc2_2_y1 >= 0)
loc0_1_x1 = Real('loc0_1_x1')
loc0_1_y1 = Real('loc0_1_y1')
s.add(loc0_1_x1 >= 0)
s.add(loc0_1_y1 >= 0)
loc1_2_x1 = Real('loc1_2_x1')
loc1_2_y1 = Real('loc1_2_y1')
s.add(loc1_2_x1 >= 0)
s.add(loc1_2_y1 >= 0)
loc0_2_x1 = Real('loc0_2_x1')
loc0_2_y1 = Real('loc0_2_y1')
s.add(loc0_2_x1 >= 0)
s.add(loc0_2_y1 >= 0)






#Creating many copies of shared variables

nsnt_x1 = Real('nsnt_x1')
nsnt_y1 = Real('nsnt_y1')
s.add(nsnt_x1 >= 0)
s.add(nsnt_y1 >= 0)






#Creating many copies of variables for rules

rule0_x1 = Real('rule0_x1')
s.add(rule0_x1 >= 0)
rule1_x1 = Real('rule1_x1')
s.add(rule1_x1 >= 0)
rule2_x1 = Real('rule2_x1')
s.add(rule2_x1 >= 0)
rule3_x1 = Real('rule3_x1')
s.add(rule3_x1 >= 0)
rule4_x1 = Real('rule4_x1')
s.add(rule4_x1 >= 0)
rule5_x1 = Real('rule5_x1')
s.add(rule5_x1 >= 0)
rule6_x1 = Real('rule6_x1')
s.add(rule6_x1 >= 0)
rule7_x1 = Real('rule7_x1')
s.add(rule7_x1 >= 0)
rule8_x1 = Real('rule8_x1')
s.add(rule8_x1 >= 0)
rule9_x1 = Real('rule9_x1')
s.add(rule9_x1 >= 0)
rule10_x1 = Real('rule10_x1')
s.add(rule10_x1 >= 0)
rule11_x1 = Real('rule11_x1')
s.add(rule11_x1 >= 0)
rule12_x1 = Real('rule12_x1')
s.add(rule12_x1 >= 0)
rule13_x1 = Real('rule13_x1')
s.add(rule13_x1 >= 0)
rule14_x1 = Real('rule14_x1')
s.add(rule14_x1 >= 0)
rule15_x1 = Real('rule15_x1')
s.add(rule15_x1 >= 0)
rule16_x1 = Real('rule16_x1')
s.add(rule16_x1 >= 0)
rule17_x1 = Real('rule17_x1')
s.add(rule17_x1 >= 0)
rule18_x1 = Real('rule18_x1')
s.add(rule18_x1 >= 0)
rule19_x1 = Real('rule19_x1')
s.add(rule19_x1 >= 0)
rule20_x1 = Real('rule20_x1')
s.add(rule20_x1 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule13_x1 - rule14_x1 + rule14_x1 - rule15_x1 - rule16_x1 ==  loc0_0_y1 - loc0_0_x1)
s.add(0 + rule3_x1 + rule6_x1 + rule8_x1 + rule12_x1 + rule16_x1 + rule19_x1 - rule20_x1 + rule20_x1 ==  loc3_3_y1 - loc3_3_x1)
s.add(0 + rule15_x1 - rule17_x1 - rule18_x1 + rule18_x1 - rule19_x1 ==  loc1_0_y1 - loc1_0_x1)
s.add(0 + rule2_x1 + rule5_x1 - rule7_x1 + rule7_x1 - rule8_x1 + rule11_x1 + rule13_x1 + rule17_x1 ==  loc2_2_y1 - loc2_2_x1)
s.add(0 - rule9_x1 - rule10_x1 - rule11_x1 - rule12_x1 ==  loc0_1_y1 - loc0_1_x1)
s.add(0 + rule1_x1 - rule4_x1 + rule4_x1 - rule5_x1 - rule6_x1 + rule10_x1 ==  loc1_2_y1 - loc1_2_x1)
s.add(0 - rule0_x1 + rule0_x1 - rule1_x1 - rule2_x1 - rule3_x1 + rule9_x1 ==  loc0_2_y1 - loc0_2_x1)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule9_x1 + rule10_x1 + rule11_x1 + rule12_x1 + rule13_x1 + rule16_x1 + rule17_x1 + rule19_x1 == nsnt_y1 - nsnt_x1)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x1 > 0), And(True, ) ))
s.add(Implies( (rule1_x1 > 0), And(nsnt_x1+F>=1, ) ))
s.add(Implies( (rule2_x1 > 0), And(nsnt_x1+F>=T+1, ) ))
s.add(Implies( (rule3_x1 > 0), And(nsnt_x1+F>=N-T, ) ))
s.add(Implies( (rule4_x1 > 0), And(nsnt_x1+F>=1, ) ))
s.add(Implies( (rule5_x1 > 0), And(nsnt_x1+F>=T+1, ) ))
s.add(Implies( (rule6_x1 > 0), And(nsnt_x1+F>=N-T, ) ))
s.add(Implies( (rule7_x1 > 0), And(nsnt_x1+F>=T+1, ) ))
s.add(Implies( (rule8_x1 > 0), And(nsnt_x1+F>=N-T, ) ))
s.add(Implies( (rule9_x1 > 0), And(True, ) ))
s.add(Implies( (rule10_x1 > 0), And(nsnt_x1+F>=1, ) ))
s.add(Implies( (rule11_x1 > 0), And(nsnt_x1+F>=T+1, ) ))
s.add(Implies( (rule12_x1 > 0), And(nsnt_x1+F>=N-T, ) ))
s.add(Implies( (rule13_x1 > 0), And(nsnt_x1+F>=T+1, ) ))
s.add(Implies( (rule14_x1 > 0), And(True, ) ))
s.add(Implies( (rule15_x1 > 0), And(nsnt_x1+F>=1, ) ))
s.add(Implies( (rule16_x1 > 0), And(nsnt_x1+F>=N-T, ) ))
s.add(Implies( (rule17_x1 > 0), And(nsnt_x1+F>=T+1, ) ))
s.add(Implies( (rule18_x1 > 0), And(nsnt_x1+F>=1, ) ))
s.add(Implies( (rule19_x1 > 0), And(nsnt_x1+F>=N-T, ) ))
s.add(Implies( (rule20_x1 > 0), And(nsnt_x1+F>=N-T, ) ))

##################Step 5#########################


#Ensuring that configurations x1 and y1 have the same context

s.add((True) == (True))
s.add((nsnt_x1+F>=1) == (nsnt_y1+F>=1))
s.add((nsnt_x1+F>=T+1) == (nsnt_y1+F>=T+1))
s.add((nsnt_x1+F>=N-T) == (nsnt_y1+F>=N-T))

####################################################################################

#Creating constraints for a run between the x2th and y2th configurations

################Step 1#################


#Creating many copies of location variables

loc0_0_x2 = Real('loc0_0_x2')
loc0_0_y2 = Real('loc0_0_y2')
s.add(loc0_0_x2 >= 0)
s.add(loc0_0_y2 >= 0)
loc3_3_x2 = Real('loc3_3_x2')
loc3_3_y2 = Real('loc3_3_y2')
s.add(loc3_3_x2 >= 0)
s.add(loc3_3_y2 >= 0)
loc1_0_x2 = Real('loc1_0_x2')
loc1_0_y2 = Real('loc1_0_y2')
s.add(loc1_0_x2 >= 0)
s.add(loc1_0_y2 >= 0)
loc2_2_x2 = Real('loc2_2_x2')
loc2_2_y2 = Real('loc2_2_y2')
s.add(loc2_2_x2 >= 0)
s.add(loc2_2_y2 >= 0)
loc0_1_x2 = Real('loc0_1_x2')
loc0_1_y2 = Real('loc0_1_y2')
s.add(loc0_1_x2 >= 0)
s.add(loc0_1_y2 >= 0)
loc1_2_x2 = Real('loc1_2_x2')
loc1_2_y2 = Real('loc1_2_y2')
s.add(loc1_2_x2 >= 0)
s.add(loc1_2_y2 >= 0)
loc0_2_x2 = Real('loc0_2_x2')
loc0_2_y2 = Real('loc0_2_y2')
s.add(loc0_2_x2 >= 0)
s.add(loc0_2_y2 >= 0)






#Creating many copies of shared variables

nsnt_x2 = Real('nsnt_x2')
nsnt_y2 = Real('nsnt_y2')
s.add(nsnt_x2 >= 0)
s.add(nsnt_y2 >= 0)






#Creating many copies of variables for rules

rule0_x2 = Real('rule0_x2')
s.add(rule0_x2 >= 0)
rule1_x2 = Real('rule1_x2')
s.add(rule1_x2 >= 0)
rule2_x2 = Real('rule2_x2')
s.add(rule2_x2 >= 0)
rule3_x2 = Real('rule3_x2')
s.add(rule3_x2 >= 0)
rule4_x2 = Real('rule4_x2')
s.add(rule4_x2 >= 0)
rule5_x2 = Real('rule5_x2')
s.add(rule5_x2 >= 0)
rule6_x2 = Real('rule6_x2')
s.add(rule6_x2 >= 0)
rule7_x2 = Real('rule7_x2')
s.add(rule7_x2 >= 0)
rule8_x2 = Real('rule8_x2')
s.add(rule8_x2 >= 0)
rule9_x2 = Real('rule9_x2')
s.add(rule9_x2 >= 0)
rule10_x2 = Real('rule10_x2')
s.add(rule10_x2 >= 0)
rule11_x2 = Real('rule11_x2')
s.add(rule11_x2 >= 0)
rule12_x2 = Real('rule12_x2')
s.add(rule12_x2 >= 0)
rule13_x2 = Real('rule13_x2')
s.add(rule13_x2 >= 0)
rule14_x2 = Real('rule14_x2')
s.add(rule14_x2 >= 0)
rule15_x2 = Real('rule15_x2')
s.add(rule15_x2 >= 0)
rule16_x2 = Real('rule16_x2')
s.add(rule16_x2 >= 0)
rule17_x2 = Real('rule17_x2')
s.add(rule17_x2 >= 0)
rule18_x2 = Real('rule18_x2')
s.add(rule18_x2 >= 0)
rule19_x2 = Real('rule19_x2')
s.add(rule19_x2 >= 0)
rule20_x2 = Real('rule20_x2')
s.add(rule20_x2 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule13_x2 - rule14_x2 + rule14_x2 - rule15_x2 - rule16_x2 ==  loc0_0_y2 - loc0_0_x2)
s.add(0 + rule3_x2 + rule6_x2 + rule8_x2 + rule12_x2 + rule16_x2 + rule19_x2 - rule20_x2 + rule20_x2 ==  loc3_3_y2 - loc3_3_x2)
s.add(0 + rule15_x2 - rule17_x2 - rule18_x2 + rule18_x2 - rule19_x2 ==  loc1_0_y2 - loc1_0_x2)
s.add(0 + rule2_x2 + rule5_x2 - rule7_x2 + rule7_x2 - rule8_x2 + rule11_x2 + rule13_x2 + rule17_x2 ==  loc2_2_y2 - loc2_2_x2)
s.add(0 - rule9_x2 - rule10_x2 - rule11_x2 - rule12_x2 ==  loc0_1_y2 - loc0_1_x2)
s.add(0 + rule1_x2 - rule4_x2 + rule4_x2 - rule5_x2 - rule6_x2 + rule10_x2 ==  loc1_2_y2 - loc1_2_x2)
s.add(0 - rule0_x2 + rule0_x2 - rule1_x2 - rule2_x2 - rule3_x2 + rule9_x2 ==  loc0_2_y2 - loc0_2_x2)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule9_x2 + rule10_x2 + rule11_x2 + rule12_x2 + rule13_x2 + rule16_x2 + rule17_x2 + rule19_x2 == nsnt_y2 - nsnt_x2)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x2 > 0), And(True, ) ))
s.add(Implies( (rule1_x2 > 0), And(nsnt_x2+F>=1, ) ))
s.add(Implies( (rule2_x2 > 0), And(nsnt_x2+F>=T+1, ) ))
s.add(Implies( (rule3_x2 > 0), And(nsnt_x2+F>=N-T, ) ))
s.add(Implies( (rule4_x2 > 0), And(nsnt_x2+F>=1, ) ))
s.add(Implies( (rule5_x2 > 0), And(nsnt_x2+F>=T+1, ) ))
s.add(Implies( (rule6_x2 > 0), And(nsnt_x2+F>=N-T, ) ))
s.add(Implies( (rule7_x2 > 0), And(nsnt_x2+F>=T+1, ) ))
s.add(Implies( (rule8_x2 > 0), And(nsnt_x2+F>=N-T, ) ))
s.add(Implies( (rule9_x2 > 0), And(True, ) ))
s.add(Implies( (rule10_x2 > 0), And(nsnt_x2+F>=1, ) ))
s.add(Implies( (rule11_x2 > 0), And(nsnt_x2+F>=T+1, ) ))
s.add(Implies( (rule12_x2 > 0), And(nsnt_x2+F>=N-T, ) ))
s.add(Implies( (rule13_x2 > 0), And(nsnt_x2+F>=T+1, ) ))
s.add(Implies( (rule14_x2 > 0), And(True, ) ))
s.add(Implies( (rule15_x2 > 0), And(nsnt_x2+F>=1, ) ))
s.add(Implies( (rule16_x2 > 0), And(nsnt_x2+F>=N-T, ) ))
s.add(Implies( (rule17_x2 > 0), And(nsnt_x2+F>=T+1, ) ))
s.add(Implies( (rule18_x2 > 0), And(nsnt_x2+F>=1, ) ))
s.add(Implies( (rule19_x2 > 0), And(nsnt_x2+F>=N-T, ) ))
s.add(Implies( (rule20_x2 > 0), And(nsnt_x2+F>=N-T, ) ))

##################Step 5#########################


#Ensuring that configurations x2 and y2 have the same context

s.add((True) == (True))
s.add((nsnt_x2+F>=1) == (nsnt_y2+F>=1))
s.add((nsnt_x2+F>=T+1) == (nsnt_y2+F>=T+1))
s.add((nsnt_x2+F>=N-T) == (nsnt_y2+F>=N-T))

####################################################################################

#Creating constraints for a run between the x3th and y3th configurations

################Step 1#################


#Creating many copies of location variables

loc0_0_x3 = Real('loc0_0_x3')
loc0_0_y3 = Real('loc0_0_y3')
s.add(loc0_0_x3 >= 0)
s.add(loc0_0_y3 >= 0)
loc3_3_x3 = Real('loc3_3_x3')
loc3_3_y3 = Real('loc3_3_y3')
s.add(loc3_3_x3 >= 0)
s.add(loc3_3_y3 >= 0)
loc1_0_x3 = Real('loc1_0_x3')
loc1_0_y3 = Real('loc1_0_y3')
s.add(loc1_0_x3 >= 0)
s.add(loc1_0_y3 >= 0)
loc2_2_x3 = Real('loc2_2_x3')
loc2_2_y3 = Real('loc2_2_y3')
s.add(loc2_2_x3 >= 0)
s.add(loc2_2_y3 >= 0)
loc0_1_x3 = Real('loc0_1_x3')
loc0_1_y3 = Real('loc0_1_y3')
s.add(loc0_1_x3 >= 0)
s.add(loc0_1_y3 >= 0)
loc1_2_x3 = Real('loc1_2_x3')
loc1_2_y3 = Real('loc1_2_y3')
s.add(loc1_2_x3 >= 0)
s.add(loc1_2_y3 >= 0)
loc0_2_x3 = Real('loc0_2_x3')
loc0_2_y3 = Real('loc0_2_y3')
s.add(loc0_2_x3 >= 0)
s.add(loc0_2_y3 >= 0)






#Creating many copies of shared variables

nsnt_x3 = Real('nsnt_x3')
nsnt_y3 = Real('nsnt_y3')
s.add(nsnt_x3 >= 0)
s.add(nsnt_y3 >= 0)






#Creating many copies of variables for rules

rule0_x3 = Real('rule0_x3')
s.add(rule0_x3 >= 0)
rule1_x3 = Real('rule1_x3')
s.add(rule1_x3 >= 0)
rule2_x3 = Real('rule2_x3')
s.add(rule2_x3 >= 0)
rule3_x3 = Real('rule3_x3')
s.add(rule3_x3 >= 0)
rule4_x3 = Real('rule4_x3')
s.add(rule4_x3 >= 0)
rule5_x3 = Real('rule5_x3')
s.add(rule5_x3 >= 0)
rule6_x3 = Real('rule6_x3')
s.add(rule6_x3 >= 0)
rule7_x3 = Real('rule7_x3')
s.add(rule7_x3 >= 0)
rule8_x3 = Real('rule8_x3')
s.add(rule8_x3 >= 0)
rule9_x3 = Real('rule9_x3')
s.add(rule9_x3 >= 0)
rule10_x3 = Real('rule10_x3')
s.add(rule10_x3 >= 0)
rule11_x3 = Real('rule11_x3')
s.add(rule11_x3 >= 0)
rule12_x3 = Real('rule12_x3')
s.add(rule12_x3 >= 0)
rule13_x3 = Real('rule13_x3')
s.add(rule13_x3 >= 0)
rule14_x3 = Real('rule14_x3')
s.add(rule14_x3 >= 0)
rule15_x3 = Real('rule15_x3')
s.add(rule15_x3 >= 0)
rule16_x3 = Real('rule16_x3')
s.add(rule16_x3 >= 0)
rule17_x3 = Real('rule17_x3')
s.add(rule17_x3 >= 0)
rule18_x3 = Real('rule18_x3')
s.add(rule18_x3 >= 0)
rule19_x3 = Real('rule19_x3')
s.add(rule19_x3 >= 0)
rule20_x3 = Real('rule20_x3')
s.add(rule20_x3 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule13_x3 - rule14_x3 + rule14_x3 - rule15_x3 - rule16_x3 ==  loc0_0_y3 - loc0_0_x3)
s.add(0 + rule3_x3 + rule6_x3 + rule8_x3 + rule12_x3 + rule16_x3 + rule19_x3 - rule20_x3 + rule20_x3 ==  loc3_3_y3 - loc3_3_x3)
s.add(0 + rule15_x3 - rule17_x3 - rule18_x3 + rule18_x3 - rule19_x3 ==  loc1_0_y3 - loc1_0_x3)
s.add(0 + rule2_x3 + rule5_x3 - rule7_x3 + rule7_x3 - rule8_x3 + rule11_x3 + rule13_x3 + rule17_x3 ==  loc2_2_y3 - loc2_2_x3)
s.add(0 - rule9_x3 - rule10_x3 - rule11_x3 - rule12_x3 ==  loc0_1_y3 - loc0_1_x3)
s.add(0 + rule1_x3 - rule4_x3 + rule4_x3 - rule5_x3 - rule6_x3 + rule10_x3 ==  loc1_2_y3 - loc1_2_x3)
s.add(0 - rule0_x3 + rule0_x3 - rule1_x3 - rule2_x3 - rule3_x3 + rule9_x3 ==  loc0_2_y3 - loc0_2_x3)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule9_x3 + rule10_x3 + rule11_x3 + rule12_x3 + rule13_x3 + rule16_x3 + rule17_x3 + rule19_x3 == nsnt_y3 - nsnt_x3)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x3 > 0), And(True, ) ))
s.add(Implies( (rule1_x3 > 0), And(nsnt_x3+F>=1, ) ))
s.add(Implies( (rule2_x3 > 0), And(nsnt_x3+F>=T+1, ) ))
s.add(Implies( (rule3_x3 > 0), And(nsnt_x3+F>=N-T, ) ))
s.add(Implies( (rule4_x3 > 0), And(nsnt_x3+F>=1, ) ))
s.add(Implies( (rule5_x3 > 0), And(nsnt_x3+F>=T+1, ) ))
s.add(Implies( (rule6_x3 > 0), And(nsnt_x3+F>=N-T, ) ))
s.add(Implies( (rule7_x3 > 0), And(nsnt_x3+F>=T+1, ) ))
s.add(Implies( (rule8_x3 > 0), And(nsnt_x3+F>=N-T, ) ))
s.add(Implies( (rule9_x3 > 0), And(True, ) ))
s.add(Implies( (rule10_x3 > 0), And(nsnt_x3+F>=1, ) ))
s.add(Implies( (rule11_x3 > 0), And(nsnt_x3+F>=T+1, ) ))
s.add(Implies( (rule12_x3 > 0), And(nsnt_x3+F>=N-T, ) ))
s.add(Implies( (rule13_x3 > 0), And(nsnt_x3+F>=T+1, ) ))
s.add(Implies( (rule14_x3 > 0), And(True, ) ))
s.add(Implies( (rule15_x3 > 0), And(nsnt_x3+F>=1, ) ))
s.add(Implies( (rule16_x3 > 0), And(nsnt_x3+F>=N-T, ) ))
s.add(Implies( (rule17_x3 > 0), And(nsnt_x3+F>=T+1, ) ))
s.add(Implies( (rule18_x3 > 0), And(nsnt_x3+F>=1, ) ))
s.add(Implies( (rule19_x3 > 0), And(nsnt_x3+F>=N-T, ) ))
s.add(Implies( (rule20_x3 > 0), And(nsnt_x3+F>=N-T, ) ))

##################Step 5#########################


#Ensuring that configurations x3 and y3 have the same context

s.add((True) == (True))
s.add((nsnt_x3+F>=1) == (nsnt_y3+F>=1))
s.add((nsnt_x3+F>=T+1) == (nsnt_y3+F>=T+1))
s.add((nsnt_x3+F>=N-T) == (nsnt_y3+F>=N-T))

####################################################################################

#Creating constraints for a run between the x4th and y4th configurations

################Step 1#################


#Creating many copies of location variables

loc0_0_x4 = Real('loc0_0_x4')
loc0_0_y4 = Real('loc0_0_y4')
s.add(loc0_0_x4 >= 0)
s.add(loc0_0_y4 >= 0)
loc3_3_x4 = Real('loc3_3_x4')
loc3_3_y4 = Real('loc3_3_y4')
s.add(loc3_3_x4 >= 0)
s.add(loc3_3_y4 >= 0)
loc1_0_x4 = Real('loc1_0_x4')
loc1_0_y4 = Real('loc1_0_y4')
s.add(loc1_0_x4 >= 0)
s.add(loc1_0_y4 >= 0)
loc2_2_x4 = Real('loc2_2_x4')
loc2_2_y4 = Real('loc2_2_y4')
s.add(loc2_2_x4 >= 0)
s.add(loc2_2_y4 >= 0)
loc0_1_x4 = Real('loc0_1_x4')
loc0_1_y4 = Real('loc0_1_y4')
s.add(loc0_1_x4 >= 0)
s.add(loc0_1_y4 >= 0)
loc1_2_x4 = Real('loc1_2_x4')
loc1_2_y4 = Real('loc1_2_y4')
s.add(loc1_2_x4 >= 0)
s.add(loc1_2_y4 >= 0)
loc0_2_x4 = Real('loc0_2_x4')
loc0_2_y4 = Real('loc0_2_y4')
s.add(loc0_2_x4 >= 0)
s.add(loc0_2_y4 >= 0)






#Creating many copies of shared variables

nsnt_x4 = Real('nsnt_x4')
nsnt_y4 = Real('nsnt_y4')
s.add(nsnt_x4 >= 0)
s.add(nsnt_y4 >= 0)






#Creating many copies of variables for rules

rule0_x4 = Real('rule0_x4')
s.add(rule0_x4 >= 0)
rule1_x4 = Real('rule1_x4')
s.add(rule1_x4 >= 0)
rule2_x4 = Real('rule2_x4')
s.add(rule2_x4 >= 0)
rule3_x4 = Real('rule3_x4')
s.add(rule3_x4 >= 0)
rule4_x4 = Real('rule4_x4')
s.add(rule4_x4 >= 0)
rule5_x4 = Real('rule5_x4')
s.add(rule5_x4 >= 0)
rule6_x4 = Real('rule6_x4')
s.add(rule6_x4 >= 0)
rule7_x4 = Real('rule7_x4')
s.add(rule7_x4 >= 0)
rule8_x4 = Real('rule8_x4')
s.add(rule8_x4 >= 0)
rule9_x4 = Real('rule9_x4')
s.add(rule9_x4 >= 0)
rule10_x4 = Real('rule10_x4')
s.add(rule10_x4 >= 0)
rule11_x4 = Real('rule11_x4')
s.add(rule11_x4 >= 0)
rule12_x4 = Real('rule12_x4')
s.add(rule12_x4 >= 0)
rule13_x4 = Real('rule13_x4')
s.add(rule13_x4 >= 0)
rule14_x4 = Real('rule14_x4')
s.add(rule14_x4 >= 0)
rule15_x4 = Real('rule15_x4')
s.add(rule15_x4 >= 0)
rule16_x4 = Real('rule16_x4')
s.add(rule16_x4 >= 0)
rule17_x4 = Real('rule17_x4')
s.add(rule17_x4 >= 0)
rule18_x4 = Real('rule18_x4')
s.add(rule18_x4 >= 0)
rule19_x4 = Real('rule19_x4')
s.add(rule19_x4 >= 0)
rule20_x4 = Real('rule20_x4')
s.add(rule20_x4 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule13_x4 - rule14_x4 + rule14_x4 - rule15_x4 - rule16_x4 ==  loc0_0_y4 - loc0_0_x4)
s.add(0 + rule3_x4 + rule6_x4 + rule8_x4 + rule12_x4 + rule16_x4 + rule19_x4 - rule20_x4 + rule20_x4 ==  loc3_3_y4 - loc3_3_x4)
s.add(0 + rule15_x4 - rule17_x4 - rule18_x4 + rule18_x4 - rule19_x4 ==  loc1_0_y4 - loc1_0_x4)
s.add(0 + rule2_x4 + rule5_x4 - rule7_x4 + rule7_x4 - rule8_x4 + rule11_x4 + rule13_x4 + rule17_x4 ==  loc2_2_y4 - loc2_2_x4)
s.add(0 - rule9_x4 - rule10_x4 - rule11_x4 - rule12_x4 ==  loc0_1_y4 - loc0_1_x4)
s.add(0 + rule1_x4 - rule4_x4 + rule4_x4 - rule5_x4 - rule6_x4 + rule10_x4 ==  loc1_2_y4 - loc1_2_x4)
s.add(0 - rule0_x4 + rule0_x4 - rule1_x4 - rule2_x4 - rule3_x4 + rule9_x4 ==  loc0_2_y4 - loc0_2_x4)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule9_x4 + rule10_x4 + rule11_x4 + rule12_x4 + rule13_x4 + rule16_x4 + rule17_x4 + rule19_x4 == nsnt_y4 - nsnt_x4)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x4 > 0), And(True, ) ))
s.add(Implies( (rule1_x4 > 0), And(nsnt_x4+F>=1, ) ))
s.add(Implies( (rule2_x4 > 0), And(nsnt_x4+F>=T+1, ) ))
s.add(Implies( (rule3_x4 > 0), And(nsnt_x4+F>=N-T, ) ))
s.add(Implies( (rule4_x4 > 0), And(nsnt_x4+F>=1, ) ))
s.add(Implies( (rule5_x4 > 0), And(nsnt_x4+F>=T+1, ) ))
s.add(Implies( (rule6_x4 > 0), And(nsnt_x4+F>=N-T, ) ))
s.add(Implies( (rule7_x4 > 0), And(nsnt_x4+F>=T+1, ) ))
s.add(Implies( (rule8_x4 > 0), And(nsnt_x4+F>=N-T, ) ))
s.add(Implies( (rule9_x4 > 0), And(True, ) ))
s.add(Implies( (rule10_x4 > 0), And(nsnt_x4+F>=1, ) ))
s.add(Implies( (rule11_x4 > 0), And(nsnt_x4+F>=T+1, ) ))
s.add(Implies( (rule12_x4 > 0), And(nsnt_x4+F>=N-T, ) ))
s.add(Implies( (rule13_x4 > 0), And(nsnt_x4+F>=T+1, ) ))
s.add(Implies( (rule14_x4 > 0), And(True, ) ))
s.add(Implies( (rule15_x4 > 0), And(nsnt_x4+F>=1, ) ))
s.add(Implies( (rule16_x4 > 0), And(nsnt_x4+F>=N-T, ) ))
s.add(Implies( (rule17_x4 > 0), And(nsnt_x4+F>=T+1, ) ))
s.add(Implies( (rule18_x4 > 0), And(nsnt_x4+F>=1, ) ))
s.add(Implies( (rule19_x4 > 0), And(nsnt_x4+F>=N-T, ) ))
s.add(Implies( (rule20_x4 > 0), And(nsnt_x4+F>=N-T, ) ))

##################Step 5#########################


#Ensuring that configurations x4 and y4 have the same context

s.add((True) == (True))
s.add((nsnt_x4+F>=1) == (nsnt_y4+F>=1))
s.add((nsnt_x4+F>=T+1) == (nsnt_y4+F>=T+1))
s.add((nsnt_x4+F>=N-T) == (nsnt_y4+F>=N-T))

####################################################################################

#Creating constraints for a run between the y0th and x1th configurations

################Step 1#################


#Creating many copies of variables for rules

rule0_y0 = Real('rule0_y0')
s.add(rule0_y0 >= 0)
rule1_y0 = Real('rule1_y0')
s.add(rule1_y0 >= 0)
rule2_y0 = Real('rule2_y0')
s.add(rule2_y0 >= 0)
rule3_y0 = Real('rule3_y0')
s.add(rule3_y0 >= 0)
rule4_y0 = Real('rule4_y0')
s.add(rule4_y0 >= 0)
rule5_y0 = Real('rule5_y0')
s.add(rule5_y0 >= 0)
rule6_y0 = Real('rule6_y0')
s.add(rule6_y0 >= 0)
rule7_y0 = Real('rule7_y0')
s.add(rule7_y0 >= 0)
rule8_y0 = Real('rule8_y0')
s.add(rule8_y0 >= 0)
rule9_y0 = Real('rule9_y0')
s.add(rule9_y0 >= 0)
rule10_y0 = Real('rule10_y0')
s.add(rule10_y0 >= 0)
rule11_y0 = Real('rule11_y0')
s.add(rule11_y0 >= 0)
rule12_y0 = Real('rule12_y0')
s.add(rule12_y0 >= 0)
rule13_y0 = Real('rule13_y0')
s.add(rule13_y0 >= 0)
rule14_y0 = Real('rule14_y0')
s.add(rule14_y0 >= 0)
rule15_y0 = Real('rule15_y0')
s.add(rule15_y0 >= 0)
rule16_y0 = Real('rule16_y0')
s.add(rule16_y0 >= 0)
rule17_y0 = Real('rule17_y0')
s.add(rule17_y0 >= 0)
rule18_y0 = Real('rule18_y0')
s.add(rule18_y0 >= 0)
rule19_y0 = Real('rule19_y0')
s.add(rule19_y0 >= 0)
rule20_y0 = Real('rule20_y0')
s.add(rule20_y0 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule13_y0 - rule14_y0 + rule14_y0 - rule15_y0 - rule16_y0 ==  loc0_0_x1 - loc0_0_y0)
s.add(0 + rule3_y0 + rule6_y0 + rule8_y0 + rule12_y0 + rule16_y0 + rule19_y0 - rule20_y0 + rule20_y0 ==  loc3_3_x1 - loc3_3_y0)
s.add(0 + rule15_y0 - rule17_y0 - rule18_y0 + rule18_y0 - rule19_y0 ==  loc1_0_x1 - loc1_0_y0)
s.add(0 + rule2_y0 + rule5_y0 - rule7_y0 + rule7_y0 - rule8_y0 + rule11_y0 + rule13_y0 + rule17_y0 ==  loc2_2_x1 - loc2_2_y0)
s.add(0 - rule9_y0 - rule10_y0 - rule11_y0 - rule12_y0 ==  loc0_1_x1 - loc0_1_y0)
s.add(0 + rule1_y0 - rule4_y0 + rule4_y0 - rule5_y0 - rule6_y0 + rule10_y0 ==  loc1_2_x1 - loc1_2_y0)
s.add(0 - rule0_y0 + rule0_y0 - rule1_y0 - rule2_y0 - rule3_y0 + rule9_y0 ==  loc0_2_x1 - loc0_2_y0)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule9_y0 + rule10_y0 + rule11_y0 + rule12_y0 + rule13_y0 + rule16_y0 + rule17_y0 + rule19_y0 == nsnt_x1 - nsnt_y0)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y0 > 0), And(True, ) ))
s.add(Implies( (rule1_y0 > 0), And(nsnt_y0+F>=1, ) ))
s.add(Implies( (rule2_y0 > 0), And(nsnt_y0+F>=T+1, ) ))
s.add(Implies( (rule3_y0 > 0), And(nsnt_y0+F>=N-T, ) ))
s.add(Implies( (rule4_y0 > 0), And(nsnt_y0+F>=1, ) ))
s.add(Implies( (rule5_y0 > 0), And(nsnt_y0+F>=T+1, ) ))
s.add(Implies( (rule6_y0 > 0), And(nsnt_y0+F>=N-T, ) ))
s.add(Implies( (rule7_y0 > 0), And(nsnt_y0+F>=T+1, ) ))
s.add(Implies( (rule8_y0 > 0), And(nsnt_y0+F>=N-T, ) ))
s.add(Implies( (rule9_y0 > 0), And(True, ) ))
s.add(Implies( (rule10_y0 > 0), And(nsnt_y0+F>=1, ) ))
s.add(Implies( (rule11_y0 > 0), And(nsnt_y0+F>=T+1, ) ))
s.add(Implies( (rule12_y0 > 0), And(nsnt_y0+F>=N-T, ) ))
s.add(Implies( (rule13_y0 > 0), And(nsnt_y0+F>=T+1, ) ))
s.add(Implies( (rule14_y0 > 0), And(True, ) ))
s.add(Implies( (rule15_y0 > 0), And(nsnt_y0+F>=1, ) ))
s.add(Implies( (rule16_y0 > 0), And(nsnt_y0+F>=N-T, ) ))
s.add(Implies( (rule17_y0 > 0), And(nsnt_y0+F>=T+1, ) ))
s.add(Implies( (rule18_y0 > 0), And(nsnt_y0+F>=1, ) ))
s.add(Implies( (rule19_y0 > 0), And(nsnt_y0+F>=N-T, ) ))
s.add(Implies( (rule20_y0 > 0), And(nsnt_y0+F>=N-T, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y0 and x0, if a fall condition is present


####################################################################################

#Creating constraints for a run between the y1th and x2th configurations

################Step 1#################


#Creating many copies of variables for rules

rule0_y1 = Real('rule0_y1')
s.add(rule0_y1 >= 0)
rule1_y1 = Real('rule1_y1')
s.add(rule1_y1 >= 0)
rule2_y1 = Real('rule2_y1')
s.add(rule2_y1 >= 0)
rule3_y1 = Real('rule3_y1')
s.add(rule3_y1 >= 0)
rule4_y1 = Real('rule4_y1')
s.add(rule4_y1 >= 0)
rule5_y1 = Real('rule5_y1')
s.add(rule5_y1 >= 0)
rule6_y1 = Real('rule6_y1')
s.add(rule6_y1 >= 0)
rule7_y1 = Real('rule7_y1')
s.add(rule7_y1 >= 0)
rule8_y1 = Real('rule8_y1')
s.add(rule8_y1 >= 0)
rule9_y1 = Real('rule9_y1')
s.add(rule9_y1 >= 0)
rule10_y1 = Real('rule10_y1')
s.add(rule10_y1 >= 0)
rule11_y1 = Real('rule11_y1')
s.add(rule11_y1 >= 0)
rule12_y1 = Real('rule12_y1')
s.add(rule12_y1 >= 0)
rule13_y1 = Real('rule13_y1')
s.add(rule13_y1 >= 0)
rule14_y1 = Real('rule14_y1')
s.add(rule14_y1 >= 0)
rule15_y1 = Real('rule15_y1')
s.add(rule15_y1 >= 0)
rule16_y1 = Real('rule16_y1')
s.add(rule16_y1 >= 0)
rule17_y1 = Real('rule17_y1')
s.add(rule17_y1 >= 0)
rule18_y1 = Real('rule18_y1')
s.add(rule18_y1 >= 0)
rule19_y1 = Real('rule19_y1')
s.add(rule19_y1 >= 0)
rule20_y1 = Real('rule20_y1')
s.add(rule20_y1 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule13_y1 - rule14_y1 + rule14_y1 - rule15_y1 - rule16_y1 ==  loc0_0_x2 - loc0_0_y1)
s.add(0 + rule3_y1 + rule6_y1 + rule8_y1 + rule12_y1 + rule16_y1 + rule19_y1 - rule20_y1 + rule20_y1 ==  loc3_3_x2 - loc3_3_y1)
s.add(0 + rule15_y1 - rule17_y1 - rule18_y1 + rule18_y1 - rule19_y1 ==  loc1_0_x2 - loc1_0_y1)
s.add(0 + rule2_y1 + rule5_y1 - rule7_y1 + rule7_y1 - rule8_y1 + rule11_y1 + rule13_y1 + rule17_y1 ==  loc2_2_x2 - loc2_2_y1)
s.add(0 - rule9_y1 - rule10_y1 - rule11_y1 - rule12_y1 ==  loc0_1_x2 - loc0_1_y1)
s.add(0 + rule1_y1 - rule4_y1 + rule4_y1 - rule5_y1 - rule6_y1 + rule10_y1 ==  loc1_2_x2 - loc1_2_y1)
s.add(0 - rule0_y1 + rule0_y1 - rule1_y1 - rule2_y1 - rule3_y1 + rule9_y1 ==  loc0_2_x2 - loc0_2_y1)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule9_y1 + rule10_y1 + rule11_y1 + rule12_y1 + rule13_y1 + rule16_y1 + rule17_y1 + rule19_y1 == nsnt_x2 - nsnt_y1)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y1 > 0), And(True, ) ))
s.add(Implies( (rule1_y1 > 0), And(nsnt_y1+F>=1, ) ))
s.add(Implies( (rule2_y1 > 0), And(nsnt_y1+F>=T+1, ) ))
s.add(Implies( (rule3_y1 > 0), And(nsnt_y1+F>=N-T, ) ))
s.add(Implies( (rule4_y1 > 0), And(nsnt_y1+F>=1, ) ))
s.add(Implies( (rule5_y1 > 0), And(nsnt_y1+F>=T+1, ) ))
s.add(Implies( (rule6_y1 > 0), And(nsnt_y1+F>=N-T, ) ))
s.add(Implies( (rule7_y1 > 0), And(nsnt_y1+F>=T+1, ) ))
s.add(Implies( (rule8_y1 > 0), And(nsnt_y1+F>=N-T, ) ))
s.add(Implies( (rule9_y1 > 0), And(True, ) ))
s.add(Implies( (rule10_y1 > 0), And(nsnt_y1+F>=1, ) ))
s.add(Implies( (rule11_y1 > 0), And(nsnt_y1+F>=T+1, ) ))
s.add(Implies( (rule12_y1 > 0), And(nsnt_y1+F>=N-T, ) ))
s.add(Implies( (rule13_y1 > 0), And(nsnt_y1+F>=T+1, ) ))
s.add(Implies( (rule14_y1 > 0), And(True, ) ))
s.add(Implies( (rule15_y1 > 0), And(nsnt_y1+F>=1, ) ))
s.add(Implies( (rule16_y1 > 0), And(nsnt_y1+F>=N-T, ) ))
s.add(Implies( (rule17_y1 > 0), And(nsnt_y1+F>=T+1, ) ))
s.add(Implies( (rule18_y1 > 0), And(nsnt_y1+F>=1, ) ))
s.add(Implies( (rule19_y1 > 0), And(nsnt_y1+F>=N-T, ) ))
s.add(Implies( (rule20_y1 > 0), And(nsnt_y1+F>=N-T, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y1 and x1, if a fall condition is present


####################################################################################

#Creating constraints for a run between the y2th and x3th configurations

################Step 1#################


#Creating many copies of variables for rules

rule0_y2 = Real('rule0_y2')
s.add(rule0_y2 >= 0)
rule1_y2 = Real('rule1_y2')
s.add(rule1_y2 >= 0)
rule2_y2 = Real('rule2_y2')
s.add(rule2_y2 >= 0)
rule3_y2 = Real('rule3_y2')
s.add(rule3_y2 >= 0)
rule4_y2 = Real('rule4_y2')
s.add(rule4_y2 >= 0)
rule5_y2 = Real('rule5_y2')
s.add(rule5_y2 >= 0)
rule6_y2 = Real('rule6_y2')
s.add(rule6_y2 >= 0)
rule7_y2 = Real('rule7_y2')
s.add(rule7_y2 >= 0)
rule8_y2 = Real('rule8_y2')
s.add(rule8_y2 >= 0)
rule9_y2 = Real('rule9_y2')
s.add(rule9_y2 >= 0)
rule10_y2 = Real('rule10_y2')
s.add(rule10_y2 >= 0)
rule11_y2 = Real('rule11_y2')
s.add(rule11_y2 >= 0)
rule12_y2 = Real('rule12_y2')
s.add(rule12_y2 >= 0)
rule13_y2 = Real('rule13_y2')
s.add(rule13_y2 >= 0)
rule14_y2 = Real('rule14_y2')
s.add(rule14_y2 >= 0)
rule15_y2 = Real('rule15_y2')
s.add(rule15_y2 >= 0)
rule16_y2 = Real('rule16_y2')
s.add(rule16_y2 >= 0)
rule17_y2 = Real('rule17_y2')
s.add(rule17_y2 >= 0)
rule18_y2 = Real('rule18_y2')
s.add(rule18_y2 >= 0)
rule19_y2 = Real('rule19_y2')
s.add(rule19_y2 >= 0)
rule20_y2 = Real('rule20_y2')
s.add(rule20_y2 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule13_y2 - rule14_y2 + rule14_y2 - rule15_y2 - rule16_y2 ==  loc0_0_x3 - loc0_0_y2)
s.add(0 + rule3_y2 + rule6_y2 + rule8_y2 + rule12_y2 + rule16_y2 + rule19_y2 - rule20_y2 + rule20_y2 ==  loc3_3_x3 - loc3_3_y2)
s.add(0 + rule15_y2 - rule17_y2 - rule18_y2 + rule18_y2 - rule19_y2 ==  loc1_0_x3 - loc1_0_y2)
s.add(0 + rule2_y2 + rule5_y2 - rule7_y2 + rule7_y2 - rule8_y2 + rule11_y2 + rule13_y2 + rule17_y2 ==  loc2_2_x3 - loc2_2_y2)
s.add(0 - rule9_y2 - rule10_y2 - rule11_y2 - rule12_y2 ==  loc0_1_x3 - loc0_1_y2)
s.add(0 + rule1_y2 - rule4_y2 + rule4_y2 - rule5_y2 - rule6_y2 + rule10_y2 ==  loc1_2_x3 - loc1_2_y2)
s.add(0 - rule0_y2 + rule0_y2 - rule1_y2 - rule2_y2 - rule3_y2 + rule9_y2 ==  loc0_2_x3 - loc0_2_y2)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule9_y2 + rule10_y2 + rule11_y2 + rule12_y2 + rule13_y2 + rule16_y2 + rule17_y2 + rule19_y2 == nsnt_x3 - nsnt_y2)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y2 > 0), And(True, ) ))
s.add(Implies( (rule1_y2 > 0), And(nsnt_y2+F>=1, ) ))
s.add(Implies( (rule2_y2 > 0), And(nsnt_y2+F>=T+1, ) ))
s.add(Implies( (rule3_y2 > 0), And(nsnt_y2+F>=N-T, ) ))
s.add(Implies( (rule4_y2 > 0), And(nsnt_y2+F>=1, ) ))
s.add(Implies( (rule5_y2 > 0), And(nsnt_y2+F>=T+1, ) ))
s.add(Implies( (rule6_y2 > 0), And(nsnt_y2+F>=N-T, ) ))
s.add(Implies( (rule7_y2 > 0), And(nsnt_y2+F>=T+1, ) ))
s.add(Implies( (rule8_y2 > 0), And(nsnt_y2+F>=N-T, ) ))
s.add(Implies( (rule9_y2 > 0), And(True, ) ))
s.add(Implies( (rule10_y2 > 0), And(nsnt_y2+F>=1, ) ))
s.add(Implies( (rule11_y2 > 0), And(nsnt_y2+F>=T+1, ) ))
s.add(Implies( (rule12_y2 > 0), And(nsnt_y2+F>=N-T, ) ))
s.add(Implies( (rule13_y2 > 0), And(nsnt_y2+F>=T+1, ) ))
s.add(Implies( (rule14_y2 > 0), And(True, ) ))
s.add(Implies( (rule15_y2 > 0), And(nsnt_y2+F>=1, ) ))
s.add(Implies( (rule16_y2 > 0), And(nsnt_y2+F>=N-T, ) ))
s.add(Implies( (rule17_y2 > 0), And(nsnt_y2+F>=T+1, ) ))
s.add(Implies( (rule18_y2 > 0), And(nsnt_y2+F>=1, ) ))
s.add(Implies( (rule19_y2 > 0), And(nsnt_y2+F>=N-T, ) ))
s.add(Implies( (rule20_y2 > 0), And(nsnt_y2+F>=N-T, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y2 and x2, if a fall condition is present


####################################################################################

#Creating constraints for a run between the y3th and x4th configurations

################Step 1#################


#Creating many copies of variables for rules

rule0_y3 = Real('rule0_y3')
s.add(rule0_y3 >= 0)
rule1_y3 = Real('rule1_y3')
s.add(rule1_y3 >= 0)
rule2_y3 = Real('rule2_y3')
s.add(rule2_y3 >= 0)
rule3_y3 = Real('rule3_y3')
s.add(rule3_y3 >= 0)
rule4_y3 = Real('rule4_y3')
s.add(rule4_y3 >= 0)
rule5_y3 = Real('rule5_y3')
s.add(rule5_y3 >= 0)
rule6_y3 = Real('rule6_y3')
s.add(rule6_y3 >= 0)
rule7_y3 = Real('rule7_y3')
s.add(rule7_y3 >= 0)
rule8_y3 = Real('rule8_y3')
s.add(rule8_y3 >= 0)
rule9_y3 = Real('rule9_y3')
s.add(rule9_y3 >= 0)
rule10_y3 = Real('rule10_y3')
s.add(rule10_y3 >= 0)
rule11_y3 = Real('rule11_y3')
s.add(rule11_y3 >= 0)
rule12_y3 = Real('rule12_y3')
s.add(rule12_y3 >= 0)
rule13_y3 = Real('rule13_y3')
s.add(rule13_y3 >= 0)
rule14_y3 = Real('rule14_y3')
s.add(rule14_y3 >= 0)
rule15_y3 = Real('rule15_y3')
s.add(rule15_y3 >= 0)
rule16_y3 = Real('rule16_y3')
s.add(rule16_y3 >= 0)
rule17_y3 = Real('rule17_y3')
s.add(rule17_y3 >= 0)
rule18_y3 = Real('rule18_y3')
s.add(rule18_y3 >= 0)
rule19_y3 = Real('rule19_y3')
s.add(rule19_y3 >= 0)
rule20_y3 = Real('rule20_y3')
s.add(rule20_y3 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule13_y3 - rule14_y3 + rule14_y3 - rule15_y3 - rule16_y3 ==  loc0_0_x4 - loc0_0_y3)
s.add(0 + rule3_y3 + rule6_y3 + rule8_y3 + rule12_y3 + rule16_y3 + rule19_y3 - rule20_y3 + rule20_y3 ==  loc3_3_x4 - loc3_3_y3)
s.add(0 + rule15_y3 - rule17_y3 - rule18_y3 + rule18_y3 - rule19_y3 ==  loc1_0_x4 - loc1_0_y3)
s.add(0 + rule2_y3 + rule5_y3 - rule7_y3 + rule7_y3 - rule8_y3 + rule11_y3 + rule13_y3 + rule17_y3 ==  loc2_2_x4 - loc2_2_y3)
s.add(0 - rule9_y3 - rule10_y3 - rule11_y3 - rule12_y3 ==  loc0_1_x4 - loc0_1_y3)
s.add(0 + rule1_y3 - rule4_y3 + rule4_y3 - rule5_y3 - rule6_y3 + rule10_y3 ==  loc1_2_x4 - loc1_2_y3)
s.add(0 - rule0_y3 + rule0_y3 - rule1_y3 - rule2_y3 - rule3_y3 + rule9_y3 ==  loc0_2_x4 - loc0_2_y3)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule9_y3 + rule10_y3 + rule11_y3 + rule12_y3 + rule13_y3 + rule16_y3 + rule17_y3 + rule19_y3 == nsnt_x4 - nsnt_y3)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y3 > 0), And(True, ) ))
s.add(Implies( (rule1_y3 > 0), And(nsnt_y3+F>=1, ) ))
s.add(Implies( (rule2_y3 > 0), And(nsnt_y3+F>=T+1, ) ))
s.add(Implies( (rule3_y3 > 0), And(nsnt_y3+F>=N-T, ) ))
s.add(Implies( (rule4_y3 > 0), And(nsnt_y3+F>=1, ) ))
s.add(Implies( (rule5_y3 > 0), And(nsnt_y3+F>=T+1, ) ))
s.add(Implies( (rule6_y3 > 0), And(nsnt_y3+F>=N-T, ) ))
s.add(Implies( (rule7_y3 > 0), And(nsnt_y3+F>=T+1, ) ))
s.add(Implies( (rule8_y3 > 0), And(nsnt_y3+F>=N-T, ) ))
s.add(Implies( (rule9_y3 > 0), And(True, ) ))
s.add(Implies( (rule10_y3 > 0), And(nsnt_y3+F>=1, ) ))
s.add(Implies( (rule11_y3 > 0), And(nsnt_y3+F>=T+1, ) ))
s.add(Implies( (rule12_y3 > 0), And(nsnt_y3+F>=N-T, ) ))
s.add(Implies( (rule13_y3 > 0), And(nsnt_y3+F>=T+1, ) ))
s.add(Implies( (rule14_y3 > 0), And(True, ) ))
s.add(Implies( (rule15_y3 > 0), And(nsnt_y3+F>=1, ) ))
s.add(Implies( (rule16_y3 > 0), And(nsnt_y3+F>=N-T, ) ))
s.add(Implies( (rule17_y3 > 0), And(nsnt_y3+F>=T+1, ) ))
s.add(Implies( (rule18_y3 > 0), And(nsnt_y3+F>=1, ) ))
s.add(Implies( (rule19_y3 > 0), And(nsnt_y3+F>=N-T, ) ))
s.add(Implies( (rule20_y3 > 0), And(nsnt_y3+F>=N-T, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y3 and x3, if a fall condition is present


#############Additional step for the final configuration#####################


###########Ensure that the last configuration satisfies the final condition#############

s.add(loc3_3_y4 != 0)






if s.check() == sat:

	print("Specification not satisfied")

else:

	print("Specification satisfied")
