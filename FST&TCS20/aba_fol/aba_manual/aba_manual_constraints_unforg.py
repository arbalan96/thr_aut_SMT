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

s.add(N > 3 * T)
s.add(T >= F)
s.add(T >= 1)

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
locEC_x0 = Real('locEC_x0')
locEC_y0 = Real('locEC_y0')
s.add(locEC_x0 >= 0)
s.add(locEC_y0 >= 0)
locRD_x0 = Real('locRD_x0')
locRD_y0 = Real('locRD_y0')
s.add(locRD_x0 >= 0)
s.add(locRD_y0 >= 0)
locAC_x0 = Real('locAC_x0')
locAC_y0 = Real('locAC_y0')
s.add(locAC_x0 >= 0)
s.add(locAC_y0 >= 0)






#Creating many copies of shared variables

nsntEC_x0 = Real('nsntEC_x0')
nsntEC_y0 = Real('nsntEC_y0')
s.add(nsntEC_x0 >= 0)
s.add(nsntEC_y0 >= 0)
nsntRD_x0 = Real('nsntRD_x0')
nsntRD_y0 = Real('nsntRD_y0')
s.add(nsntRD_x0 >= 0)
s.add(nsntRD_y0 >= 0)






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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule1_x0 - rule2_x0 - rule6_x0 + rule6_x0 ==  loc0_y0 - loc0_x0)
s.add(0 - rule0_x0 ==  loc1_y0 - loc1_x0)
s.add(0 + rule0_x0 + rule1_x0 + rule2_x0 - rule3_x0 - rule4_x0 - rule7_x0 + rule7_x0 ==  locEC_y0 - locEC_x0)
s.add(0 + rule3_x0 + rule4_x0 - rule5_x0 - rule8_x0 + rule8_x0 ==  locRD_y0 - locRD_x0)
s.add(0 + rule5_x0 - rule9_x0 + rule9_x0 ==  locAC_y0 - locAC_x0)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x0 + rule1_x0 + rule2_x0 == nsntEC_y0 - nsntEC_x0)
s.add(0 + rule3_x0 + rule4_x0 == nsntRD_y0 - nsntRD_x0)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x0 > 0), And(True, ) ))
s.add(Implies( (rule1_x0 > 0), And(2*nsntEC_x0>=N+T+1-2*F, ) ))
s.add(Implies( (rule2_x0 > 0), And(nsntRD_x0>=T+1-F, ) ))
s.add(Implies( (rule3_x0 > 0), And(2*nsntEC_x0>=N+T+1-2*F, ) ))
s.add(Implies( (rule4_x0 > 0), And(nsntRD_x0>=T+1-F, ) ))
s.add(Implies( (rule5_x0 > 0), And(2*nsntRD_x0>=2*T+1, ) ))
s.add(Implies( (rule6_x0 > 0), And(2*nsntEC_x0<=N+T, nsntRD_x0<=T, ) ))
s.add(Implies( (rule7_x0 > 0), And(2*nsntEC_x0<=N+T, nsntRD_x0<=T, ) ))
s.add(Implies( (rule8_x0 > 0), And(nsntRD_x0<=2*T, ) ))
s.add(Implies( (rule9_x0 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x0 and y0 have the same context

s.add((nsntRD_x0>=T+1-F) == (nsntRD_y0>=T+1-F))
s.add((2*nsntEC_x0<=N+T) == (2*nsntEC_y0<=N+T))
s.add((nsntRD_x0<=T) == (nsntRD_y0<=T))
s.add((nsntRD_x0<=2*T) == (nsntRD_y0<=2*T))
s.add((True) == (True))
s.add((2*nsntEC_x0>=N+T+1-2*F) == (2*nsntEC_y0>=N+T+1-2*F))
s.add((2*nsntRD_x0>=2*T+1) == (2*nsntRD_y0>=2*T+1))

#############Additional step for the initial configuration#####################


#############Ensure that the first configuration only contains initial locations###########

s.add((loc0_x0 + loc1_x0) == N - F)
s.add(locEC_x0 == 0)
s.add(locRD_x0 == 0)
s.add(locAC_x0 == 0)
s.add(nsntEC_x0 == 0)
s.add(nsntRD_x0 == 0)






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
locEC_x1 = Real('locEC_x1')
locEC_y1 = Real('locEC_y1')
s.add(locEC_x1 >= 0)
s.add(locEC_y1 >= 0)
locRD_x1 = Real('locRD_x1')
locRD_y1 = Real('locRD_y1')
s.add(locRD_x1 >= 0)
s.add(locRD_y1 >= 0)
locAC_x1 = Real('locAC_x1')
locAC_y1 = Real('locAC_y1')
s.add(locAC_x1 >= 0)
s.add(locAC_y1 >= 0)






#Creating many copies of shared variables

nsntEC_x1 = Real('nsntEC_x1')
nsntEC_y1 = Real('nsntEC_y1')
s.add(nsntEC_x1 >= 0)
s.add(nsntEC_y1 >= 0)
nsntRD_x1 = Real('nsntRD_x1')
nsntRD_y1 = Real('nsntRD_y1')
s.add(nsntRD_x1 >= 0)
s.add(nsntRD_y1 >= 0)






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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule1_x1 - rule2_x1 - rule6_x1 + rule6_x1 ==  loc0_y1 - loc0_x1)
s.add(0 - rule0_x1 ==  loc1_y1 - loc1_x1)
s.add(0 + rule0_x1 + rule1_x1 + rule2_x1 - rule3_x1 - rule4_x1 - rule7_x1 + rule7_x1 ==  locEC_y1 - locEC_x1)
s.add(0 + rule3_x1 + rule4_x1 - rule5_x1 - rule8_x1 + rule8_x1 ==  locRD_y1 - locRD_x1)
s.add(0 + rule5_x1 - rule9_x1 + rule9_x1 ==  locAC_y1 - locAC_x1)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x1 + rule1_x1 + rule2_x1 == nsntEC_y1 - nsntEC_x1)
s.add(0 + rule3_x1 + rule4_x1 == nsntRD_y1 - nsntRD_x1)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x1 > 0), And(True, ) ))
s.add(Implies( (rule1_x1 > 0), And(2*nsntEC_x1>=N+T+1-2*F, ) ))
s.add(Implies( (rule2_x1 > 0), And(nsntRD_x1>=T+1-F, ) ))
s.add(Implies( (rule3_x1 > 0), And(2*nsntEC_x1>=N+T+1-2*F, ) ))
s.add(Implies( (rule4_x1 > 0), And(nsntRD_x1>=T+1-F, ) ))
s.add(Implies( (rule5_x1 > 0), And(2*nsntRD_x1>=2*T+1, ) ))
s.add(Implies( (rule6_x1 > 0), And(2*nsntEC_x1<=N+T, nsntRD_x1<=T, ) ))
s.add(Implies( (rule7_x1 > 0), And(2*nsntEC_x1<=N+T, nsntRD_x1<=T, ) ))
s.add(Implies( (rule8_x1 > 0), And(nsntRD_x1<=2*T, ) ))
s.add(Implies( (rule9_x1 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x1 and y1 have the same context

s.add((nsntRD_x1>=T+1-F) == (nsntRD_y1>=T+1-F))
s.add((2*nsntEC_x1<=N+T) == (2*nsntEC_y1<=N+T))
s.add((nsntRD_x1<=T) == (nsntRD_y1<=T))
s.add((nsntRD_x1<=2*T) == (nsntRD_y1<=2*T))
s.add((True) == (True))
s.add((2*nsntEC_x1>=N+T+1-2*F) == (2*nsntEC_y1>=N+T+1-2*F))
s.add((2*nsntRD_x1>=2*T+1) == (2*nsntRD_y1>=2*T+1))

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
locEC_x2 = Real('locEC_x2')
locEC_y2 = Real('locEC_y2')
s.add(locEC_x2 >= 0)
s.add(locEC_y2 >= 0)
locRD_x2 = Real('locRD_x2')
locRD_y2 = Real('locRD_y2')
s.add(locRD_x2 >= 0)
s.add(locRD_y2 >= 0)
locAC_x2 = Real('locAC_x2')
locAC_y2 = Real('locAC_y2')
s.add(locAC_x2 >= 0)
s.add(locAC_y2 >= 0)






#Creating many copies of shared variables

nsntEC_x2 = Real('nsntEC_x2')
nsntEC_y2 = Real('nsntEC_y2')
s.add(nsntEC_x2 >= 0)
s.add(nsntEC_y2 >= 0)
nsntRD_x2 = Real('nsntRD_x2')
nsntRD_y2 = Real('nsntRD_y2')
s.add(nsntRD_x2 >= 0)
s.add(nsntRD_y2 >= 0)






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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule1_x2 - rule2_x2 - rule6_x2 + rule6_x2 ==  loc0_y2 - loc0_x2)
s.add(0 - rule0_x2 ==  loc1_y2 - loc1_x2)
s.add(0 + rule0_x2 + rule1_x2 + rule2_x2 - rule3_x2 - rule4_x2 - rule7_x2 + rule7_x2 ==  locEC_y2 - locEC_x2)
s.add(0 + rule3_x2 + rule4_x2 - rule5_x2 - rule8_x2 + rule8_x2 ==  locRD_y2 - locRD_x2)
s.add(0 + rule5_x2 - rule9_x2 + rule9_x2 ==  locAC_y2 - locAC_x2)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x2 + rule1_x2 + rule2_x2 == nsntEC_y2 - nsntEC_x2)
s.add(0 + rule3_x2 + rule4_x2 == nsntRD_y2 - nsntRD_x2)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x2 > 0), And(True, ) ))
s.add(Implies( (rule1_x2 > 0), And(2*nsntEC_x2>=N+T+1-2*F, ) ))
s.add(Implies( (rule2_x2 > 0), And(nsntRD_x2>=T+1-F, ) ))
s.add(Implies( (rule3_x2 > 0), And(2*nsntEC_x2>=N+T+1-2*F, ) ))
s.add(Implies( (rule4_x2 > 0), And(nsntRD_x2>=T+1-F, ) ))
s.add(Implies( (rule5_x2 > 0), And(2*nsntRD_x2>=2*T+1, ) ))
s.add(Implies( (rule6_x2 > 0), And(2*nsntEC_x2<=N+T, nsntRD_x2<=T, ) ))
s.add(Implies( (rule7_x2 > 0), And(2*nsntEC_x2<=N+T, nsntRD_x2<=T, ) ))
s.add(Implies( (rule8_x2 > 0), And(nsntRD_x2<=2*T, ) ))
s.add(Implies( (rule9_x2 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x2 and y2 have the same context

s.add((nsntRD_x2>=T+1-F) == (nsntRD_y2>=T+1-F))
s.add((2*nsntEC_x2<=N+T) == (2*nsntEC_y2<=N+T))
s.add((nsntRD_x2<=T) == (nsntRD_y2<=T))
s.add((nsntRD_x2<=2*T) == (nsntRD_y2<=2*T))
s.add((True) == (True))
s.add((2*nsntEC_x2>=N+T+1-2*F) == (2*nsntEC_y2>=N+T+1-2*F))
s.add((2*nsntRD_x2>=2*T+1) == (2*nsntRD_y2>=2*T+1))

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
locEC_x3 = Real('locEC_x3')
locEC_y3 = Real('locEC_y3')
s.add(locEC_x3 >= 0)
s.add(locEC_y3 >= 0)
locRD_x3 = Real('locRD_x3')
locRD_y3 = Real('locRD_y3')
s.add(locRD_x3 >= 0)
s.add(locRD_y3 >= 0)
locAC_x3 = Real('locAC_x3')
locAC_y3 = Real('locAC_y3')
s.add(locAC_x3 >= 0)
s.add(locAC_y3 >= 0)






#Creating many copies of shared variables

nsntEC_x3 = Real('nsntEC_x3')
nsntEC_y3 = Real('nsntEC_y3')
s.add(nsntEC_x3 >= 0)
s.add(nsntEC_y3 >= 0)
nsntRD_x3 = Real('nsntRD_x3')
nsntRD_y3 = Real('nsntRD_y3')
s.add(nsntRD_x3 >= 0)
s.add(nsntRD_y3 >= 0)






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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule1_x3 - rule2_x3 - rule6_x3 + rule6_x3 ==  loc0_y3 - loc0_x3)
s.add(0 - rule0_x3 ==  loc1_y3 - loc1_x3)
s.add(0 + rule0_x3 + rule1_x3 + rule2_x3 - rule3_x3 - rule4_x3 - rule7_x3 + rule7_x3 ==  locEC_y3 - locEC_x3)
s.add(0 + rule3_x3 + rule4_x3 - rule5_x3 - rule8_x3 + rule8_x3 ==  locRD_y3 - locRD_x3)
s.add(0 + rule5_x3 - rule9_x3 + rule9_x3 ==  locAC_y3 - locAC_x3)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x3 + rule1_x3 + rule2_x3 == nsntEC_y3 - nsntEC_x3)
s.add(0 + rule3_x3 + rule4_x3 == nsntRD_y3 - nsntRD_x3)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x3 > 0), And(True, ) ))
s.add(Implies( (rule1_x3 > 0), And(2*nsntEC_x3>=N+T+1-2*F, ) ))
s.add(Implies( (rule2_x3 > 0), And(nsntRD_x3>=T+1-F, ) ))
s.add(Implies( (rule3_x3 > 0), And(2*nsntEC_x3>=N+T+1-2*F, ) ))
s.add(Implies( (rule4_x3 > 0), And(nsntRD_x3>=T+1-F, ) ))
s.add(Implies( (rule5_x3 > 0), And(2*nsntRD_x3>=2*T+1, ) ))
s.add(Implies( (rule6_x3 > 0), And(2*nsntEC_x3<=N+T, nsntRD_x3<=T, ) ))
s.add(Implies( (rule7_x3 > 0), And(2*nsntEC_x3<=N+T, nsntRD_x3<=T, ) ))
s.add(Implies( (rule8_x3 > 0), And(nsntRD_x3<=2*T, ) ))
s.add(Implies( (rule9_x3 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x3 and y3 have the same context

s.add((nsntRD_x3>=T+1-F) == (nsntRD_y3>=T+1-F))
s.add((2*nsntEC_x3<=N+T) == (2*nsntEC_y3<=N+T))
s.add((nsntRD_x3<=T) == (nsntRD_y3<=T))
s.add((nsntRD_x3<=2*T) == (nsntRD_y3<=2*T))
s.add((True) == (True))
s.add((2*nsntEC_x3>=N+T+1-2*F) == (2*nsntEC_y3>=N+T+1-2*F))
s.add((2*nsntRD_x3>=2*T+1) == (2*nsntRD_y3>=2*T+1))

####################################################################################

#Creating constraints for a run between the x4th and y4th configurations

################Step 1#################


#Creating many copies of location variables

loc0_x4 = Real('loc0_x4')
loc0_y4 = Real('loc0_y4')
s.add(loc0_x4 >= 0)
s.add(loc0_y4 >= 0)
loc1_x4 = Real('loc1_x4')
loc1_y4 = Real('loc1_y4')
s.add(loc1_x4 >= 0)
s.add(loc1_y4 >= 0)
locEC_x4 = Real('locEC_x4')
locEC_y4 = Real('locEC_y4')
s.add(locEC_x4 >= 0)
s.add(locEC_y4 >= 0)
locRD_x4 = Real('locRD_x4')
locRD_y4 = Real('locRD_y4')
s.add(locRD_x4 >= 0)
s.add(locRD_y4 >= 0)
locAC_x4 = Real('locAC_x4')
locAC_y4 = Real('locAC_y4')
s.add(locAC_x4 >= 0)
s.add(locAC_y4 >= 0)






#Creating many copies of shared variables

nsntEC_x4 = Real('nsntEC_x4')
nsntEC_y4 = Real('nsntEC_y4')
s.add(nsntEC_x4 >= 0)
s.add(nsntEC_y4 >= 0)
nsntRD_x4 = Real('nsntRD_x4')
nsntRD_y4 = Real('nsntRD_y4')
s.add(nsntRD_x4 >= 0)
s.add(nsntRD_y4 >= 0)






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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule1_x4 - rule2_x4 - rule6_x4 + rule6_x4 ==  loc0_y4 - loc0_x4)
s.add(0 - rule0_x4 ==  loc1_y4 - loc1_x4)
s.add(0 + rule0_x4 + rule1_x4 + rule2_x4 - rule3_x4 - rule4_x4 - rule7_x4 + rule7_x4 ==  locEC_y4 - locEC_x4)
s.add(0 + rule3_x4 + rule4_x4 - rule5_x4 - rule8_x4 + rule8_x4 ==  locRD_y4 - locRD_x4)
s.add(0 + rule5_x4 - rule9_x4 + rule9_x4 ==  locAC_y4 - locAC_x4)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x4 + rule1_x4 + rule2_x4 == nsntEC_y4 - nsntEC_x4)
s.add(0 + rule3_x4 + rule4_x4 == nsntRD_y4 - nsntRD_x4)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x4 > 0), And(True, ) ))
s.add(Implies( (rule1_x4 > 0), And(2*nsntEC_x4>=N+T+1-2*F, ) ))
s.add(Implies( (rule2_x4 > 0), And(nsntRD_x4>=T+1-F, ) ))
s.add(Implies( (rule3_x4 > 0), And(2*nsntEC_x4>=N+T+1-2*F, ) ))
s.add(Implies( (rule4_x4 > 0), And(nsntRD_x4>=T+1-F, ) ))
s.add(Implies( (rule5_x4 > 0), And(2*nsntRD_x4>=2*T+1, ) ))
s.add(Implies( (rule6_x4 > 0), And(2*nsntEC_x4<=N+T, nsntRD_x4<=T, ) ))
s.add(Implies( (rule7_x4 > 0), And(2*nsntEC_x4<=N+T, nsntRD_x4<=T, ) ))
s.add(Implies( (rule8_x4 > 0), And(nsntRD_x4<=2*T, ) ))
s.add(Implies( (rule9_x4 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x4 and y4 have the same context

s.add((nsntRD_x4>=T+1-F) == (nsntRD_y4>=T+1-F))
s.add((2*nsntEC_x4<=N+T) == (2*nsntEC_y4<=N+T))
s.add((nsntRD_x4<=T) == (nsntRD_y4<=T))
s.add((nsntRD_x4<=2*T) == (nsntRD_y4<=2*T))
s.add((True) == (True))
s.add((2*nsntEC_x4>=N+T+1-2*F) == (2*nsntEC_y4>=N+T+1-2*F))
s.add((2*nsntRD_x4>=2*T+1) == (2*nsntRD_y4>=2*T+1))

####################################################################################

#Creating constraints for a run between the x5th and y5th configurations

################Step 1#################


#Creating many copies of location variables

loc0_x5 = Real('loc0_x5')
loc0_y5 = Real('loc0_y5')
s.add(loc0_x5 >= 0)
s.add(loc0_y5 >= 0)
loc1_x5 = Real('loc1_x5')
loc1_y5 = Real('loc1_y5')
s.add(loc1_x5 >= 0)
s.add(loc1_y5 >= 0)
locEC_x5 = Real('locEC_x5')
locEC_y5 = Real('locEC_y5')
s.add(locEC_x5 >= 0)
s.add(locEC_y5 >= 0)
locRD_x5 = Real('locRD_x5')
locRD_y5 = Real('locRD_y5')
s.add(locRD_x5 >= 0)
s.add(locRD_y5 >= 0)
locAC_x5 = Real('locAC_x5')
locAC_y5 = Real('locAC_y5')
s.add(locAC_x5 >= 0)
s.add(locAC_y5 >= 0)






#Creating many copies of shared variables

nsntEC_x5 = Real('nsntEC_x5')
nsntEC_y5 = Real('nsntEC_y5')
s.add(nsntEC_x5 >= 0)
s.add(nsntEC_y5 >= 0)
nsntRD_x5 = Real('nsntRD_x5')
nsntRD_y5 = Real('nsntRD_y5')
s.add(nsntRD_x5 >= 0)
s.add(nsntRD_y5 >= 0)






#Creating many copies of variables for rules

rule0_x5 = Real('rule0_x5')
s.add(rule0_x5 >= 0)
rule1_x5 = Real('rule1_x5')
s.add(rule1_x5 >= 0)
rule2_x5 = Real('rule2_x5')
s.add(rule2_x5 >= 0)
rule3_x5 = Real('rule3_x5')
s.add(rule3_x5 >= 0)
rule4_x5 = Real('rule4_x5')
s.add(rule4_x5 >= 0)
rule5_x5 = Real('rule5_x5')
s.add(rule5_x5 >= 0)
rule6_x5 = Real('rule6_x5')
s.add(rule6_x5 >= 0)
rule7_x5 = Real('rule7_x5')
s.add(rule7_x5 >= 0)
rule8_x5 = Real('rule8_x5')
s.add(rule8_x5 >= 0)
rule9_x5 = Real('rule9_x5')
s.add(rule9_x5 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule1_x5 - rule2_x5 - rule6_x5 + rule6_x5 ==  loc0_y5 - loc0_x5)
s.add(0 - rule0_x5 ==  loc1_y5 - loc1_x5)
s.add(0 + rule0_x5 + rule1_x5 + rule2_x5 - rule3_x5 - rule4_x5 - rule7_x5 + rule7_x5 ==  locEC_y5 - locEC_x5)
s.add(0 + rule3_x5 + rule4_x5 - rule5_x5 - rule8_x5 + rule8_x5 ==  locRD_y5 - locRD_x5)
s.add(0 + rule5_x5 - rule9_x5 + rule9_x5 ==  locAC_y5 - locAC_x5)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x5 + rule1_x5 + rule2_x5 == nsntEC_y5 - nsntEC_x5)
s.add(0 + rule3_x5 + rule4_x5 == nsntRD_y5 - nsntRD_x5)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x5 > 0), And(True, ) ))
s.add(Implies( (rule1_x5 > 0), And(2*nsntEC_x5>=N+T+1-2*F, ) ))
s.add(Implies( (rule2_x5 > 0), And(nsntRD_x5>=T+1-F, ) ))
s.add(Implies( (rule3_x5 > 0), And(2*nsntEC_x5>=N+T+1-2*F, ) ))
s.add(Implies( (rule4_x5 > 0), And(nsntRD_x5>=T+1-F, ) ))
s.add(Implies( (rule5_x5 > 0), And(2*nsntRD_x5>=2*T+1, ) ))
s.add(Implies( (rule6_x5 > 0), And(2*nsntEC_x5<=N+T, nsntRD_x5<=T, ) ))
s.add(Implies( (rule7_x5 > 0), And(2*nsntEC_x5<=N+T, nsntRD_x5<=T, ) ))
s.add(Implies( (rule8_x5 > 0), And(nsntRD_x5<=2*T, ) ))
s.add(Implies( (rule9_x5 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x5 and y5 have the same context

s.add((nsntRD_x5>=T+1-F) == (nsntRD_y5>=T+1-F))
s.add((2*nsntEC_x5<=N+T) == (2*nsntEC_y5<=N+T))
s.add((nsntRD_x5<=T) == (nsntRD_y5<=T))
s.add((nsntRD_x5<=2*T) == (nsntRD_y5<=2*T))
s.add((True) == (True))
s.add((2*nsntEC_x5>=N+T+1-2*F) == (2*nsntEC_y5>=N+T+1-2*F))
s.add((2*nsntRD_x5>=2*T+1) == (2*nsntRD_y5>=2*T+1))

####################################################################################

#Creating constraints for a run between the x6th and y6th configurations

################Step 1#################


#Creating many copies of location variables

loc0_x6 = Real('loc0_x6')
loc0_y6 = Real('loc0_y6')
s.add(loc0_x6 >= 0)
s.add(loc0_y6 >= 0)
loc1_x6 = Real('loc1_x6')
loc1_y6 = Real('loc1_y6')
s.add(loc1_x6 >= 0)
s.add(loc1_y6 >= 0)
locEC_x6 = Real('locEC_x6')
locEC_y6 = Real('locEC_y6')
s.add(locEC_x6 >= 0)
s.add(locEC_y6 >= 0)
locRD_x6 = Real('locRD_x6')
locRD_y6 = Real('locRD_y6')
s.add(locRD_x6 >= 0)
s.add(locRD_y6 >= 0)
locAC_x6 = Real('locAC_x6')
locAC_y6 = Real('locAC_y6')
s.add(locAC_x6 >= 0)
s.add(locAC_y6 >= 0)






#Creating many copies of shared variables

nsntEC_x6 = Real('nsntEC_x6')
nsntEC_y6 = Real('nsntEC_y6')
s.add(nsntEC_x6 >= 0)
s.add(nsntEC_y6 >= 0)
nsntRD_x6 = Real('nsntRD_x6')
nsntRD_y6 = Real('nsntRD_y6')
s.add(nsntRD_x6 >= 0)
s.add(nsntRD_y6 >= 0)






#Creating many copies of variables for rules

rule0_x6 = Real('rule0_x6')
s.add(rule0_x6 >= 0)
rule1_x6 = Real('rule1_x6')
s.add(rule1_x6 >= 0)
rule2_x6 = Real('rule2_x6')
s.add(rule2_x6 >= 0)
rule3_x6 = Real('rule3_x6')
s.add(rule3_x6 >= 0)
rule4_x6 = Real('rule4_x6')
s.add(rule4_x6 >= 0)
rule5_x6 = Real('rule5_x6')
s.add(rule5_x6 >= 0)
rule6_x6 = Real('rule6_x6')
s.add(rule6_x6 >= 0)
rule7_x6 = Real('rule7_x6')
s.add(rule7_x6 >= 0)
rule8_x6 = Real('rule8_x6')
s.add(rule8_x6 >= 0)
rule9_x6 = Real('rule9_x6')
s.add(rule9_x6 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule1_x6 - rule2_x6 - rule6_x6 + rule6_x6 ==  loc0_y6 - loc0_x6)
s.add(0 - rule0_x6 ==  loc1_y6 - loc1_x6)
s.add(0 + rule0_x6 + rule1_x6 + rule2_x6 - rule3_x6 - rule4_x6 - rule7_x6 + rule7_x6 ==  locEC_y6 - locEC_x6)
s.add(0 + rule3_x6 + rule4_x6 - rule5_x6 - rule8_x6 + rule8_x6 ==  locRD_y6 - locRD_x6)
s.add(0 + rule5_x6 - rule9_x6 + rule9_x6 ==  locAC_y6 - locAC_x6)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x6 + rule1_x6 + rule2_x6 == nsntEC_y6 - nsntEC_x6)
s.add(0 + rule3_x6 + rule4_x6 == nsntRD_y6 - nsntRD_x6)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x6 > 0), And(True, ) ))
s.add(Implies( (rule1_x6 > 0), And(2*nsntEC_x6>=N+T+1-2*F, ) ))
s.add(Implies( (rule2_x6 > 0), And(nsntRD_x6>=T+1-F, ) ))
s.add(Implies( (rule3_x6 > 0), And(2*nsntEC_x6>=N+T+1-2*F, ) ))
s.add(Implies( (rule4_x6 > 0), And(nsntRD_x6>=T+1-F, ) ))
s.add(Implies( (rule5_x6 > 0), And(2*nsntRD_x6>=2*T+1, ) ))
s.add(Implies( (rule6_x6 > 0), And(2*nsntEC_x6<=N+T, nsntRD_x6<=T, ) ))
s.add(Implies( (rule7_x6 > 0), And(2*nsntEC_x6<=N+T, nsntRD_x6<=T, ) ))
s.add(Implies( (rule8_x6 > 0), And(nsntRD_x6<=2*T, ) ))
s.add(Implies( (rule9_x6 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x6 and y6 have the same context

s.add((nsntRD_x6>=T+1-F) == (nsntRD_y6>=T+1-F))
s.add((2*nsntEC_x6<=N+T) == (2*nsntEC_y6<=N+T))
s.add((nsntRD_x6<=T) == (nsntRD_y6<=T))
s.add((nsntRD_x6<=2*T) == (nsntRD_y6<=2*T))
s.add((True) == (True))
s.add((2*nsntEC_x6>=N+T+1-2*F) == (2*nsntEC_y6>=N+T+1-2*F))
s.add((2*nsntRD_x6>=2*T+1) == (2*nsntRD_y6>=2*T+1))

####################################################################################

#Creating constraints for a run between the x7th and y7th configurations

################Step 1#################


#Creating many copies of location variables

loc0_x7 = Real('loc0_x7')
loc0_y7 = Real('loc0_y7')
s.add(loc0_x7 >= 0)
s.add(loc0_y7 >= 0)
loc1_x7 = Real('loc1_x7')
loc1_y7 = Real('loc1_y7')
s.add(loc1_x7 >= 0)
s.add(loc1_y7 >= 0)
locEC_x7 = Real('locEC_x7')
locEC_y7 = Real('locEC_y7')
s.add(locEC_x7 >= 0)
s.add(locEC_y7 >= 0)
locRD_x7 = Real('locRD_x7')
locRD_y7 = Real('locRD_y7')
s.add(locRD_x7 >= 0)
s.add(locRD_y7 >= 0)
locAC_x7 = Real('locAC_x7')
locAC_y7 = Real('locAC_y7')
s.add(locAC_x7 >= 0)
s.add(locAC_y7 >= 0)






#Creating many copies of shared variables

nsntEC_x7 = Real('nsntEC_x7')
nsntEC_y7 = Real('nsntEC_y7')
s.add(nsntEC_x7 >= 0)
s.add(nsntEC_y7 >= 0)
nsntRD_x7 = Real('nsntRD_x7')
nsntRD_y7 = Real('nsntRD_y7')
s.add(nsntRD_x7 >= 0)
s.add(nsntRD_y7 >= 0)






#Creating many copies of variables for rules

rule0_x7 = Real('rule0_x7')
s.add(rule0_x7 >= 0)
rule1_x7 = Real('rule1_x7')
s.add(rule1_x7 >= 0)
rule2_x7 = Real('rule2_x7')
s.add(rule2_x7 >= 0)
rule3_x7 = Real('rule3_x7')
s.add(rule3_x7 >= 0)
rule4_x7 = Real('rule4_x7')
s.add(rule4_x7 >= 0)
rule5_x7 = Real('rule5_x7')
s.add(rule5_x7 >= 0)
rule6_x7 = Real('rule6_x7')
s.add(rule6_x7 >= 0)
rule7_x7 = Real('rule7_x7')
s.add(rule7_x7 >= 0)
rule8_x7 = Real('rule8_x7')
s.add(rule8_x7 >= 0)
rule9_x7 = Real('rule9_x7')
s.add(rule9_x7 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule1_x7 - rule2_x7 - rule6_x7 + rule6_x7 ==  loc0_y7 - loc0_x7)
s.add(0 - rule0_x7 ==  loc1_y7 - loc1_x7)
s.add(0 + rule0_x7 + rule1_x7 + rule2_x7 - rule3_x7 - rule4_x7 - rule7_x7 + rule7_x7 ==  locEC_y7 - locEC_x7)
s.add(0 + rule3_x7 + rule4_x7 - rule5_x7 - rule8_x7 + rule8_x7 ==  locRD_y7 - locRD_x7)
s.add(0 + rule5_x7 - rule9_x7 + rule9_x7 ==  locAC_y7 - locAC_x7)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x7 + rule1_x7 + rule2_x7 == nsntEC_y7 - nsntEC_x7)
s.add(0 + rule3_x7 + rule4_x7 == nsntRD_y7 - nsntRD_x7)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x7 > 0), And(True, ) ))
s.add(Implies( (rule1_x7 > 0), And(2*nsntEC_x7>=N+T+1-2*F, ) ))
s.add(Implies( (rule2_x7 > 0), And(nsntRD_x7>=T+1-F, ) ))
s.add(Implies( (rule3_x7 > 0), And(2*nsntEC_x7>=N+T+1-2*F, ) ))
s.add(Implies( (rule4_x7 > 0), And(nsntRD_x7>=T+1-F, ) ))
s.add(Implies( (rule5_x7 > 0), And(2*nsntRD_x7>=2*T+1, ) ))
s.add(Implies( (rule6_x7 > 0), And(2*nsntEC_x7<=N+T, nsntRD_x7<=T, ) ))
s.add(Implies( (rule7_x7 > 0), And(2*nsntEC_x7<=N+T, nsntRD_x7<=T, ) ))
s.add(Implies( (rule8_x7 > 0), And(nsntRD_x7<=2*T, ) ))
s.add(Implies( (rule9_x7 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x7 and y7 have the same context

s.add((nsntRD_x7>=T+1-F) == (nsntRD_y7>=T+1-F))
s.add((2*nsntEC_x7<=N+T) == (2*nsntEC_y7<=N+T))
s.add((nsntRD_x7<=T) == (nsntRD_y7<=T))
s.add((nsntRD_x7<=2*T) == (nsntRD_y7<=2*T))
s.add((True) == (True))
s.add((2*nsntEC_x7>=N+T+1-2*F) == (2*nsntEC_y7>=N+T+1-2*F))
s.add((2*nsntRD_x7>=2*T+1) == (2*nsntRD_y7>=2*T+1))

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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule1_y0 - rule2_y0 - rule6_y0 + rule6_y0 ==  loc0_x1 - loc0_y0)
s.add(0 - rule0_y0 ==  loc1_x1 - loc1_y0)
s.add(0 + rule0_y0 + rule1_y0 + rule2_y0 - rule3_y0 - rule4_y0 - rule7_y0 + rule7_y0 ==  locEC_x1 - locEC_y0)
s.add(0 + rule3_y0 + rule4_y0 - rule5_y0 - rule8_y0 + rule8_y0 ==  locRD_x1 - locRD_y0)
s.add(0 + rule5_y0 - rule9_y0 + rule9_y0 ==  locAC_x1 - locAC_y0)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y0 + rule1_y0 + rule2_y0 == nsntEC_x1 - nsntEC_y0)
s.add(0 + rule3_y0 + rule4_y0 == nsntRD_x1 - nsntRD_y0)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y0 > 0), And(True, ) ))
s.add(Implies( (rule1_y0 > 0), And(2*nsntEC_y0>=N+T+1-2*F, ) ))
s.add(Implies( (rule2_y0 > 0), And(nsntRD_y0>=T+1-F, ) ))
s.add(Implies( (rule3_y0 > 0), And(2*nsntEC_y0>=N+T+1-2*F, ) ))
s.add(Implies( (rule4_y0 > 0), And(nsntRD_y0>=T+1-F, ) ))
s.add(Implies( (rule5_y0 > 0), And(2*nsntRD_y0>=2*T+1, ) ))
s.add(Implies( (rule6_y0 > 0), And(2*nsntEC_y0<=N+T, nsntRD_y0<=T, ) ))
s.add(Implies( (rule7_y0 > 0), And(2*nsntEC_y0<=N+T, nsntRD_y0<=T, ) ))
s.add(Implies( (rule8_y0 > 0), And(nsntRD_y0<=2*T, ) ))
s.add(Implies( (rule9_y0 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y0 and x0, if a fall condition is present

s.add((nsntRD_x1<=T) == (nsntRD_y0<=T))
s.add(Implies(And((nsntRD_x1<=T), Not(nsntRD_y0<=T)), Or((rule0_y0 == 0), (rule0_y0 == 1))))
s.add(Implies(And((nsntRD_x1<=T), Not(nsntRD_y0<=T)), Or((rule1_y0 == 0), (rule1_y0 == 1))))
s.add(Implies(And((nsntRD_x1<=T), Not(nsntRD_y0<=T)), Or((rule2_y0 == 0), (rule2_y0 == 1))))
s.add(Implies(And((nsntRD_x1<=T), Not(nsntRD_y0<=T)), Or((rule3_y0 == 0), (rule3_y0 == 1))))
s.add(Implies(And((nsntRD_x1<=T), Not(nsntRD_y0<=T)), Or((rule4_y0 == 0), (rule4_y0 == 1))))
s.add(Implies(And((nsntRD_x1<=T), Not(nsntRD_y0<=T)), Or((rule5_y0 == 0), (rule5_y0 == 1))))
s.add(Implies(And((nsntRD_x1<=T), Not(nsntRD_y0<=T)), Or((rule6_y0 == 0), (rule6_y0 == 1))))
s.add(Implies(And((nsntRD_x1<=T), Not(nsntRD_y0<=T)), Or((rule7_y0 == 0), (rule7_y0 == 1))))
s.add(Implies(And((nsntRD_x1<=T), Not(nsntRD_y0<=T)), Or((rule8_y0 == 0), (rule8_y0 == 1))))
s.add(Implies(And((nsntRD_x1<=T), Not(nsntRD_y0<=T)), Or((rule9_y0 == 0), (rule9_y0 == 1))))
s.add(Implies(And((nsntRD_x1<=T), Not(nsntRD_y0<=T)), rule0_y0+rule1_y0+rule2_y0+rule3_y0+rule4_y0+rule5_y0+rule6_y0+rule7_y0+rule8_y0+rule9_y0 <= 1))

s.add((2*nsntEC_x1<=N+T) == (2*nsntEC_y0<=N+T))
s.add(Implies(And((2*nsntEC_x1<=N+T), Not(2*nsntEC_y0<=N+T)), Or((rule0_y0 == 0), (rule0_y0 == 1))))
s.add(Implies(And((2*nsntEC_x1<=N+T), Not(2*nsntEC_y0<=N+T)), Or((rule1_y0 == 0), (rule1_y0 == 1))))
s.add(Implies(And((2*nsntEC_x1<=N+T), Not(2*nsntEC_y0<=N+T)), Or((rule2_y0 == 0), (rule2_y0 == 1))))
s.add(Implies(And((2*nsntEC_x1<=N+T), Not(2*nsntEC_y0<=N+T)), Or((rule3_y0 == 0), (rule3_y0 == 1))))
s.add(Implies(And((2*nsntEC_x1<=N+T), Not(2*nsntEC_y0<=N+T)), Or((rule4_y0 == 0), (rule4_y0 == 1))))
s.add(Implies(And((2*nsntEC_x1<=N+T), Not(2*nsntEC_y0<=N+T)), Or((rule5_y0 == 0), (rule5_y0 == 1))))
s.add(Implies(And((2*nsntEC_x1<=N+T), Not(2*nsntEC_y0<=N+T)), Or((rule6_y0 == 0), (rule6_y0 == 1))))
s.add(Implies(And((2*nsntEC_x1<=N+T), Not(2*nsntEC_y0<=N+T)), Or((rule7_y0 == 0), (rule7_y0 == 1))))
s.add(Implies(And((2*nsntEC_x1<=N+T), Not(2*nsntEC_y0<=N+T)), Or((rule8_y0 == 0), (rule8_y0 == 1))))
s.add(Implies(And((2*nsntEC_x1<=N+T), Not(2*nsntEC_y0<=N+T)), Or((rule9_y0 == 0), (rule9_y0 == 1))))
s.add(Implies(And((2*nsntEC_x1<=N+T), Not(2*nsntEC_y0<=N+T)), rule0_y0+rule1_y0+rule2_y0+rule3_y0+rule4_y0+rule5_y0+rule6_y0+rule7_y0+rule8_y0+rule9_y0 <= 1))

s.add((nsntRD_x1<=2*T) == (nsntRD_y0<=2*T))
s.add(Implies(And((nsntRD_x1<=2*T), Not(nsntRD_y0<=2*T)), Or((rule0_y0 == 0), (rule0_y0 == 1))))
s.add(Implies(And((nsntRD_x1<=2*T), Not(nsntRD_y0<=2*T)), Or((rule1_y0 == 0), (rule1_y0 == 1))))
s.add(Implies(And((nsntRD_x1<=2*T), Not(nsntRD_y0<=2*T)), Or((rule2_y0 == 0), (rule2_y0 == 1))))
s.add(Implies(And((nsntRD_x1<=2*T), Not(nsntRD_y0<=2*T)), Or((rule3_y0 == 0), (rule3_y0 == 1))))
s.add(Implies(And((nsntRD_x1<=2*T), Not(nsntRD_y0<=2*T)), Or((rule4_y0 == 0), (rule4_y0 == 1))))
s.add(Implies(And((nsntRD_x1<=2*T), Not(nsntRD_y0<=2*T)), Or((rule5_y0 == 0), (rule5_y0 == 1))))
s.add(Implies(And((nsntRD_x1<=2*T), Not(nsntRD_y0<=2*T)), Or((rule6_y0 == 0), (rule6_y0 == 1))))
s.add(Implies(And((nsntRD_x1<=2*T), Not(nsntRD_y0<=2*T)), Or((rule7_y0 == 0), (rule7_y0 == 1))))
s.add(Implies(And((nsntRD_x1<=2*T), Not(nsntRD_y0<=2*T)), Or((rule8_y0 == 0), (rule8_y0 == 1))))
s.add(Implies(And((nsntRD_x1<=2*T), Not(nsntRD_y0<=2*T)), Or((rule9_y0 == 0), (rule9_y0 == 1))))
s.add(Implies(And((nsntRD_x1<=2*T), Not(nsntRD_y0<=2*T)), rule0_y0+rule1_y0+rule2_y0+rule3_y0+rule4_y0+rule5_y0+rule6_y0+rule7_y0+rule8_y0+rule9_y0 <= 1))


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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule1_y1 - rule2_y1 - rule6_y1 + rule6_y1 ==  loc0_x2 - loc0_y1)
s.add(0 - rule0_y1 ==  loc1_x2 - loc1_y1)
s.add(0 + rule0_y1 + rule1_y1 + rule2_y1 - rule3_y1 - rule4_y1 - rule7_y1 + rule7_y1 ==  locEC_x2 - locEC_y1)
s.add(0 + rule3_y1 + rule4_y1 - rule5_y1 - rule8_y1 + rule8_y1 ==  locRD_x2 - locRD_y1)
s.add(0 + rule5_y1 - rule9_y1 + rule9_y1 ==  locAC_x2 - locAC_y1)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y1 + rule1_y1 + rule2_y1 == nsntEC_x2 - nsntEC_y1)
s.add(0 + rule3_y1 + rule4_y1 == nsntRD_x2 - nsntRD_y1)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y1 > 0), And(True, ) ))
s.add(Implies( (rule1_y1 > 0), And(2*nsntEC_y1>=N+T+1-2*F, ) ))
s.add(Implies( (rule2_y1 > 0), And(nsntRD_y1>=T+1-F, ) ))
s.add(Implies( (rule3_y1 > 0), And(2*nsntEC_y1>=N+T+1-2*F, ) ))
s.add(Implies( (rule4_y1 > 0), And(nsntRD_y1>=T+1-F, ) ))
s.add(Implies( (rule5_y1 > 0), And(2*nsntRD_y1>=2*T+1, ) ))
s.add(Implies( (rule6_y1 > 0), And(2*nsntEC_y1<=N+T, nsntRD_y1<=T, ) ))
s.add(Implies( (rule7_y1 > 0), And(2*nsntEC_y1<=N+T, nsntRD_y1<=T, ) ))
s.add(Implies( (rule8_y1 > 0), And(nsntRD_y1<=2*T, ) ))
s.add(Implies( (rule9_y1 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y1 and x1, if a fall condition is present

s.add((nsntRD_x2<=T) == (nsntRD_y1<=T))
s.add(Implies(And((nsntRD_x2<=T), Not(nsntRD_y1<=T)), Or((rule0_y1 == 0), (rule0_y1 == 1))))
s.add(Implies(And((nsntRD_x2<=T), Not(nsntRD_y1<=T)), Or((rule1_y1 == 0), (rule1_y1 == 1))))
s.add(Implies(And((nsntRD_x2<=T), Not(nsntRD_y1<=T)), Or((rule2_y1 == 0), (rule2_y1 == 1))))
s.add(Implies(And((nsntRD_x2<=T), Not(nsntRD_y1<=T)), Or((rule3_y1 == 0), (rule3_y1 == 1))))
s.add(Implies(And((nsntRD_x2<=T), Not(nsntRD_y1<=T)), Or((rule4_y1 == 0), (rule4_y1 == 1))))
s.add(Implies(And((nsntRD_x2<=T), Not(nsntRD_y1<=T)), Or((rule5_y1 == 0), (rule5_y1 == 1))))
s.add(Implies(And((nsntRD_x2<=T), Not(nsntRD_y1<=T)), Or((rule6_y1 == 0), (rule6_y1 == 1))))
s.add(Implies(And((nsntRD_x2<=T), Not(nsntRD_y1<=T)), Or((rule7_y1 == 0), (rule7_y1 == 1))))
s.add(Implies(And((nsntRD_x2<=T), Not(nsntRD_y1<=T)), Or((rule8_y1 == 0), (rule8_y1 == 1))))
s.add(Implies(And((nsntRD_x2<=T), Not(nsntRD_y1<=T)), Or((rule9_y1 == 0), (rule9_y1 == 1))))
s.add(Implies(And((nsntRD_x2<=T), Not(nsntRD_y1<=T)), rule0_y1+rule1_y1+rule2_y1+rule3_y1+rule4_y1+rule5_y1+rule6_y1+rule7_y1+rule8_y1+rule9_y1 <= 1))

s.add((2*nsntEC_x2<=N+T) == (2*nsntEC_y1<=N+T))
s.add(Implies(And((2*nsntEC_x2<=N+T), Not(2*nsntEC_y1<=N+T)), Or((rule0_y1 == 0), (rule0_y1 == 1))))
s.add(Implies(And((2*nsntEC_x2<=N+T), Not(2*nsntEC_y1<=N+T)), Or((rule1_y1 == 0), (rule1_y1 == 1))))
s.add(Implies(And((2*nsntEC_x2<=N+T), Not(2*nsntEC_y1<=N+T)), Or((rule2_y1 == 0), (rule2_y1 == 1))))
s.add(Implies(And((2*nsntEC_x2<=N+T), Not(2*nsntEC_y1<=N+T)), Or((rule3_y1 == 0), (rule3_y1 == 1))))
s.add(Implies(And((2*nsntEC_x2<=N+T), Not(2*nsntEC_y1<=N+T)), Or((rule4_y1 == 0), (rule4_y1 == 1))))
s.add(Implies(And((2*nsntEC_x2<=N+T), Not(2*nsntEC_y1<=N+T)), Or((rule5_y1 == 0), (rule5_y1 == 1))))
s.add(Implies(And((2*nsntEC_x2<=N+T), Not(2*nsntEC_y1<=N+T)), Or((rule6_y1 == 0), (rule6_y1 == 1))))
s.add(Implies(And((2*nsntEC_x2<=N+T), Not(2*nsntEC_y1<=N+T)), Or((rule7_y1 == 0), (rule7_y1 == 1))))
s.add(Implies(And((2*nsntEC_x2<=N+T), Not(2*nsntEC_y1<=N+T)), Or((rule8_y1 == 0), (rule8_y1 == 1))))
s.add(Implies(And((2*nsntEC_x2<=N+T), Not(2*nsntEC_y1<=N+T)), Or((rule9_y1 == 0), (rule9_y1 == 1))))
s.add(Implies(And((2*nsntEC_x2<=N+T), Not(2*nsntEC_y1<=N+T)), rule0_y1+rule1_y1+rule2_y1+rule3_y1+rule4_y1+rule5_y1+rule6_y1+rule7_y1+rule8_y1+rule9_y1 <= 1))

s.add((nsntRD_x2<=2*T) == (nsntRD_y1<=2*T))
s.add(Implies(And((nsntRD_x2<=2*T), Not(nsntRD_y1<=2*T)), Or((rule0_y1 == 0), (rule0_y1 == 1))))
s.add(Implies(And((nsntRD_x2<=2*T), Not(nsntRD_y1<=2*T)), Or((rule1_y1 == 0), (rule1_y1 == 1))))
s.add(Implies(And((nsntRD_x2<=2*T), Not(nsntRD_y1<=2*T)), Or((rule2_y1 == 0), (rule2_y1 == 1))))
s.add(Implies(And((nsntRD_x2<=2*T), Not(nsntRD_y1<=2*T)), Or((rule3_y1 == 0), (rule3_y1 == 1))))
s.add(Implies(And((nsntRD_x2<=2*T), Not(nsntRD_y1<=2*T)), Or((rule4_y1 == 0), (rule4_y1 == 1))))
s.add(Implies(And((nsntRD_x2<=2*T), Not(nsntRD_y1<=2*T)), Or((rule5_y1 == 0), (rule5_y1 == 1))))
s.add(Implies(And((nsntRD_x2<=2*T), Not(nsntRD_y1<=2*T)), Or((rule6_y1 == 0), (rule6_y1 == 1))))
s.add(Implies(And((nsntRD_x2<=2*T), Not(nsntRD_y1<=2*T)), Or((rule7_y1 == 0), (rule7_y1 == 1))))
s.add(Implies(And((nsntRD_x2<=2*T), Not(nsntRD_y1<=2*T)), Or((rule8_y1 == 0), (rule8_y1 == 1))))
s.add(Implies(And((nsntRD_x2<=2*T), Not(nsntRD_y1<=2*T)), Or((rule9_y1 == 0), (rule9_y1 == 1))))
s.add(Implies(And((nsntRD_x2<=2*T), Not(nsntRD_y1<=2*T)), rule0_y1+rule1_y1+rule2_y1+rule3_y1+rule4_y1+rule5_y1+rule6_y1+rule7_y1+rule8_y1+rule9_y1 <= 1))


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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule1_y2 - rule2_y2 - rule6_y2 + rule6_y2 ==  loc0_x3 - loc0_y2)
s.add(0 - rule0_y2 ==  loc1_x3 - loc1_y2)
s.add(0 + rule0_y2 + rule1_y2 + rule2_y2 - rule3_y2 - rule4_y2 - rule7_y2 + rule7_y2 ==  locEC_x3 - locEC_y2)
s.add(0 + rule3_y2 + rule4_y2 - rule5_y2 - rule8_y2 + rule8_y2 ==  locRD_x3 - locRD_y2)
s.add(0 + rule5_y2 - rule9_y2 + rule9_y2 ==  locAC_x3 - locAC_y2)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y2 + rule1_y2 + rule2_y2 == nsntEC_x3 - nsntEC_y2)
s.add(0 + rule3_y2 + rule4_y2 == nsntRD_x3 - nsntRD_y2)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y2 > 0), And(True, ) ))
s.add(Implies( (rule1_y2 > 0), And(2*nsntEC_y2>=N+T+1-2*F, ) ))
s.add(Implies( (rule2_y2 > 0), And(nsntRD_y2>=T+1-F, ) ))
s.add(Implies( (rule3_y2 > 0), And(2*nsntEC_y2>=N+T+1-2*F, ) ))
s.add(Implies( (rule4_y2 > 0), And(nsntRD_y2>=T+1-F, ) ))
s.add(Implies( (rule5_y2 > 0), And(2*nsntRD_y2>=2*T+1, ) ))
s.add(Implies( (rule6_y2 > 0), And(2*nsntEC_y2<=N+T, nsntRD_y2<=T, ) ))
s.add(Implies( (rule7_y2 > 0), And(2*nsntEC_y2<=N+T, nsntRD_y2<=T, ) ))
s.add(Implies( (rule8_y2 > 0), And(nsntRD_y2<=2*T, ) ))
s.add(Implies( (rule9_y2 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y2 and x2, if a fall condition is present

s.add((nsntRD_x3<=T) == (nsntRD_y2<=T))
s.add(Implies(And((nsntRD_x3<=T), Not(nsntRD_y2<=T)), Or((rule0_y2 == 0), (rule0_y2 == 1))))
s.add(Implies(And((nsntRD_x3<=T), Not(nsntRD_y2<=T)), Or((rule1_y2 == 0), (rule1_y2 == 1))))
s.add(Implies(And((nsntRD_x3<=T), Not(nsntRD_y2<=T)), Or((rule2_y2 == 0), (rule2_y2 == 1))))
s.add(Implies(And((nsntRD_x3<=T), Not(nsntRD_y2<=T)), Or((rule3_y2 == 0), (rule3_y2 == 1))))
s.add(Implies(And((nsntRD_x3<=T), Not(nsntRD_y2<=T)), Or((rule4_y2 == 0), (rule4_y2 == 1))))
s.add(Implies(And((nsntRD_x3<=T), Not(nsntRD_y2<=T)), Or((rule5_y2 == 0), (rule5_y2 == 1))))
s.add(Implies(And((nsntRD_x3<=T), Not(nsntRD_y2<=T)), Or((rule6_y2 == 0), (rule6_y2 == 1))))
s.add(Implies(And((nsntRD_x3<=T), Not(nsntRD_y2<=T)), Or((rule7_y2 == 0), (rule7_y2 == 1))))
s.add(Implies(And((nsntRD_x3<=T), Not(nsntRD_y2<=T)), Or((rule8_y2 == 0), (rule8_y2 == 1))))
s.add(Implies(And((nsntRD_x3<=T), Not(nsntRD_y2<=T)), Or((rule9_y2 == 0), (rule9_y2 == 1))))
s.add(Implies(And((nsntRD_x3<=T), Not(nsntRD_y2<=T)), rule0_y2+rule1_y2+rule2_y2+rule3_y2+rule4_y2+rule5_y2+rule6_y2+rule7_y2+rule8_y2+rule9_y2 <= 1))

s.add((2*nsntEC_x3<=N+T) == (2*nsntEC_y2<=N+T))
s.add(Implies(And((2*nsntEC_x3<=N+T), Not(2*nsntEC_y2<=N+T)), Or((rule0_y2 == 0), (rule0_y2 == 1))))
s.add(Implies(And((2*nsntEC_x3<=N+T), Not(2*nsntEC_y2<=N+T)), Or((rule1_y2 == 0), (rule1_y2 == 1))))
s.add(Implies(And((2*nsntEC_x3<=N+T), Not(2*nsntEC_y2<=N+T)), Or((rule2_y2 == 0), (rule2_y2 == 1))))
s.add(Implies(And((2*nsntEC_x3<=N+T), Not(2*nsntEC_y2<=N+T)), Or((rule3_y2 == 0), (rule3_y2 == 1))))
s.add(Implies(And((2*nsntEC_x3<=N+T), Not(2*nsntEC_y2<=N+T)), Or((rule4_y2 == 0), (rule4_y2 == 1))))
s.add(Implies(And((2*nsntEC_x3<=N+T), Not(2*nsntEC_y2<=N+T)), Or((rule5_y2 == 0), (rule5_y2 == 1))))
s.add(Implies(And((2*nsntEC_x3<=N+T), Not(2*nsntEC_y2<=N+T)), Or((rule6_y2 == 0), (rule6_y2 == 1))))
s.add(Implies(And((2*nsntEC_x3<=N+T), Not(2*nsntEC_y2<=N+T)), Or((rule7_y2 == 0), (rule7_y2 == 1))))
s.add(Implies(And((2*nsntEC_x3<=N+T), Not(2*nsntEC_y2<=N+T)), Or((rule8_y2 == 0), (rule8_y2 == 1))))
s.add(Implies(And((2*nsntEC_x3<=N+T), Not(2*nsntEC_y2<=N+T)), Or((rule9_y2 == 0), (rule9_y2 == 1))))
s.add(Implies(And((2*nsntEC_x3<=N+T), Not(2*nsntEC_y2<=N+T)), rule0_y2+rule1_y2+rule2_y2+rule3_y2+rule4_y2+rule5_y2+rule6_y2+rule7_y2+rule8_y2+rule9_y2 <= 1))

s.add((nsntRD_x3<=2*T) == (nsntRD_y2<=2*T))
s.add(Implies(And((nsntRD_x3<=2*T), Not(nsntRD_y2<=2*T)), Or((rule0_y2 == 0), (rule0_y2 == 1))))
s.add(Implies(And((nsntRD_x3<=2*T), Not(nsntRD_y2<=2*T)), Or((rule1_y2 == 0), (rule1_y2 == 1))))
s.add(Implies(And((nsntRD_x3<=2*T), Not(nsntRD_y2<=2*T)), Or((rule2_y2 == 0), (rule2_y2 == 1))))
s.add(Implies(And((nsntRD_x3<=2*T), Not(nsntRD_y2<=2*T)), Or((rule3_y2 == 0), (rule3_y2 == 1))))
s.add(Implies(And((nsntRD_x3<=2*T), Not(nsntRD_y2<=2*T)), Or((rule4_y2 == 0), (rule4_y2 == 1))))
s.add(Implies(And((nsntRD_x3<=2*T), Not(nsntRD_y2<=2*T)), Or((rule5_y2 == 0), (rule5_y2 == 1))))
s.add(Implies(And((nsntRD_x3<=2*T), Not(nsntRD_y2<=2*T)), Or((rule6_y2 == 0), (rule6_y2 == 1))))
s.add(Implies(And((nsntRD_x3<=2*T), Not(nsntRD_y2<=2*T)), Or((rule7_y2 == 0), (rule7_y2 == 1))))
s.add(Implies(And((nsntRD_x3<=2*T), Not(nsntRD_y2<=2*T)), Or((rule8_y2 == 0), (rule8_y2 == 1))))
s.add(Implies(And((nsntRD_x3<=2*T), Not(nsntRD_y2<=2*T)), Or((rule9_y2 == 0), (rule9_y2 == 1))))
s.add(Implies(And((nsntRD_x3<=2*T), Not(nsntRD_y2<=2*T)), rule0_y2+rule1_y2+rule2_y2+rule3_y2+rule4_y2+rule5_y2+rule6_y2+rule7_y2+rule8_y2+rule9_y2 <= 1))


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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule1_y3 - rule2_y3 - rule6_y3 + rule6_y3 ==  loc0_x4 - loc0_y3)
s.add(0 - rule0_y3 ==  loc1_x4 - loc1_y3)
s.add(0 + rule0_y3 + rule1_y3 + rule2_y3 - rule3_y3 - rule4_y3 - rule7_y3 + rule7_y3 ==  locEC_x4 - locEC_y3)
s.add(0 + rule3_y3 + rule4_y3 - rule5_y3 - rule8_y3 + rule8_y3 ==  locRD_x4 - locRD_y3)
s.add(0 + rule5_y3 - rule9_y3 + rule9_y3 ==  locAC_x4 - locAC_y3)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y3 + rule1_y3 + rule2_y3 == nsntEC_x4 - nsntEC_y3)
s.add(0 + rule3_y3 + rule4_y3 == nsntRD_x4 - nsntRD_y3)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y3 > 0), And(True, ) ))
s.add(Implies( (rule1_y3 > 0), And(2*nsntEC_y3>=N+T+1-2*F, ) ))
s.add(Implies( (rule2_y3 > 0), And(nsntRD_y3>=T+1-F, ) ))
s.add(Implies( (rule3_y3 > 0), And(2*nsntEC_y3>=N+T+1-2*F, ) ))
s.add(Implies( (rule4_y3 > 0), And(nsntRD_y3>=T+1-F, ) ))
s.add(Implies( (rule5_y3 > 0), And(2*nsntRD_y3>=2*T+1, ) ))
s.add(Implies( (rule6_y3 > 0), And(2*nsntEC_y3<=N+T, nsntRD_y3<=T, ) ))
s.add(Implies( (rule7_y3 > 0), And(2*nsntEC_y3<=N+T, nsntRD_y3<=T, ) ))
s.add(Implies( (rule8_y3 > 0), And(nsntRD_y3<=2*T, ) ))
s.add(Implies( (rule9_y3 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y3 and x3, if a fall condition is present

s.add((nsntRD_x4<=T) == (nsntRD_y3<=T))
s.add(Implies(And((nsntRD_x4<=T), Not(nsntRD_y3<=T)), Or((rule0_y3 == 0), (rule0_y3 == 1))))
s.add(Implies(And((nsntRD_x4<=T), Not(nsntRD_y3<=T)), Or((rule1_y3 == 0), (rule1_y3 == 1))))
s.add(Implies(And((nsntRD_x4<=T), Not(nsntRD_y3<=T)), Or((rule2_y3 == 0), (rule2_y3 == 1))))
s.add(Implies(And((nsntRD_x4<=T), Not(nsntRD_y3<=T)), Or((rule3_y3 == 0), (rule3_y3 == 1))))
s.add(Implies(And((nsntRD_x4<=T), Not(nsntRD_y3<=T)), Or((rule4_y3 == 0), (rule4_y3 == 1))))
s.add(Implies(And((nsntRD_x4<=T), Not(nsntRD_y3<=T)), Or((rule5_y3 == 0), (rule5_y3 == 1))))
s.add(Implies(And((nsntRD_x4<=T), Not(nsntRD_y3<=T)), Or((rule6_y3 == 0), (rule6_y3 == 1))))
s.add(Implies(And((nsntRD_x4<=T), Not(nsntRD_y3<=T)), Or((rule7_y3 == 0), (rule7_y3 == 1))))
s.add(Implies(And((nsntRD_x4<=T), Not(nsntRD_y3<=T)), Or((rule8_y3 == 0), (rule8_y3 == 1))))
s.add(Implies(And((nsntRD_x4<=T), Not(nsntRD_y3<=T)), Or((rule9_y3 == 0), (rule9_y3 == 1))))
s.add(Implies(And((nsntRD_x4<=T), Not(nsntRD_y3<=T)), rule0_y3+rule1_y3+rule2_y3+rule3_y3+rule4_y3+rule5_y3+rule6_y3+rule7_y3+rule8_y3+rule9_y3 <= 1))

s.add((2*nsntEC_x4<=N+T) == (2*nsntEC_y3<=N+T))
s.add(Implies(And((2*nsntEC_x4<=N+T), Not(2*nsntEC_y3<=N+T)), Or((rule0_y3 == 0), (rule0_y3 == 1))))
s.add(Implies(And((2*nsntEC_x4<=N+T), Not(2*nsntEC_y3<=N+T)), Or((rule1_y3 == 0), (rule1_y3 == 1))))
s.add(Implies(And((2*nsntEC_x4<=N+T), Not(2*nsntEC_y3<=N+T)), Or((rule2_y3 == 0), (rule2_y3 == 1))))
s.add(Implies(And((2*nsntEC_x4<=N+T), Not(2*nsntEC_y3<=N+T)), Or((rule3_y3 == 0), (rule3_y3 == 1))))
s.add(Implies(And((2*nsntEC_x4<=N+T), Not(2*nsntEC_y3<=N+T)), Or((rule4_y3 == 0), (rule4_y3 == 1))))
s.add(Implies(And((2*nsntEC_x4<=N+T), Not(2*nsntEC_y3<=N+T)), Or((rule5_y3 == 0), (rule5_y3 == 1))))
s.add(Implies(And((2*nsntEC_x4<=N+T), Not(2*nsntEC_y3<=N+T)), Or((rule6_y3 == 0), (rule6_y3 == 1))))
s.add(Implies(And((2*nsntEC_x4<=N+T), Not(2*nsntEC_y3<=N+T)), Or((rule7_y3 == 0), (rule7_y3 == 1))))
s.add(Implies(And((2*nsntEC_x4<=N+T), Not(2*nsntEC_y3<=N+T)), Or((rule8_y3 == 0), (rule8_y3 == 1))))
s.add(Implies(And((2*nsntEC_x4<=N+T), Not(2*nsntEC_y3<=N+T)), Or((rule9_y3 == 0), (rule9_y3 == 1))))
s.add(Implies(And((2*nsntEC_x4<=N+T), Not(2*nsntEC_y3<=N+T)), rule0_y3+rule1_y3+rule2_y3+rule3_y3+rule4_y3+rule5_y3+rule6_y3+rule7_y3+rule8_y3+rule9_y3 <= 1))

s.add((nsntRD_x4<=2*T) == (nsntRD_y3<=2*T))
s.add(Implies(And((nsntRD_x4<=2*T), Not(nsntRD_y3<=2*T)), Or((rule0_y3 == 0), (rule0_y3 == 1))))
s.add(Implies(And((nsntRD_x4<=2*T), Not(nsntRD_y3<=2*T)), Or((rule1_y3 == 0), (rule1_y3 == 1))))
s.add(Implies(And((nsntRD_x4<=2*T), Not(nsntRD_y3<=2*T)), Or((rule2_y3 == 0), (rule2_y3 == 1))))
s.add(Implies(And((nsntRD_x4<=2*T), Not(nsntRD_y3<=2*T)), Or((rule3_y3 == 0), (rule3_y3 == 1))))
s.add(Implies(And((nsntRD_x4<=2*T), Not(nsntRD_y3<=2*T)), Or((rule4_y3 == 0), (rule4_y3 == 1))))
s.add(Implies(And((nsntRD_x4<=2*T), Not(nsntRD_y3<=2*T)), Or((rule5_y3 == 0), (rule5_y3 == 1))))
s.add(Implies(And((nsntRD_x4<=2*T), Not(nsntRD_y3<=2*T)), Or((rule6_y3 == 0), (rule6_y3 == 1))))
s.add(Implies(And((nsntRD_x4<=2*T), Not(nsntRD_y3<=2*T)), Or((rule7_y3 == 0), (rule7_y3 == 1))))
s.add(Implies(And((nsntRD_x4<=2*T), Not(nsntRD_y3<=2*T)), Or((rule8_y3 == 0), (rule8_y3 == 1))))
s.add(Implies(And((nsntRD_x4<=2*T), Not(nsntRD_y3<=2*T)), Or((rule9_y3 == 0), (rule9_y3 == 1))))
s.add(Implies(And((nsntRD_x4<=2*T), Not(nsntRD_y3<=2*T)), rule0_y3+rule1_y3+rule2_y3+rule3_y3+rule4_y3+rule5_y3+rule6_y3+rule7_y3+rule8_y3+rule9_y3 <= 1))


####################################################################################

#Creating constraints for a run between the y4th and x5th configurations

################Step 1#################


#Creating many copies of variables for rules

rule0_y4 = Real('rule0_y4')
s.add(rule0_y4 >= 0)
rule1_y4 = Real('rule1_y4')
s.add(rule1_y4 >= 0)
rule2_y4 = Real('rule2_y4')
s.add(rule2_y4 >= 0)
rule3_y4 = Real('rule3_y4')
s.add(rule3_y4 >= 0)
rule4_y4 = Real('rule4_y4')
s.add(rule4_y4 >= 0)
rule5_y4 = Real('rule5_y4')
s.add(rule5_y4 >= 0)
rule6_y4 = Real('rule6_y4')
s.add(rule6_y4 >= 0)
rule7_y4 = Real('rule7_y4')
s.add(rule7_y4 >= 0)
rule8_y4 = Real('rule8_y4')
s.add(rule8_y4 >= 0)
rule9_y4 = Real('rule9_y4')
s.add(rule9_y4 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule1_y4 - rule2_y4 - rule6_y4 + rule6_y4 ==  loc0_x5 - loc0_y4)
s.add(0 - rule0_y4 ==  loc1_x5 - loc1_y4)
s.add(0 + rule0_y4 + rule1_y4 + rule2_y4 - rule3_y4 - rule4_y4 - rule7_y4 + rule7_y4 ==  locEC_x5 - locEC_y4)
s.add(0 + rule3_y4 + rule4_y4 - rule5_y4 - rule8_y4 + rule8_y4 ==  locRD_x5 - locRD_y4)
s.add(0 + rule5_y4 - rule9_y4 + rule9_y4 ==  locAC_x5 - locAC_y4)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y4 + rule1_y4 + rule2_y4 == nsntEC_x5 - nsntEC_y4)
s.add(0 + rule3_y4 + rule4_y4 == nsntRD_x5 - nsntRD_y4)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y4 > 0), And(True, ) ))
s.add(Implies( (rule1_y4 > 0), And(2*nsntEC_y4>=N+T+1-2*F, ) ))
s.add(Implies( (rule2_y4 > 0), And(nsntRD_y4>=T+1-F, ) ))
s.add(Implies( (rule3_y4 > 0), And(2*nsntEC_y4>=N+T+1-2*F, ) ))
s.add(Implies( (rule4_y4 > 0), And(nsntRD_y4>=T+1-F, ) ))
s.add(Implies( (rule5_y4 > 0), And(2*nsntRD_y4>=2*T+1, ) ))
s.add(Implies( (rule6_y4 > 0), And(2*nsntEC_y4<=N+T, nsntRD_y4<=T, ) ))
s.add(Implies( (rule7_y4 > 0), And(2*nsntEC_y4<=N+T, nsntRD_y4<=T, ) ))
s.add(Implies( (rule8_y4 > 0), And(nsntRD_y4<=2*T, ) ))
s.add(Implies( (rule9_y4 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y4 and x4, if a fall condition is present

s.add((nsntRD_x5<=T) == (nsntRD_y4<=T))
s.add(Implies(And((nsntRD_x5<=T), Not(nsntRD_y4<=T)), Or((rule0_y4 == 0), (rule0_y4 == 1))))
s.add(Implies(And((nsntRD_x5<=T), Not(nsntRD_y4<=T)), Or((rule1_y4 == 0), (rule1_y4 == 1))))
s.add(Implies(And((nsntRD_x5<=T), Not(nsntRD_y4<=T)), Or((rule2_y4 == 0), (rule2_y4 == 1))))
s.add(Implies(And((nsntRD_x5<=T), Not(nsntRD_y4<=T)), Or((rule3_y4 == 0), (rule3_y4 == 1))))
s.add(Implies(And((nsntRD_x5<=T), Not(nsntRD_y4<=T)), Or((rule4_y4 == 0), (rule4_y4 == 1))))
s.add(Implies(And((nsntRD_x5<=T), Not(nsntRD_y4<=T)), Or((rule5_y4 == 0), (rule5_y4 == 1))))
s.add(Implies(And((nsntRD_x5<=T), Not(nsntRD_y4<=T)), Or((rule6_y4 == 0), (rule6_y4 == 1))))
s.add(Implies(And((nsntRD_x5<=T), Not(nsntRD_y4<=T)), Or((rule7_y4 == 0), (rule7_y4 == 1))))
s.add(Implies(And((nsntRD_x5<=T), Not(nsntRD_y4<=T)), Or((rule8_y4 == 0), (rule8_y4 == 1))))
s.add(Implies(And((nsntRD_x5<=T), Not(nsntRD_y4<=T)), Or((rule9_y4 == 0), (rule9_y4 == 1))))
s.add(Implies(And((nsntRD_x5<=T), Not(nsntRD_y4<=T)), rule0_y4+rule1_y4+rule2_y4+rule3_y4+rule4_y4+rule5_y4+rule6_y4+rule7_y4+rule8_y4+rule9_y4 <= 1))

s.add((2*nsntEC_x5<=N+T) == (2*nsntEC_y4<=N+T))
s.add(Implies(And((2*nsntEC_x5<=N+T), Not(2*nsntEC_y4<=N+T)), Or((rule0_y4 == 0), (rule0_y4 == 1))))
s.add(Implies(And((2*nsntEC_x5<=N+T), Not(2*nsntEC_y4<=N+T)), Or((rule1_y4 == 0), (rule1_y4 == 1))))
s.add(Implies(And((2*nsntEC_x5<=N+T), Not(2*nsntEC_y4<=N+T)), Or((rule2_y4 == 0), (rule2_y4 == 1))))
s.add(Implies(And((2*nsntEC_x5<=N+T), Not(2*nsntEC_y4<=N+T)), Or((rule3_y4 == 0), (rule3_y4 == 1))))
s.add(Implies(And((2*nsntEC_x5<=N+T), Not(2*nsntEC_y4<=N+T)), Or((rule4_y4 == 0), (rule4_y4 == 1))))
s.add(Implies(And((2*nsntEC_x5<=N+T), Not(2*nsntEC_y4<=N+T)), Or((rule5_y4 == 0), (rule5_y4 == 1))))
s.add(Implies(And((2*nsntEC_x5<=N+T), Not(2*nsntEC_y4<=N+T)), Or((rule6_y4 == 0), (rule6_y4 == 1))))
s.add(Implies(And((2*nsntEC_x5<=N+T), Not(2*nsntEC_y4<=N+T)), Or((rule7_y4 == 0), (rule7_y4 == 1))))
s.add(Implies(And((2*nsntEC_x5<=N+T), Not(2*nsntEC_y4<=N+T)), Or((rule8_y4 == 0), (rule8_y4 == 1))))
s.add(Implies(And((2*nsntEC_x5<=N+T), Not(2*nsntEC_y4<=N+T)), Or((rule9_y4 == 0), (rule9_y4 == 1))))
s.add(Implies(And((2*nsntEC_x5<=N+T), Not(2*nsntEC_y4<=N+T)), rule0_y4+rule1_y4+rule2_y4+rule3_y4+rule4_y4+rule5_y4+rule6_y4+rule7_y4+rule8_y4+rule9_y4 <= 1))

s.add((nsntRD_x5<=2*T) == (nsntRD_y4<=2*T))
s.add(Implies(And((nsntRD_x5<=2*T), Not(nsntRD_y4<=2*T)), Or((rule0_y4 == 0), (rule0_y4 == 1))))
s.add(Implies(And((nsntRD_x5<=2*T), Not(nsntRD_y4<=2*T)), Or((rule1_y4 == 0), (rule1_y4 == 1))))
s.add(Implies(And((nsntRD_x5<=2*T), Not(nsntRD_y4<=2*T)), Or((rule2_y4 == 0), (rule2_y4 == 1))))
s.add(Implies(And((nsntRD_x5<=2*T), Not(nsntRD_y4<=2*T)), Or((rule3_y4 == 0), (rule3_y4 == 1))))
s.add(Implies(And((nsntRD_x5<=2*T), Not(nsntRD_y4<=2*T)), Or((rule4_y4 == 0), (rule4_y4 == 1))))
s.add(Implies(And((nsntRD_x5<=2*T), Not(nsntRD_y4<=2*T)), Or((rule5_y4 == 0), (rule5_y4 == 1))))
s.add(Implies(And((nsntRD_x5<=2*T), Not(nsntRD_y4<=2*T)), Or((rule6_y4 == 0), (rule6_y4 == 1))))
s.add(Implies(And((nsntRD_x5<=2*T), Not(nsntRD_y4<=2*T)), Or((rule7_y4 == 0), (rule7_y4 == 1))))
s.add(Implies(And((nsntRD_x5<=2*T), Not(nsntRD_y4<=2*T)), Or((rule8_y4 == 0), (rule8_y4 == 1))))
s.add(Implies(And((nsntRD_x5<=2*T), Not(nsntRD_y4<=2*T)), Or((rule9_y4 == 0), (rule9_y4 == 1))))
s.add(Implies(And((nsntRD_x5<=2*T), Not(nsntRD_y4<=2*T)), rule0_y4+rule1_y4+rule2_y4+rule3_y4+rule4_y4+rule5_y4+rule6_y4+rule7_y4+rule8_y4+rule9_y4 <= 1))


####################################################################################

#Creating constraints for a run between the y5th and x6th configurations

################Step 1#################


#Creating many copies of variables for rules

rule0_y5 = Real('rule0_y5')
s.add(rule0_y5 >= 0)
rule1_y5 = Real('rule1_y5')
s.add(rule1_y5 >= 0)
rule2_y5 = Real('rule2_y5')
s.add(rule2_y5 >= 0)
rule3_y5 = Real('rule3_y5')
s.add(rule3_y5 >= 0)
rule4_y5 = Real('rule4_y5')
s.add(rule4_y5 >= 0)
rule5_y5 = Real('rule5_y5')
s.add(rule5_y5 >= 0)
rule6_y5 = Real('rule6_y5')
s.add(rule6_y5 >= 0)
rule7_y5 = Real('rule7_y5')
s.add(rule7_y5 >= 0)
rule8_y5 = Real('rule8_y5')
s.add(rule8_y5 >= 0)
rule9_y5 = Real('rule9_y5')
s.add(rule9_y5 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule1_y5 - rule2_y5 - rule6_y5 + rule6_y5 ==  loc0_x6 - loc0_y5)
s.add(0 - rule0_y5 ==  loc1_x6 - loc1_y5)
s.add(0 + rule0_y5 + rule1_y5 + rule2_y5 - rule3_y5 - rule4_y5 - rule7_y5 + rule7_y5 ==  locEC_x6 - locEC_y5)
s.add(0 + rule3_y5 + rule4_y5 - rule5_y5 - rule8_y5 + rule8_y5 ==  locRD_x6 - locRD_y5)
s.add(0 + rule5_y5 - rule9_y5 + rule9_y5 ==  locAC_x6 - locAC_y5)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y5 + rule1_y5 + rule2_y5 == nsntEC_x6 - nsntEC_y5)
s.add(0 + rule3_y5 + rule4_y5 == nsntRD_x6 - nsntRD_y5)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y5 > 0), And(True, ) ))
s.add(Implies( (rule1_y5 > 0), And(2*nsntEC_y5>=N+T+1-2*F, ) ))
s.add(Implies( (rule2_y5 > 0), And(nsntRD_y5>=T+1-F, ) ))
s.add(Implies( (rule3_y5 > 0), And(2*nsntEC_y5>=N+T+1-2*F, ) ))
s.add(Implies( (rule4_y5 > 0), And(nsntRD_y5>=T+1-F, ) ))
s.add(Implies( (rule5_y5 > 0), And(2*nsntRD_y5>=2*T+1, ) ))
s.add(Implies( (rule6_y5 > 0), And(2*nsntEC_y5<=N+T, nsntRD_y5<=T, ) ))
s.add(Implies( (rule7_y5 > 0), And(2*nsntEC_y5<=N+T, nsntRD_y5<=T, ) ))
s.add(Implies( (rule8_y5 > 0), And(nsntRD_y5<=2*T, ) ))
s.add(Implies( (rule9_y5 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y5 and x5, if a fall condition is present

s.add((nsntRD_x6<=T) == (nsntRD_y5<=T))
s.add(Implies(And((nsntRD_x6<=T), Not(nsntRD_y5<=T)), Or((rule0_y5 == 0), (rule0_y5 == 1))))
s.add(Implies(And((nsntRD_x6<=T), Not(nsntRD_y5<=T)), Or((rule1_y5 == 0), (rule1_y5 == 1))))
s.add(Implies(And((nsntRD_x6<=T), Not(nsntRD_y5<=T)), Or((rule2_y5 == 0), (rule2_y5 == 1))))
s.add(Implies(And((nsntRD_x6<=T), Not(nsntRD_y5<=T)), Or((rule3_y5 == 0), (rule3_y5 == 1))))
s.add(Implies(And((nsntRD_x6<=T), Not(nsntRD_y5<=T)), Or((rule4_y5 == 0), (rule4_y5 == 1))))
s.add(Implies(And((nsntRD_x6<=T), Not(nsntRD_y5<=T)), Or((rule5_y5 == 0), (rule5_y5 == 1))))
s.add(Implies(And((nsntRD_x6<=T), Not(nsntRD_y5<=T)), Or((rule6_y5 == 0), (rule6_y5 == 1))))
s.add(Implies(And((nsntRD_x6<=T), Not(nsntRD_y5<=T)), Or((rule7_y5 == 0), (rule7_y5 == 1))))
s.add(Implies(And((nsntRD_x6<=T), Not(nsntRD_y5<=T)), Or((rule8_y5 == 0), (rule8_y5 == 1))))
s.add(Implies(And((nsntRD_x6<=T), Not(nsntRD_y5<=T)), Or((rule9_y5 == 0), (rule9_y5 == 1))))
s.add(Implies(And((nsntRD_x6<=T), Not(nsntRD_y5<=T)), rule0_y5+rule1_y5+rule2_y5+rule3_y5+rule4_y5+rule5_y5+rule6_y5+rule7_y5+rule8_y5+rule9_y5 <= 1))

s.add((2*nsntEC_x6<=N+T) == (2*nsntEC_y5<=N+T))
s.add(Implies(And((2*nsntEC_x6<=N+T), Not(2*nsntEC_y5<=N+T)), Or((rule0_y5 == 0), (rule0_y5 == 1))))
s.add(Implies(And((2*nsntEC_x6<=N+T), Not(2*nsntEC_y5<=N+T)), Or((rule1_y5 == 0), (rule1_y5 == 1))))
s.add(Implies(And((2*nsntEC_x6<=N+T), Not(2*nsntEC_y5<=N+T)), Or((rule2_y5 == 0), (rule2_y5 == 1))))
s.add(Implies(And((2*nsntEC_x6<=N+T), Not(2*nsntEC_y5<=N+T)), Or((rule3_y5 == 0), (rule3_y5 == 1))))
s.add(Implies(And((2*nsntEC_x6<=N+T), Not(2*nsntEC_y5<=N+T)), Or((rule4_y5 == 0), (rule4_y5 == 1))))
s.add(Implies(And((2*nsntEC_x6<=N+T), Not(2*nsntEC_y5<=N+T)), Or((rule5_y5 == 0), (rule5_y5 == 1))))
s.add(Implies(And((2*nsntEC_x6<=N+T), Not(2*nsntEC_y5<=N+T)), Or((rule6_y5 == 0), (rule6_y5 == 1))))
s.add(Implies(And((2*nsntEC_x6<=N+T), Not(2*nsntEC_y5<=N+T)), Or((rule7_y5 == 0), (rule7_y5 == 1))))
s.add(Implies(And((2*nsntEC_x6<=N+T), Not(2*nsntEC_y5<=N+T)), Or((rule8_y5 == 0), (rule8_y5 == 1))))
s.add(Implies(And((2*nsntEC_x6<=N+T), Not(2*nsntEC_y5<=N+T)), Or((rule9_y5 == 0), (rule9_y5 == 1))))
s.add(Implies(And((2*nsntEC_x6<=N+T), Not(2*nsntEC_y5<=N+T)), rule0_y5+rule1_y5+rule2_y5+rule3_y5+rule4_y5+rule5_y5+rule6_y5+rule7_y5+rule8_y5+rule9_y5 <= 1))

s.add((nsntRD_x6<=2*T) == (nsntRD_y5<=2*T))
s.add(Implies(And((nsntRD_x6<=2*T), Not(nsntRD_y5<=2*T)), Or((rule0_y5 == 0), (rule0_y5 == 1))))
s.add(Implies(And((nsntRD_x6<=2*T), Not(nsntRD_y5<=2*T)), Or((rule1_y5 == 0), (rule1_y5 == 1))))
s.add(Implies(And((nsntRD_x6<=2*T), Not(nsntRD_y5<=2*T)), Or((rule2_y5 == 0), (rule2_y5 == 1))))
s.add(Implies(And((nsntRD_x6<=2*T), Not(nsntRD_y5<=2*T)), Or((rule3_y5 == 0), (rule3_y5 == 1))))
s.add(Implies(And((nsntRD_x6<=2*T), Not(nsntRD_y5<=2*T)), Or((rule4_y5 == 0), (rule4_y5 == 1))))
s.add(Implies(And((nsntRD_x6<=2*T), Not(nsntRD_y5<=2*T)), Or((rule5_y5 == 0), (rule5_y5 == 1))))
s.add(Implies(And((nsntRD_x6<=2*T), Not(nsntRD_y5<=2*T)), Or((rule6_y5 == 0), (rule6_y5 == 1))))
s.add(Implies(And((nsntRD_x6<=2*T), Not(nsntRD_y5<=2*T)), Or((rule7_y5 == 0), (rule7_y5 == 1))))
s.add(Implies(And((nsntRD_x6<=2*T), Not(nsntRD_y5<=2*T)), Or((rule8_y5 == 0), (rule8_y5 == 1))))
s.add(Implies(And((nsntRD_x6<=2*T), Not(nsntRD_y5<=2*T)), Or((rule9_y5 == 0), (rule9_y5 == 1))))
s.add(Implies(And((nsntRD_x6<=2*T), Not(nsntRD_y5<=2*T)), rule0_y5+rule1_y5+rule2_y5+rule3_y5+rule4_y5+rule5_y5+rule6_y5+rule7_y5+rule8_y5+rule9_y5 <= 1))


####################################################################################

#Creating constraints for a run between the y6th and x7th configurations

################Step 1#################


#Creating many copies of variables for rules

rule0_y6 = Real('rule0_y6')
s.add(rule0_y6 >= 0)
rule1_y6 = Real('rule1_y6')
s.add(rule1_y6 >= 0)
rule2_y6 = Real('rule2_y6')
s.add(rule2_y6 >= 0)
rule3_y6 = Real('rule3_y6')
s.add(rule3_y6 >= 0)
rule4_y6 = Real('rule4_y6')
s.add(rule4_y6 >= 0)
rule5_y6 = Real('rule5_y6')
s.add(rule5_y6 >= 0)
rule6_y6 = Real('rule6_y6')
s.add(rule6_y6 >= 0)
rule7_y6 = Real('rule7_y6')
s.add(rule7_y6 >= 0)
rule8_y6 = Real('rule8_y6')
s.add(rule8_y6 >= 0)
rule9_y6 = Real('rule9_y6')
s.add(rule9_y6 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule1_y6 - rule2_y6 - rule6_y6 + rule6_y6 ==  loc0_x7 - loc0_y6)
s.add(0 - rule0_y6 ==  loc1_x7 - loc1_y6)
s.add(0 + rule0_y6 + rule1_y6 + rule2_y6 - rule3_y6 - rule4_y6 - rule7_y6 + rule7_y6 ==  locEC_x7 - locEC_y6)
s.add(0 + rule3_y6 + rule4_y6 - rule5_y6 - rule8_y6 + rule8_y6 ==  locRD_x7 - locRD_y6)
s.add(0 + rule5_y6 - rule9_y6 + rule9_y6 ==  locAC_x7 - locAC_y6)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y6 + rule1_y6 + rule2_y6 == nsntEC_x7 - nsntEC_y6)
s.add(0 + rule3_y6 + rule4_y6 == nsntRD_x7 - nsntRD_y6)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y6 > 0), And(True, ) ))
s.add(Implies( (rule1_y6 > 0), And(2*nsntEC_y6>=N+T+1-2*F, ) ))
s.add(Implies( (rule2_y6 > 0), And(nsntRD_y6>=T+1-F, ) ))
s.add(Implies( (rule3_y6 > 0), And(2*nsntEC_y6>=N+T+1-2*F, ) ))
s.add(Implies( (rule4_y6 > 0), And(nsntRD_y6>=T+1-F, ) ))
s.add(Implies( (rule5_y6 > 0), And(2*nsntRD_y6>=2*T+1, ) ))
s.add(Implies( (rule6_y6 > 0), And(2*nsntEC_y6<=N+T, nsntRD_y6<=T, ) ))
s.add(Implies( (rule7_y6 > 0), And(2*nsntEC_y6<=N+T, nsntRD_y6<=T, ) ))
s.add(Implies( (rule8_y6 > 0), And(nsntRD_y6<=2*T, ) ))
s.add(Implies( (rule9_y6 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y6 and x6, if a fall condition is present

s.add((nsntRD_x7<=T) == (nsntRD_y6<=T))
s.add(Implies(And((nsntRD_x7<=T), Not(nsntRD_y6<=T)), Or((rule0_y6 == 0), (rule0_y6 == 1))))
s.add(Implies(And((nsntRD_x7<=T), Not(nsntRD_y6<=T)), Or((rule1_y6 == 0), (rule1_y6 == 1))))
s.add(Implies(And((nsntRD_x7<=T), Not(nsntRD_y6<=T)), Or((rule2_y6 == 0), (rule2_y6 == 1))))
s.add(Implies(And((nsntRD_x7<=T), Not(nsntRD_y6<=T)), Or((rule3_y6 == 0), (rule3_y6 == 1))))
s.add(Implies(And((nsntRD_x7<=T), Not(nsntRD_y6<=T)), Or((rule4_y6 == 0), (rule4_y6 == 1))))
s.add(Implies(And((nsntRD_x7<=T), Not(nsntRD_y6<=T)), Or((rule5_y6 == 0), (rule5_y6 == 1))))
s.add(Implies(And((nsntRD_x7<=T), Not(nsntRD_y6<=T)), Or((rule6_y6 == 0), (rule6_y6 == 1))))
s.add(Implies(And((nsntRD_x7<=T), Not(nsntRD_y6<=T)), Or((rule7_y6 == 0), (rule7_y6 == 1))))
s.add(Implies(And((nsntRD_x7<=T), Not(nsntRD_y6<=T)), Or((rule8_y6 == 0), (rule8_y6 == 1))))
s.add(Implies(And((nsntRD_x7<=T), Not(nsntRD_y6<=T)), Or((rule9_y6 == 0), (rule9_y6 == 1))))
s.add(Implies(And((nsntRD_x7<=T), Not(nsntRD_y6<=T)), rule0_y6+rule1_y6+rule2_y6+rule3_y6+rule4_y6+rule5_y6+rule6_y6+rule7_y6+rule8_y6+rule9_y6 <= 1))

s.add((2*nsntEC_x7<=N+T) == (2*nsntEC_y6<=N+T))
s.add(Implies(And((2*nsntEC_x7<=N+T), Not(2*nsntEC_y6<=N+T)), Or((rule0_y6 == 0), (rule0_y6 == 1))))
s.add(Implies(And((2*nsntEC_x7<=N+T), Not(2*nsntEC_y6<=N+T)), Or((rule1_y6 == 0), (rule1_y6 == 1))))
s.add(Implies(And((2*nsntEC_x7<=N+T), Not(2*nsntEC_y6<=N+T)), Or((rule2_y6 == 0), (rule2_y6 == 1))))
s.add(Implies(And((2*nsntEC_x7<=N+T), Not(2*nsntEC_y6<=N+T)), Or((rule3_y6 == 0), (rule3_y6 == 1))))
s.add(Implies(And((2*nsntEC_x7<=N+T), Not(2*nsntEC_y6<=N+T)), Or((rule4_y6 == 0), (rule4_y6 == 1))))
s.add(Implies(And((2*nsntEC_x7<=N+T), Not(2*nsntEC_y6<=N+T)), Or((rule5_y6 == 0), (rule5_y6 == 1))))
s.add(Implies(And((2*nsntEC_x7<=N+T), Not(2*nsntEC_y6<=N+T)), Or((rule6_y6 == 0), (rule6_y6 == 1))))
s.add(Implies(And((2*nsntEC_x7<=N+T), Not(2*nsntEC_y6<=N+T)), Or((rule7_y6 == 0), (rule7_y6 == 1))))
s.add(Implies(And((2*nsntEC_x7<=N+T), Not(2*nsntEC_y6<=N+T)), Or((rule8_y6 == 0), (rule8_y6 == 1))))
s.add(Implies(And((2*nsntEC_x7<=N+T), Not(2*nsntEC_y6<=N+T)), Or((rule9_y6 == 0), (rule9_y6 == 1))))
s.add(Implies(And((2*nsntEC_x7<=N+T), Not(2*nsntEC_y6<=N+T)), rule0_y6+rule1_y6+rule2_y6+rule3_y6+rule4_y6+rule5_y6+rule6_y6+rule7_y6+rule8_y6+rule9_y6 <= 1))

s.add((nsntRD_x7<=2*T) == (nsntRD_y6<=2*T))
s.add(Implies(And((nsntRD_x7<=2*T), Not(nsntRD_y6<=2*T)), Or((rule0_y6 == 0), (rule0_y6 == 1))))
s.add(Implies(And((nsntRD_x7<=2*T), Not(nsntRD_y6<=2*T)), Or((rule1_y6 == 0), (rule1_y6 == 1))))
s.add(Implies(And((nsntRD_x7<=2*T), Not(nsntRD_y6<=2*T)), Or((rule2_y6 == 0), (rule2_y6 == 1))))
s.add(Implies(And((nsntRD_x7<=2*T), Not(nsntRD_y6<=2*T)), Or((rule3_y6 == 0), (rule3_y6 == 1))))
s.add(Implies(And((nsntRD_x7<=2*T), Not(nsntRD_y6<=2*T)), Or((rule4_y6 == 0), (rule4_y6 == 1))))
s.add(Implies(And((nsntRD_x7<=2*T), Not(nsntRD_y6<=2*T)), Or((rule5_y6 == 0), (rule5_y6 == 1))))
s.add(Implies(And((nsntRD_x7<=2*T), Not(nsntRD_y6<=2*T)), Or((rule6_y6 == 0), (rule6_y6 == 1))))
s.add(Implies(And((nsntRD_x7<=2*T), Not(nsntRD_y6<=2*T)), Or((rule7_y6 == 0), (rule7_y6 == 1))))
s.add(Implies(And((nsntRD_x7<=2*T), Not(nsntRD_y6<=2*T)), Or((rule8_y6 == 0), (rule8_y6 == 1))))
s.add(Implies(And((nsntRD_x7<=2*T), Not(nsntRD_y6<=2*T)), Or((rule9_y6 == 0), (rule9_y6 == 1))))
s.add(Implies(And((nsntRD_x7<=2*T), Not(nsntRD_y6<=2*T)), rule0_y6+rule1_y6+rule2_y6+rule3_y6+rule4_y6+rule5_y6+rule6_y6+rule7_y6+rule8_y6+rule9_y6 <= 1))


#############Additional step for the final configuration#####################


###########Ensure that the last configuration satisfies the final condition#############

s.add(Or(locAC_y7 != 0, locAC_y7 != 0))






if s.check() == sat:

	print("Specification not satisfied")

else:

	print("Specification satisfied")
