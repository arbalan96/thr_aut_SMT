from z3 import *
s = Solver()

#Declaring parameter variables

N = Real('N')
s.add(N >= 0)

#Adding the resilience condition

s.add(N > 1)

####################################################################################

#Creating constraints for a run between the x0th and y0th configurations

################Step 1#################


#Creating many copies of location variables

loc0_0_x0 = Real('loc0_0_x0')
loc0_0_y0 = Real('loc0_0_y0')
s.add(loc0_0_x0 >= 0)
s.add(loc0_0_y0 >= 0)
loc1_2_x0 = Real('loc1_2_x0')
loc1_2_y0 = Real('loc1_2_y0')
s.add(loc1_2_x0 >= 0)
s.add(loc1_2_y0 >= 0)
loc1_3_x0 = Real('loc1_3_x0')
loc1_3_y0 = Real('loc1_3_y0')
s.add(loc1_3_x0 >= 0)
s.add(loc1_3_y0 >= 0)
loc1_0_x0 = Real('loc1_0_x0')
loc1_0_y0 = Real('loc1_0_y0')
s.add(loc1_0_x0 >= 0)
s.add(loc1_0_y0 >= 0)
loc0_1_x0 = Real('loc0_1_x0')
loc0_1_y0 = Real('loc0_1_y0')
s.add(loc0_1_x0 >= 0)
s.add(loc0_1_y0 >= 0)
loc0_2_x0 = Real('loc0_2_x0')
loc0_2_y0 = Real('loc0_2_y0')
s.add(loc0_2_x0 >= 0)
s.add(loc0_2_y0 >= 0)
loc0_3_x0 = Real('loc0_3_x0')
loc0_3_y0 = Real('loc0_3_y0')
s.add(loc0_3_x0 >= 0)
s.add(loc0_3_y0 >= 0)






#Creating many copies of shared variables

nsnt_x0 = Real('nsnt_x0')
nsnt_y0 = Real('nsnt_y0')
s.add(nsnt_x0 >= 0)
s.add(nsnt_y0 >= 0)
nsntF_x0 = Real('nsntF_x0')
nsntF_y0 = Real('nsntF_y0')
s.add(nsntF_x0 >= 0)
s.add(nsntF_y0 >= 0)






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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule3_x0 - rule4_x0 + rule4_x0 - rule5_x0 - rule6_x0 ==  loc0_0_y0 - loc0_0_x0)
s.add(0 + rule2_x0 + rule6_x0 - rule7_x0 + rule7_x0 + rule8_x0 + rule12_x0 ==  loc1_2_y0 - loc1_2_x0)
s.add(0 + rule1_x0 + rule5_x0 + rule10_x0 ==  loc1_3_y0 - loc1_3_x0)
s.add(0 - rule0_x0 + rule0_x0 - rule1_x0 - rule2_x0 + rule3_x0 ==  loc1_0_y0 - loc1_0_x0)
s.add(0 - rule10_x0 - rule11_x0 - rule12_x0 - rule13_x0 ==  loc0_1_y0 - loc0_1_x0)
s.add(0 - rule8_x0 - rule9_x0 + rule9_x0 + rule13_x0 ==  loc0_2_y0 - loc0_2_x0)
s.add(0 + rule11_x0 ==  loc0_3_y0 - loc0_3_x0)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule2_x0 + rule6_x0 + rule12_x0 + rule13_x0 == nsnt_y0 - nsnt_x0)
s.add(0 + rule1_x0 + rule5_x0 + rule10_x0 + rule11_x0 == nsntF_y0 - nsntF_x0)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x0 > 0), And(nsnt_x0+nsntF_x0>=1, ) ))
s.add(Implies( (rule1_x0 > 0), And(nsnt_x0+nsntF_x0>=1, ) ))
s.add(Implies( (rule2_x0 > 0), And(nsnt_x0+nsntF_x0>=1, ) ))
s.add(Implies( (rule3_x0 > 0), And(nsnt_x0+nsntF_x0>=1, ) ))
s.add(Implies( (rule4_x0 > 0), And(True, ) ))
s.add(Implies( (rule5_x0 > 0), And(nsnt_x0+nsntF_x0>=1, ) ))
s.add(Implies( (rule6_x0 > 0), And(nsnt_x0+nsntF_x0>=1, ) ))
s.add(Implies( (rule7_x0 > 0), And(nsnt_x0+nsntF_x0>=1, ) ))
s.add(Implies( (rule8_x0 > 0), And(nsnt_x0+nsntF_x0>=1, ) ))
s.add(Implies( (rule9_x0 > 0), And(True, ) ))
s.add(Implies( (rule10_x0 > 0), And(nsnt_x0+nsntF_x0>=1, ) ))
s.add(Implies( (rule11_x0 > 0), And(True, ) ))
s.add(Implies( (rule12_x0 > 0), And(nsnt_x0+nsntF_x0>=1, ) ))
s.add(Implies( (rule13_x0 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x0 and y0 have the same context

s.add((True) == (True))
s.add((nsnt_x0+nsntF_x0>=1) == (nsnt_y0+nsntF_y0>=1))

#############Additional step for the initial configuration#####################


#############Ensure that the first configuration only contains initial locations###########

s.add((loc0_1_x0 + loc0_0_x0) == N)
s.add(loc0_2_x0 == 0)
s.add(loc1_2_x0 == 0)
s.add(loc0_3_x0 == 0)
s.add(loc1_3_x0 == 0)
s.add(loc1_0_x0 == 0)
s.add(nsnt_x0 == 0)
s.add(nsntF_x0 == 0)






###########Ensure that the first configuration satisfies the initial condition#############

s.add(And(loc0_3_x0 == 0, loc0_2_x0 == 0, loc0_1_x0 == 0, loc1_3_x0 == 0, loc1_2_x0 == 0))






####################################################################################

#Creating constraints for a run between the x1th and y1th configurations

################Step 1#################


#Creating many copies of location variables

loc0_0_x1 = Real('loc0_0_x1')
loc0_0_y1 = Real('loc0_0_y1')
s.add(loc0_0_x1 >= 0)
s.add(loc0_0_y1 >= 0)
loc1_2_x1 = Real('loc1_2_x1')
loc1_2_y1 = Real('loc1_2_y1')
s.add(loc1_2_x1 >= 0)
s.add(loc1_2_y1 >= 0)
loc1_3_x1 = Real('loc1_3_x1')
loc1_3_y1 = Real('loc1_3_y1')
s.add(loc1_3_x1 >= 0)
s.add(loc1_3_y1 >= 0)
loc1_0_x1 = Real('loc1_0_x1')
loc1_0_y1 = Real('loc1_0_y1')
s.add(loc1_0_x1 >= 0)
s.add(loc1_0_y1 >= 0)
loc0_1_x1 = Real('loc0_1_x1')
loc0_1_y1 = Real('loc0_1_y1')
s.add(loc0_1_x1 >= 0)
s.add(loc0_1_y1 >= 0)
loc0_2_x1 = Real('loc0_2_x1')
loc0_2_y1 = Real('loc0_2_y1')
s.add(loc0_2_x1 >= 0)
s.add(loc0_2_y1 >= 0)
loc0_3_x1 = Real('loc0_3_x1')
loc0_3_y1 = Real('loc0_3_y1')
s.add(loc0_3_x1 >= 0)
s.add(loc0_3_y1 >= 0)






#Creating many copies of shared variables

nsnt_x1 = Real('nsnt_x1')
nsnt_y1 = Real('nsnt_y1')
s.add(nsnt_x1 >= 0)
s.add(nsnt_y1 >= 0)
nsntF_x1 = Real('nsntF_x1')
nsntF_y1 = Real('nsntF_y1')
s.add(nsntF_x1 >= 0)
s.add(nsntF_y1 >= 0)






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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule3_x1 - rule4_x1 + rule4_x1 - rule5_x1 - rule6_x1 ==  loc0_0_y1 - loc0_0_x1)
s.add(0 + rule2_x1 + rule6_x1 - rule7_x1 + rule7_x1 + rule8_x1 + rule12_x1 ==  loc1_2_y1 - loc1_2_x1)
s.add(0 + rule1_x1 + rule5_x1 + rule10_x1 ==  loc1_3_y1 - loc1_3_x1)
s.add(0 - rule0_x1 + rule0_x1 - rule1_x1 - rule2_x1 + rule3_x1 ==  loc1_0_y1 - loc1_0_x1)
s.add(0 - rule10_x1 - rule11_x1 - rule12_x1 - rule13_x1 ==  loc0_1_y1 - loc0_1_x1)
s.add(0 - rule8_x1 - rule9_x1 + rule9_x1 + rule13_x1 ==  loc0_2_y1 - loc0_2_x1)
s.add(0 + rule11_x1 ==  loc0_3_y1 - loc0_3_x1)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule2_x1 + rule6_x1 + rule12_x1 + rule13_x1 == nsnt_y1 - nsnt_x1)
s.add(0 + rule1_x1 + rule5_x1 + rule10_x1 + rule11_x1 == nsntF_y1 - nsntF_x1)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x1 > 0), And(nsnt_x1+nsntF_x1>=1, ) ))
s.add(Implies( (rule1_x1 > 0), And(nsnt_x1+nsntF_x1>=1, ) ))
s.add(Implies( (rule2_x1 > 0), And(nsnt_x1+nsntF_x1>=1, ) ))
s.add(Implies( (rule3_x1 > 0), And(nsnt_x1+nsntF_x1>=1, ) ))
s.add(Implies( (rule4_x1 > 0), And(True, ) ))
s.add(Implies( (rule5_x1 > 0), And(nsnt_x1+nsntF_x1>=1, ) ))
s.add(Implies( (rule6_x1 > 0), And(nsnt_x1+nsntF_x1>=1, ) ))
s.add(Implies( (rule7_x1 > 0), And(nsnt_x1+nsntF_x1>=1, ) ))
s.add(Implies( (rule8_x1 > 0), And(nsnt_x1+nsntF_x1>=1, ) ))
s.add(Implies( (rule9_x1 > 0), And(True, ) ))
s.add(Implies( (rule10_x1 > 0), And(nsnt_x1+nsntF_x1>=1, ) ))
s.add(Implies( (rule11_x1 > 0), And(True, ) ))
s.add(Implies( (rule12_x1 > 0), And(nsnt_x1+nsntF_x1>=1, ) ))
s.add(Implies( (rule13_x1 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x1 and y1 have the same context

s.add((True) == (True))
s.add((nsnt_x1+nsntF_x1>=1) == (nsnt_y1+nsntF_y1>=1))

####################################################################################

#Creating constraints for a run between the x2th and y2th configurations

################Step 1#################


#Creating many copies of location variables

loc0_0_x2 = Real('loc0_0_x2')
loc0_0_y2 = Real('loc0_0_y2')
s.add(loc0_0_x2 >= 0)
s.add(loc0_0_y2 >= 0)
loc1_2_x2 = Real('loc1_2_x2')
loc1_2_y2 = Real('loc1_2_y2')
s.add(loc1_2_x2 >= 0)
s.add(loc1_2_y2 >= 0)
loc1_3_x2 = Real('loc1_3_x2')
loc1_3_y2 = Real('loc1_3_y2')
s.add(loc1_3_x2 >= 0)
s.add(loc1_3_y2 >= 0)
loc1_0_x2 = Real('loc1_0_x2')
loc1_0_y2 = Real('loc1_0_y2')
s.add(loc1_0_x2 >= 0)
s.add(loc1_0_y2 >= 0)
loc0_1_x2 = Real('loc0_1_x2')
loc0_1_y2 = Real('loc0_1_y2')
s.add(loc0_1_x2 >= 0)
s.add(loc0_1_y2 >= 0)
loc0_2_x2 = Real('loc0_2_x2')
loc0_2_y2 = Real('loc0_2_y2')
s.add(loc0_2_x2 >= 0)
s.add(loc0_2_y2 >= 0)
loc0_3_x2 = Real('loc0_3_x2')
loc0_3_y2 = Real('loc0_3_y2')
s.add(loc0_3_x2 >= 0)
s.add(loc0_3_y2 >= 0)






#Creating many copies of shared variables

nsnt_x2 = Real('nsnt_x2')
nsnt_y2 = Real('nsnt_y2')
s.add(nsnt_x2 >= 0)
s.add(nsnt_y2 >= 0)
nsntF_x2 = Real('nsntF_x2')
nsntF_y2 = Real('nsntF_y2')
s.add(nsntF_x2 >= 0)
s.add(nsntF_y2 >= 0)






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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule3_x2 - rule4_x2 + rule4_x2 - rule5_x2 - rule6_x2 ==  loc0_0_y2 - loc0_0_x2)
s.add(0 + rule2_x2 + rule6_x2 - rule7_x2 + rule7_x2 + rule8_x2 + rule12_x2 ==  loc1_2_y2 - loc1_2_x2)
s.add(0 + rule1_x2 + rule5_x2 + rule10_x2 ==  loc1_3_y2 - loc1_3_x2)
s.add(0 - rule0_x2 + rule0_x2 - rule1_x2 - rule2_x2 + rule3_x2 ==  loc1_0_y2 - loc1_0_x2)
s.add(0 - rule10_x2 - rule11_x2 - rule12_x2 - rule13_x2 ==  loc0_1_y2 - loc0_1_x2)
s.add(0 - rule8_x2 - rule9_x2 + rule9_x2 + rule13_x2 ==  loc0_2_y2 - loc0_2_x2)
s.add(0 + rule11_x2 ==  loc0_3_y2 - loc0_3_x2)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule2_x2 + rule6_x2 + rule12_x2 + rule13_x2 == nsnt_y2 - nsnt_x2)
s.add(0 + rule1_x2 + rule5_x2 + rule10_x2 + rule11_x2 == nsntF_y2 - nsntF_x2)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x2 > 0), And(nsnt_x2+nsntF_x2>=1, ) ))
s.add(Implies( (rule1_x2 > 0), And(nsnt_x2+nsntF_x2>=1, ) ))
s.add(Implies( (rule2_x2 > 0), And(nsnt_x2+nsntF_x2>=1, ) ))
s.add(Implies( (rule3_x2 > 0), And(nsnt_x2+nsntF_x2>=1, ) ))
s.add(Implies( (rule4_x2 > 0), And(True, ) ))
s.add(Implies( (rule5_x2 > 0), And(nsnt_x2+nsntF_x2>=1, ) ))
s.add(Implies( (rule6_x2 > 0), And(nsnt_x2+nsntF_x2>=1, ) ))
s.add(Implies( (rule7_x2 > 0), And(nsnt_x2+nsntF_x2>=1, ) ))
s.add(Implies( (rule8_x2 > 0), And(nsnt_x2+nsntF_x2>=1, ) ))
s.add(Implies( (rule9_x2 > 0), And(True, ) ))
s.add(Implies( (rule10_x2 > 0), And(nsnt_x2+nsntF_x2>=1, ) ))
s.add(Implies( (rule11_x2 > 0), And(True, ) ))
s.add(Implies( (rule12_x2 > 0), And(nsnt_x2+nsntF_x2>=1, ) ))
s.add(Implies( (rule13_x2 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x2 and y2 have the same context

s.add((True) == (True))
s.add((nsnt_x2+nsntF_x2>=1) == (nsnt_y2+nsntF_y2>=1))

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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule3_y0 - rule4_y0 + rule4_y0 - rule5_y0 - rule6_y0 ==  loc0_0_x1 - loc0_0_y0)
s.add(0 + rule2_y0 + rule6_y0 - rule7_y0 + rule7_y0 + rule8_y0 + rule12_y0 ==  loc1_2_x1 - loc1_2_y0)
s.add(0 + rule1_y0 + rule5_y0 + rule10_y0 ==  loc1_3_x1 - loc1_3_y0)
s.add(0 - rule0_y0 + rule0_y0 - rule1_y0 - rule2_y0 + rule3_y0 ==  loc1_0_x1 - loc1_0_y0)
s.add(0 - rule10_y0 - rule11_y0 - rule12_y0 - rule13_y0 ==  loc0_1_x1 - loc0_1_y0)
s.add(0 - rule8_y0 - rule9_y0 + rule9_y0 + rule13_y0 ==  loc0_2_x1 - loc0_2_y0)
s.add(0 + rule11_y0 ==  loc0_3_x1 - loc0_3_y0)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule2_y0 + rule6_y0 + rule12_y0 + rule13_y0 == nsnt_x1 - nsnt_y0)
s.add(0 + rule1_y0 + rule5_y0 + rule10_y0 + rule11_y0 == nsntF_x1 - nsntF_y0)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y0 > 0), And(nsnt_y0+nsntF_y0>=1, ) ))
s.add(Implies( (rule1_y0 > 0), And(nsnt_y0+nsntF_y0>=1, ) ))
s.add(Implies( (rule2_y0 > 0), And(nsnt_y0+nsntF_y0>=1, ) ))
s.add(Implies( (rule3_y0 > 0), And(nsnt_y0+nsntF_y0>=1, ) ))
s.add(Implies( (rule4_y0 > 0), And(True, ) ))
s.add(Implies( (rule5_y0 > 0), And(nsnt_y0+nsntF_y0>=1, ) ))
s.add(Implies( (rule6_y0 > 0), And(nsnt_y0+nsntF_y0>=1, ) ))
s.add(Implies( (rule7_y0 > 0), And(nsnt_y0+nsntF_y0>=1, ) ))
s.add(Implies( (rule8_y0 > 0), And(nsnt_y0+nsntF_y0>=1, ) ))
s.add(Implies( (rule9_y0 > 0), And(True, ) ))
s.add(Implies( (rule10_y0 > 0), And(nsnt_y0+nsntF_y0>=1, ) ))
s.add(Implies( (rule11_y0 > 0), And(True, ) ))
s.add(Implies( (rule12_y0 > 0), And(nsnt_y0+nsntF_y0>=1, ) ))
s.add(Implies( (rule13_y0 > 0), And(True, ) ))

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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule3_y1 - rule4_y1 + rule4_y1 - rule5_y1 - rule6_y1 ==  loc0_0_x2 - loc0_0_y1)
s.add(0 + rule2_y1 + rule6_y1 - rule7_y1 + rule7_y1 + rule8_y1 + rule12_y1 ==  loc1_2_x2 - loc1_2_y1)
s.add(0 + rule1_y1 + rule5_y1 + rule10_y1 ==  loc1_3_x2 - loc1_3_y1)
s.add(0 - rule0_y1 + rule0_y1 - rule1_y1 - rule2_y1 + rule3_y1 ==  loc1_0_x2 - loc1_0_y1)
s.add(0 - rule10_y1 - rule11_y1 - rule12_y1 - rule13_y1 ==  loc0_1_x2 - loc0_1_y1)
s.add(0 - rule8_y1 - rule9_y1 + rule9_y1 + rule13_y1 ==  loc0_2_x2 - loc0_2_y1)
s.add(0 + rule11_y1 ==  loc0_3_x2 - loc0_3_y1)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule2_y1 + rule6_y1 + rule12_y1 + rule13_y1 == nsnt_x2 - nsnt_y1)
s.add(0 + rule1_y1 + rule5_y1 + rule10_y1 + rule11_y1 == nsntF_x2 - nsntF_y1)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y1 > 0), And(nsnt_y1+nsntF_y1>=1, ) ))
s.add(Implies( (rule1_y1 > 0), And(nsnt_y1+nsntF_y1>=1, ) ))
s.add(Implies( (rule2_y1 > 0), And(nsnt_y1+nsntF_y1>=1, ) ))
s.add(Implies( (rule3_y1 > 0), And(nsnt_y1+nsntF_y1>=1, ) ))
s.add(Implies( (rule4_y1 > 0), And(True, ) ))
s.add(Implies( (rule5_y1 > 0), And(nsnt_y1+nsntF_y1>=1, ) ))
s.add(Implies( (rule6_y1 > 0), And(nsnt_y1+nsntF_y1>=1, ) ))
s.add(Implies( (rule7_y1 > 0), And(nsnt_y1+nsntF_y1>=1, ) ))
s.add(Implies( (rule8_y1 > 0), And(nsnt_y1+nsntF_y1>=1, ) ))
s.add(Implies( (rule9_y1 > 0), And(True, ) ))
s.add(Implies( (rule10_y1 > 0), And(nsnt_y1+nsntF_y1>=1, ) ))
s.add(Implies( (rule11_y1 > 0), And(True, ) ))
s.add(Implies( (rule12_y1 > 0), And(nsnt_y1+nsntF_y1>=1, ) ))
s.add(Implies( (rule13_y1 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y1 and x1, if a fall condition is present


#############Additional step for the final configuration#####################


###########Ensure that the last configuration satisfies the final condition#############

s.add(Or(loc0_2_y2 != 0, loc1_2_y2 != 0))






if s.check() == sat:

	print("Specification not satisfied")

else:

	print("Specification satisfied")
