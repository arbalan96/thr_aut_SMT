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

s.add(N >= 1)
s.add(N > T)
s.add(T >= F)

####################################################################################

#Creating constraints for a run between the x0th and y0th configurations

################Step 1#################


#Creating many copies of location variables

loc0_x0 = Real('loc0_x0')
loc0_y0 = Real('loc0_y0')
s.add(loc0_x0 >= 0)
s.add(loc0_y0 >= 0)
loc1_x0 = Real('loc1_x0')
loc1_y0 = Real('loc1_y0')
s.add(loc1_x0 >= 0)
s.add(loc1_y0 >= 0)
locCR_x0 = Real('locCR_x0')
locCR_y0 = Real('locCR_y0')
s.add(locCR_x0 >= 0)
s.add(locCR_y0 >= 0)
locAC_x0 = Real('locAC_x0')
locAC_y0 = Real('locAC_y0')
s.add(locAC_x0 >= 0)
s.add(locAC_y0 >= 0)






#Creating many copies of shared variables

nsnt_x0 = Real('nsnt_x0')
nsnt_y0 = Real('nsnt_y0')
s.add(nsnt_x0 >= 0)
s.add(nsnt_y0 >= 0)
nsntF_x0 = Real('nsntF_x0')
nsntF_y0 = Real('nsntF_y0')
s.add(nsntF_x0 >= 0)
s.add(nsntF_y0 >= 0)
nfaulty_x0 = Real('nfaulty_x0')
nfaulty_y0 = Real('nfaulty_y0')
s.add(nfaulty_x0 >= 0)
s.add(nfaulty_y0 >= 0)






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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x0 - rule5_x0 - rule6_x0 + rule6_x0 ==  loc0_y0 - loc0_x0)
s.add(0 - rule1_x0 - rule2_x0 - rule4_x0 - rule7_x0 + rule7_x0 ==  loc1_y0 - loc1_x0)
s.add(0 + rule0_x0 + rule1_x0 + rule2_x0 + rule3_x0 ==  locCR_y0 - locCR_x0)
s.add(0 - rule3_x0 + rule4_x0 + rule5_x0 - rule8_x0 + rule8_x0 ==  locAC_y0 - locAC_x0)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule4_x0 + rule5_x0 == nsnt_y0 - nsnt_x0)
s.add(0 + rule2_x0 == nsntF_y0 - nsntF_x0)
s.add(0 + rule0_x0 + rule1_x0 + rule2_x0 + rule3_x0 == nfaulty_y0 - nfaulty_x0)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x0 > 0), And(nfaulty_x0<F, ) ))
s.add(Implies( (rule1_x0 > 0), And(nfaulty_x0<F, ) ))
s.add(Implies( (rule2_x0 > 0), And(nfaulty_x0<F, ) ))
s.add(Implies( (rule3_x0 > 0), And(nfaulty_x0<F, ) ))
s.add(Implies( (rule4_x0 > 0), And(nsnt_x0>=0, ) ))
s.add(Implies( (rule5_x0 > 0), And(nsnt_x0>=1, ) ))
s.add(Implies( (rule6_x0 > 0), And(nsnt_x0>=0, ) ))
s.add(Implies( (rule7_x0 > 0), And(nsnt_x0>=0, ) ))
s.add(Implies( (rule8_x0 > 0), And(nsnt_x0>=0, ) ))

##################Step 5#########################


#Ensuring that configurations x0 and y0 have the same context

s.add((nsnt_x0>=1) == (nsnt_y0>=1))
s.add((nsnt_x0>=0) == (nsnt_y0>=0))
s.add((nfaulty_x0<F) == (nfaulty_y0<F))

#############Additional step for the initial configuration#####################


#############Ensure that the first configuration only contains initial locations###########

s.add((loc0_x0 + loc1_x0) == N)
s.add(locCR_x0 == 0)
s.add(locAC_x0 == 0)
s.add(nsnt_x0 == 0)
s.add(nsntF_x0 == 0)
s.add(nfaulty_x0 == 0)






###########Ensure that the first configuration satisfies the initial condition#############

s.add(And(loc1_x0 == 0, loc1_x0 == 0))






####################################################################################

#Creating constraints for a run between the x1th and y1th configurations

################Step 1#################


#Creating many copies of location variables

loc0_x1 = Real('loc0_x1')
loc0_y1 = Real('loc0_y1')
s.add(loc0_x1 >= 0)
s.add(loc0_y1 >= 0)
loc1_x1 = Real('loc1_x1')
loc1_y1 = Real('loc1_y1')
s.add(loc1_x1 >= 0)
s.add(loc1_y1 >= 0)
locCR_x1 = Real('locCR_x1')
locCR_y1 = Real('locCR_y1')
s.add(locCR_x1 >= 0)
s.add(locCR_y1 >= 0)
locAC_x1 = Real('locAC_x1')
locAC_y1 = Real('locAC_y1')
s.add(locAC_x1 >= 0)
s.add(locAC_y1 >= 0)






#Creating many copies of shared variables

nsnt_x1 = Real('nsnt_x1')
nsnt_y1 = Real('nsnt_y1')
s.add(nsnt_x1 >= 0)
s.add(nsnt_y1 >= 0)
nsntF_x1 = Real('nsntF_x1')
nsntF_y1 = Real('nsntF_y1')
s.add(nsntF_x1 >= 0)
s.add(nsntF_y1 >= 0)
nfaulty_x1 = Real('nfaulty_x1')
nfaulty_y1 = Real('nfaulty_y1')
s.add(nfaulty_x1 >= 0)
s.add(nfaulty_y1 >= 0)






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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x1 - rule5_x1 - rule6_x1 + rule6_x1 ==  loc0_y1 - loc0_x1)
s.add(0 - rule1_x1 - rule2_x1 - rule4_x1 - rule7_x1 + rule7_x1 ==  loc1_y1 - loc1_x1)
s.add(0 + rule0_x1 + rule1_x1 + rule2_x1 + rule3_x1 ==  locCR_y1 - locCR_x1)
s.add(0 - rule3_x1 + rule4_x1 + rule5_x1 - rule8_x1 + rule8_x1 ==  locAC_y1 - locAC_x1)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule4_x1 + rule5_x1 == nsnt_y1 - nsnt_x1)
s.add(0 + rule2_x1 == nsntF_y1 - nsntF_x1)
s.add(0 + rule0_x1 + rule1_x1 + rule2_x1 + rule3_x1 == nfaulty_y1 - nfaulty_x1)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x1 > 0), And(nfaulty_x1<F, ) ))
s.add(Implies( (rule1_x1 > 0), And(nfaulty_x1<F, ) ))
s.add(Implies( (rule2_x1 > 0), And(nfaulty_x1<F, ) ))
s.add(Implies( (rule3_x1 > 0), And(nfaulty_x1<F, ) ))
s.add(Implies( (rule4_x1 > 0), And(nsnt_x1>=0, ) ))
s.add(Implies( (rule5_x1 > 0), And(nsnt_x1>=1, ) ))
s.add(Implies( (rule6_x1 > 0), And(nsnt_x1>=0, ) ))
s.add(Implies( (rule7_x1 > 0), And(nsnt_x1>=0, ) ))
s.add(Implies( (rule8_x1 > 0), And(nsnt_x1>=0, ) ))

##################Step 5#########################


#Ensuring that configurations x1 and y1 have the same context

s.add((nsnt_x1>=1) == (nsnt_y1>=1))
s.add((nsnt_x1>=0) == (nsnt_y1>=0))
s.add((nfaulty_x1<F) == (nfaulty_y1<F))

####################################################################################

#Creating constraints for a run between the x2th and y2th configurations

################Step 1#################


#Creating many copies of location variables

loc0_x2 = Real('loc0_x2')
loc0_y2 = Real('loc0_y2')
s.add(loc0_x2 >= 0)
s.add(loc0_y2 >= 0)
loc1_x2 = Real('loc1_x2')
loc1_y2 = Real('loc1_y2')
s.add(loc1_x2 >= 0)
s.add(loc1_y2 >= 0)
locCR_x2 = Real('locCR_x2')
locCR_y2 = Real('locCR_y2')
s.add(locCR_x2 >= 0)
s.add(locCR_y2 >= 0)
locAC_x2 = Real('locAC_x2')
locAC_y2 = Real('locAC_y2')
s.add(locAC_x2 >= 0)
s.add(locAC_y2 >= 0)






#Creating many copies of shared variables

nsnt_x2 = Real('nsnt_x2')
nsnt_y2 = Real('nsnt_y2')
s.add(nsnt_x2 >= 0)
s.add(nsnt_y2 >= 0)
nsntF_x2 = Real('nsntF_x2')
nsntF_y2 = Real('nsntF_y2')
s.add(nsntF_x2 >= 0)
s.add(nsntF_y2 >= 0)
nfaulty_x2 = Real('nfaulty_x2')
nfaulty_y2 = Real('nfaulty_y2')
s.add(nfaulty_x2 >= 0)
s.add(nfaulty_y2 >= 0)






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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x2 - rule5_x2 - rule6_x2 + rule6_x2 ==  loc0_y2 - loc0_x2)
s.add(0 - rule1_x2 - rule2_x2 - rule4_x2 - rule7_x2 + rule7_x2 ==  loc1_y2 - loc1_x2)
s.add(0 + rule0_x2 + rule1_x2 + rule2_x2 + rule3_x2 ==  locCR_y2 - locCR_x2)
s.add(0 - rule3_x2 + rule4_x2 + rule5_x2 - rule8_x2 + rule8_x2 ==  locAC_y2 - locAC_x2)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule4_x2 + rule5_x2 == nsnt_y2 - nsnt_x2)
s.add(0 + rule2_x2 == nsntF_y2 - nsntF_x2)
s.add(0 + rule0_x2 + rule1_x2 + rule2_x2 + rule3_x2 == nfaulty_y2 - nfaulty_x2)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x2 > 0), And(nfaulty_x2<F, ) ))
s.add(Implies( (rule1_x2 > 0), And(nfaulty_x2<F, ) ))
s.add(Implies( (rule2_x2 > 0), And(nfaulty_x2<F, ) ))
s.add(Implies( (rule3_x2 > 0), And(nfaulty_x2<F, ) ))
s.add(Implies( (rule4_x2 > 0), And(nsnt_x2>=0, ) ))
s.add(Implies( (rule5_x2 > 0), And(nsnt_x2>=1, ) ))
s.add(Implies( (rule6_x2 > 0), And(nsnt_x2>=0, ) ))
s.add(Implies( (rule7_x2 > 0), And(nsnt_x2>=0, ) ))
s.add(Implies( (rule8_x2 > 0), And(nsnt_x2>=0, ) ))

##################Step 5#########################


#Ensuring that configurations x2 and y2 have the same context

s.add((nsnt_x2>=1) == (nsnt_y2>=1))
s.add((nsnt_x2>=0) == (nsnt_y2>=0))
s.add((nfaulty_x2<F) == (nfaulty_y2<F))

####################################################################################

#Creating constraints for a run between the x3th and y3th configurations

################Step 1#################


#Creating many copies of location variables

loc0_x3 = Real('loc0_x3')
loc0_y3 = Real('loc0_y3')
s.add(loc0_x3 >= 0)
s.add(loc0_y3 >= 0)
loc1_x3 = Real('loc1_x3')
loc1_y3 = Real('loc1_y3')
s.add(loc1_x3 >= 0)
s.add(loc1_y3 >= 0)
locCR_x3 = Real('locCR_x3')
locCR_y3 = Real('locCR_y3')
s.add(locCR_x3 >= 0)
s.add(locCR_y3 >= 0)
locAC_x3 = Real('locAC_x3')
locAC_y3 = Real('locAC_y3')
s.add(locAC_x3 >= 0)
s.add(locAC_y3 >= 0)






#Creating many copies of shared variables

nsnt_x3 = Real('nsnt_x3')
nsnt_y3 = Real('nsnt_y3')
s.add(nsnt_x3 >= 0)
s.add(nsnt_y3 >= 0)
nsntF_x3 = Real('nsntF_x3')
nsntF_y3 = Real('nsntF_y3')
s.add(nsntF_x3 >= 0)
s.add(nsntF_y3 >= 0)
nfaulty_x3 = Real('nfaulty_x3')
nfaulty_y3 = Real('nfaulty_y3')
s.add(nfaulty_x3 >= 0)
s.add(nfaulty_y3 >= 0)






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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x3 - rule5_x3 - rule6_x3 + rule6_x3 ==  loc0_y3 - loc0_x3)
s.add(0 - rule1_x3 - rule2_x3 - rule4_x3 - rule7_x3 + rule7_x3 ==  loc1_y3 - loc1_x3)
s.add(0 + rule0_x3 + rule1_x3 + rule2_x3 + rule3_x3 ==  locCR_y3 - locCR_x3)
s.add(0 - rule3_x3 + rule4_x3 + rule5_x3 - rule8_x3 + rule8_x3 ==  locAC_y3 - locAC_x3)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule4_x3 + rule5_x3 == nsnt_y3 - nsnt_x3)
s.add(0 + rule2_x3 == nsntF_y3 - nsntF_x3)
s.add(0 + rule0_x3 + rule1_x3 + rule2_x3 + rule3_x3 == nfaulty_y3 - nfaulty_x3)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x3 > 0), And(nfaulty_x3<F, ) ))
s.add(Implies( (rule1_x3 > 0), And(nfaulty_x3<F, ) ))
s.add(Implies( (rule2_x3 > 0), And(nfaulty_x3<F, ) ))
s.add(Implies( (rule3_x3 > 0), And(nfaulty_x3<F, ) ))
s.add(Implies( (rule4_x3 > 0), And(nsnt_x3>=0, ) ))
s.add(Implies( (rule5_x3 > 0), And(nsnt_x3>=1, ) ))
s.add(Implies( (rule6_x3 > 0), And(nsnt_x3>=0, ) ))
s.add(Implies( (rule7_x3 > 0), And(nsnt_x3>=0, ) ))
s.add(Implies( (rule8_x3 > 0), And(nsnt_x3>=0, ) ))

##################Step 5#########################


#Ensuring that configurations x3 and y3 have the same context

s.add((nsnt_x3>=1) == (nsnt_y3>=1))
s.add((nsnt_x3>=0) == (nsnt_y3>=0))
s.add((nfaulty_x3<F) == (nfaulty_y3<F))

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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y0 - rule5_y0 - rule6_y0 + rule6_y0 ==  loc0_x1 - loc0_y0)
s.add(0 - rule1_y0 - rule2_y0 - rule4_y0 - rule7_y0 + rule7_y0 ==  loc1_x1 - loc1_y0)
s.add(0 + rule0_y0 + rule1_y0 + rule2_y0 + rule3_y0 ==  locCR_x1 - locCR_y0)
s.add(0 - rule3_y0 + rule4_y0 + rule5_y0 - rule8_y0 + rule8_y0 ==  locAC_x1 - locAC_y0)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule4_y0 + rule5_y0 == nsnt_x1 - nsnt_y0)
s.add(0 + rule2_y0 == nsntF_x1 - nsntF_y0)
s.add(0 + rule0_y0 + rule1_y0 + rule2_y0 + rule3_y0 == nfaulty_x1 - nfaulty_y0)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y0 > 0), And(nfaulty_y0<F, ) ))
s.add(Implies( (rule1_y0 > 0), And(nfaulty_y0<F, ) ))
s.add(Implies( (rule2_y0 > 0), And(nfaulty_y0<F, ) ))
s.add(Implies( (rule3_y0 > 0), And(nfaulty_y0<F, ) ))
s.add(Implies( (rule4_y0 > 0), And(nsnt_y0>=0, ) ))
s.add(Implies( (rule5_y0 > 0), And(nsnt_y0>=1, ) ))
s.add(Implies( (rule6_y0 > 0), And(nsnt_y0>=0, ) ))
s.add(Implies( (rule7_y0 > 0), And(nsnt_y0>=0, ) ))
s.add(Implies( (rule8_y0 > 0), And(nsnt_y0>=0, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y0 and x0, if a fall condition is present

s.add((nfaulty_x1<F) == (nfaulty_y0<F))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule0_y0 == 0), (rule0_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule1_y0 == 0), (rule1_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule2_y0 == 0), (rule2_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule3_y0 == 0), (rule3_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule4_y0 == 0), (rule4_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule5_y0 == 0), (rule5_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule6_y0 == 0), (rule6_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule7_y0 == 0), (rule7_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule8_y0 == 0), (rule8_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), rule0_y0+rule1_y0+rule2_y0+rule3_y0+rule4_y0+rule5_y0+rule6_y0+rule7_y0+rule8_y0 <= 1))


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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y1 - rule5_y1 - rule6_y1 + rule6_y1 ==  loc0_x2 - loc0_y1)
s.add(0 - rule1_y1 - rule2_y1 - rule4_y1 - rule7_y1 + rule7_y1 ==  loc1_x2 - loc1_y1)
s.add(0 + rule0_y1 + rule1_y1 + rule2_y1 + rule3_y1 ==  locCR_x2 - locCR_y1)
s.add(0 - rule3_y1 + rule4_y1 + rule5_y1 - rule8_y1 + rule8_y1 ==  locAC_x2 - locAC_y1)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule4_y1 + rule5_y1 == nsnt_x2 - nsnt_y1)
s.add(0 + rule2_y1 == nsntF_x2 - nsntF_y1)
s.add(0 + rule0_y1 + rule1_y1 + rule2_y1 + rule3_y1 == nfaulty_x2 - nfaulty_y1)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y1 > 0), And(nfaulty_y1<F, ) ))
s.add(Implies( (rule1_y1 > 0), And(nfaulty_y1<F, ) ))
s.add(Implies( (rule2_y1 > 0), And(nfaulty_y1<F, ) ))
s.add(Implies( (rule3_y1 > 0), And(nfaulty_y1<F, ) ))
s.add(Implies( (rule4_y1 > 0), And(nsnt_y1>=0, ) ))
s.add(Implies( (rule5_y1 > 0), And(nsnt_y1>=1, ) ))
s.add(Implies( (rule6_y1 > 0), And(nsnt_y1>=0, ) ))
s.add(Implies( (rule7_y1 > 0), And(nsnt_y1>=0, ) ))
s.add(Implies( (rule8_y1 > 0), And(nsnt_y1>=0, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y1 and x1, if a fall condition is present

s.add((nfaulty_x2<F) == (nfaulty_y1<F))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule0_y1 == 0), (rule0_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule1_y1 == 0), (rule1_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule2_y1 == 0), (rule2_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule3_y1 == 0), (rule3_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule4_y1 == 0), (rule4_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule5_y1 == 0), (rule5_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule6_y1 == 0), (rule6_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule7_y1 == 0), (rule7_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule8_y1 == 0), (rule8_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), rule0_y1+rule1_y1+rule2_y1+rule3_y1+rule4_y1+rule5_y1+rule6_y1+rule7_y1+rule8_y1 <= 1))


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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y2 - rule5_y2 - rule6_y2 + rule6_y2 ==  loc0_x3 - loc0_y2)
s.add(0 - rule1_y2 - rule2_y2 - rule4_y2 - rule7_y2 + rule7_y2 ==  loc1_x3 - loc1_y2)
s.add(0 + rule0_y2 + rule1_y2 + rule2_y2 + rule3_y2 ==  locCR_x3 - locCR_y2)
s.add(0 - rule3_y2 + rule4_y2 + rule5_y2 - rule8_y2 + rule8_y2 ==  locAC_x3 - locAC_y2)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule4_y2 + rule5_y2 == nsnt_x3 - nsnt_y2)
s.add(0 + rule2_y2 == nsntF_x3 - nsntF_y2)
s.add(0 + rule0_y2 + rule1_y2 + rule2_y2 + rule3_y2 == nfaulty_x3 - nfaulty_y2)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y2 > 0), And(nfaulty_y2<F, ) ))
s.add(Implies( (rule1_y2 > 0), And(nfaulty_y2<F, ) ))
s.add(Implies( (rule2_y2 > 0), And(nfaulty_y2<F, ) ))
s.add(Implies( (rule3_y2 > 0), And(nfaulty_y2<F, ) ))
s.add(Implies( (rule4_y2 > 0), And(nsnt_y2>=0, ) ))
s.add(Implies( (rule5_y2 > 0), And(nsnt_y2>=1, ) ))
s.add(Implies( (rule6_y2 > 0), And(nsnt_y2>=0, ) ))
s.add(Implies( (rule7_y2 > 0), And(nsnt_y2>=0, ) ))
s.add(Implies( (rule8_y2 > 0), And(nsnt_y2>=0, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y2 and x2, if a fall condition is present

s.add((nfaulty_x3<F) == (nfaulty_y2<F))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule0_y2 == 0), (rule0_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule1_y2 == 0), (rule1_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule2_y2 == 0), (rule2_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule3_y2 == 0), (rule3_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule4_y2 == 0), (rule4_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule5_y2 == 0), (rule5_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule6_y2 == 0), (rule6_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule7_y2 == 0), (rule7_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule8_y2 == 0), (rule8_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), rule0_y2+rule1_y2+rule2_y2+rule3_y2+rule4_y2+rule5_y2+rule6_y2+rule7_y2+rule8_y2 <= 1))


#############Additional step for the final configuration#####################


###########Ensure that the last configuration satisfies the final condition#############

s.add(Or(locAC_y3 != 0, locAC_y3 != 0))






if s.check() == sat:

	print("Specification not satisfied")

else:

	print("Specification satisfied")
